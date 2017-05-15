# BMICalculator.py
# Your job is to write a BMI calculator that matches the formula
# and chart on http://flightphysical.com/medical-exam/weight

# Define Function below
# be sure to return an integer

import math
def calculateBMI(h, w):

    BMI = w/h**2*703
    BMI = round(BMI, 0)
    return BMI

if __name__ == '__main__':
    # Call the function in here if you want to test it
    # Make sure it's indented
    pass # remove or comment out this line if you wish to test the function 
