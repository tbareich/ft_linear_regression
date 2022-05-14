from genericpath import exists
from model import f


def get_mileage(theta_0, theta_1):
    try:
        mileage_arg = input("Tap a car mileage: ")
        mileage = float(mileage_arg)
        print(f(mileage, theta_0, theta_1))
    except ValueError as e:
        print('Enter a valid number.')
        get_mileage(theta_0, theta_1)


try:
    theta_0 = 0
    theta_1 = 0
    if exists('weights'):
        file = open('weights', 'r')
        weights = file.readline().split(' ')
        theta_0 = float(weights[0])
        theta_1 = float(weights[1])
    get_mileage(theta_0, theta_1)
except Exception as e:
    print('Something went wrong.')
