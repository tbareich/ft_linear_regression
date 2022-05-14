import numpy as np
import csv
import matplotlib
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
epochs = 700

parser = argparse.ArgumentParser(
    description='Train a linear regression model.')
parser.add_argument(
    'file',
    metavar='filename',
    type=str,
    help=
    'the file containing the data for which the linear model will be trained with.'
)
parser.add_argument(
    '--plot',
    action='store_const',
    const=True,
    default=False,
    help=
    'plot trained data with a linear function representing the predictions.')
parser.add_argument('--calc_precision',
                    action='store_const',
                    const=True,
                    default=False,
                    help='calculate the precision of the algorithm.')
args = parser.parse_args()
plot = args.plot
filename = args.file
calc_precision = args.calc_precision

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

    def update_weights(i):
        global theta_0, theta_1, epochs
        tmp_theta_0 = (1 / m) * sum(f(X, theta_0, theta_1) - Y)
        tmp_theta_1 = (1 / m) * \
         sum(X * (f(X, theta_0, theta_1) - Y))
        theta_0 -= learning_rate * tmp_theta_0
        theta_1 -= learning_rate * tmp_theta_1
        line.set_data((X * maxX, f(X, theta_0, theta_1) * maxY))
        epochs -= 1

    def plot_avp_prices(X, Y):
        global line, epochs
        plt.title('Car mileage versus car price')
        plt.scatter(X * maxX, Y * maxY, label='Actual prices')
        plt.xlabel('Mileage (Km)')
        plt.ylabel('Price ($)')
        plt.xlim(0)
        plt.ylim(0)
        line.set_label('Estimated regression line')
        line.set_color('red')
        anim = FuncAnimation(fig,
                             update_weights,
                             repeat=False,
                             frames=epochs,
                             interval=1)
        plt.legend()
        plt.show()

    if plot == 1:
        plot_avp_prices(X, Y)
    while epochs > 0:
        update_weights(0)
    theta_0 *= maxY
    theta_1 *= maxY / maxX
    file = open("weights", "w")
    file.write(f'{theta_0} {theta_1}')
    file.close()
    if calc_precision:
        Y = Y * maxY
        X = X * maxX
        precision = sum((Y - abs(Y - f(X, theta_0, theta_1))) / Y) / m * 100
        print('precision: %.2f%%' % precision)
except OSError as e:
    print('The training file does\'t exist.')
except Exception as e:
    print('Something went wrong.')