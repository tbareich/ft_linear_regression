from statistics import mode
import string
import numpy as np
import csv
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import argparse
from model import f

plt.rcParams.update({
    'figure.figsize': (8, 6),
    'figure.facecolor': 'white',
    'axes.titlesize': 'x-large',
    'axes.labelsize': 'large',
    'xtick.labelsize': 'medium',
    'ytick.labelsize': 'medium',
    'axes.grid': True,
    'grid.linewidth': 0.5,
    'grid.alpha': 0.3
})

theta_0 = 0.0
theta_1 = 0.0
learning_rate = 0.1
epoch = 1000
plot = 0

parser = argparse.ArgumentParser(description='Train a Linear model.')
parser.add_argument('file',
                    metavar='filename',
                    type=str,
                    help='file containing data to be train with.')
parser.add_argument('--plot',
                    dest='plot',
                    action='store_const',
                    const=1,
                    default=0,
                    help='plot data with predictions.')
args = parser.parse_args()
plot = args.plot
filename = args.file

try:
    X = np.array([])
    Y = np.array([])
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file)
        i = 0
        for row in csv_reader:
            if i != 0:
                X = np.append(X, float(row[0]))
                Y = np.append(Y, float(row[1]))
            i += 1
    m = len(X)

    maxX = max(X)
    maxY = max(Y)
    X = X / maxX
    Y = Y / maxY

    def cost():
        return (1 / (2 * m)) * sum((f(X, theta_0, theta_1) - Y)**2)

    fig, ax = plt.subplots()
    line, = ax.plot([])

    def update_weights(_):
        global theta_0, theta_1, epoch
        tmp_theta_0 = (1 / m) * sum(f(X, theta_0, theta_1) - Y)
        tmp_theta_1 = (1 / m) * sum(X * (f(X, theta_0, theta_1) - Y))
        theta_0 -= learning_rate * tmp_theta_0
        theta_1 -= learning_rate * tmp_theta_1
        line.set_data((X * maxX, f(X, theta_0, theta_1) * maxY))
        epoch -= 1

    def plot_avp_prices(X, Y):
        global line, epoch
        plt.title('Car mileage versus car price')
        plt.scatter(X * maxX, Y * maxY, label='Actual prices')
        plt.xlabel('Mileage (Km)')
        plt.ylabel('Price ($)')
        plt.xlim(0)
        plt.ylim(0)
        anim = FuncAnimation(fig, update_weights, frames=1000, interval=20)
        line.set_label('Predicted prices')
        line.set_color('red')
        plt.legend()
        plt.show()

    if plot == 1:
        plot_avp_prices(X, Y)
    else:
        while epoch > 0:
            update_weights(0)
    theta_0 *= maxY
    theta_1 *= maxY / maxX

    f = open("weights", "w")
    f.write(f'{theta_0} {theta_1}')
    f.close()
except:
    print('The training file does\'t exist.')
