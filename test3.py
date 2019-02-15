import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
    tip = (meal_cost * tip_percent)/100
    tax = (meal_cost * tax_percent)/100
    total_cost = meal_cost + tip + tax
    return round(total_cost)

if __name__ == '__main__':
    meal_cost = float(input('Enter the meal cost :'))

    tip_percent = int(input('Enter the percentage tip :'))

    tax_percent = int(input('Enter the percentage tax :'))

    solve(meal_cost, tip_percent, tax_percent)
