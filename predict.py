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
    mileage_arg = args.mileage
    mileage = float(mileage_arg)
    file = open('weights', 'r')
    weights = file.readline().split(' ')
    theta_0 = float(weights[0])
    theta_1 = float(weights[1])
    print(f(mileage, theta_0, theta_1))
except OSError as e:
    print('The weights file doesn\'t exist, try to run the train program.')
except ValueError as e:
    print('Please insert a valid number.')
except Exception as e:
    print('Something went wrong.')
