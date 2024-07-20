# !/usr/bin/env python3

# Script name: Assignment 3-3
# Author Name: Christen Reinhart
# Date of Latest Revision: 05/30/2024
# Purpose: Calculculate Date

# This Calculates Dates
# Input: Interactive Year, Month, Day
# Output: Calculate date based upon inputs

# start

# Constants
MIN_YEAR = 0
MIN_MONTH = 1
MAX_MONTH = 12
MIN_DAY = 1
MAX_DAY = 31

# variable to determine if the date is valid
validDate = True

# month, and day from the user
try:
    year = int(input("Enter year: "))
    month = int(input("Enter month (1-12): "))
    day = int(input("Enter day: "))
except ValueError:
    print("Invalid input. Please enter numeric values for year, month, and day.")
    validDate = False

# check year
if validDate:
    if year < MIN_YEAR:
        validDate = False
    # Check month
    elif month < MIN_MONTH or month > MAX_MONTH:
        validDate = False
    else:
        # Check day based on month
        if month in [4, 6, 9, 11] and (day < MIN_DAY or day > 30):  
            validDate = False
        elif month == 2 and (day < MIN_DAY or day > 28):  
            validDate = False
        elif day < MIN_DAY or day > MAX_DAY:  
            validDate = False

# output the result
if validDate:
    print(f"{month}/{day}/{year} is a valid date.")
else:
    if validDate: # checks to see if date is valid before proceeding
        print(f"{month}/{day}/{year} is an invalid date.")

# end
