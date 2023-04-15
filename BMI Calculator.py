# Ariann Decker
# 4/13/2023
# BMI Calculator
import math
from tabulate import tabulate

# Create Function
def BMI_Calc():

# Ask user for Weight and Height
    # Accept User question Input
    weight = float(input('Please enter your Weight in Lbs: '))
    height = float(input('Please enter your Height in Inches: '))

   # print(weight + 'Lbs',height + 'Inches')

# Perform BMI Calculation
    BMI = float(weight / (height**2) * 703)
    print("Your BMI is: " + "%.1f" % BMI)


# If Statement for details about BMI
# Underweight, Healthy Weight,Overweight, Obesity
    if BMI <= 18.5:
        print("Based on the information you entered, your BMI suggests you are Underweight.")
    elif 18.5 < BMI < 24.9:
        print("Based on the information you entered, your BMI suggests you are a healthy weight!")
    elif 25.0 < BMI < 29.9:
        print("Based on the information you entered, your BMI suggests you are Overweight.")
    else:
        print("Based on the information you entered, your BMI suggests you are Obese.")

    

BMI_Calc()
