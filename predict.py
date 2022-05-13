import sys

from numpy import integer
from model import f
import argparse

try:
    parser = argparse.ArgumentParser(
        description='Predict cars prices using linear model.')
    parser.add_argument('mileage',
                        metavar='car_mileage',
                        type=str,
                        help='car mileage.')
    args = parser.parse_args()
    mileage = float(args.mileage)
    file = open('weights', 'r')
    weights = file.readline().split(' ')
    theta_0 = float(weights[0])
    theta_1 = float(weights[1])
    print(f(mileage, theta_0, theta_1))
except OSError as e:
    print('The "weights" file doesn\'t exist, try to run "train.py".')
except Exception as e:
    print('Something went wrong')
