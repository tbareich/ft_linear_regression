import sys
from model import f

try:
    file = open('weights', 'r')
    weights = file.readline().split(' ')
    theta_0 = float(weights[0])
    theta_1 = float(weights[1])
    arg = float(sys.argv[1])
    print(f(arg, theta_0, theta_1))
except IndexError as e:
    print('')
except OSError as e:
    print('The "weights" file doesn\'t exist, try to run "train.py".')
except Exception as e:
    print('Something went wrong')
