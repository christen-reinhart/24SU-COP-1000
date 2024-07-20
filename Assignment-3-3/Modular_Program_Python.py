# !/usr/bin/env python3

# Script name: Assignment 3-3
# Author Name: Christen Reinhart
# Date of Latest Revision: 05/30/2024
# Purpose: Calculculate Date

# This Calculates Dates
# Input: Interactive Year, Month, Day
# Output: Calculate date based upon inputs

# start

# constants
MIN_YEAR = 0
MIN_MONTH = 1
MAX_MONTH = 12
MIN_DAY = 1
MAX_DAY = 31

validDate = True

# get the year, month, and day 
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
    # check month
    elif month < MIN_MONTH or month > MAX_MONTH:
        validDate = False
    else:
        # check day based on month
        if month in [4, 6, 9, 11] and (day < MIN_DAY or day > 30):  
            validDate = False
        elif month == 2 and (day < MIN_DAY or day > 28):  
            validDate = False
        elif day < MIN_DAY or day > MAX_DAY:  
            validDate = False

# output 
if validDate:
    print(f"{month}/{day}/{year} is a valid date.")
else:
    print(f"{month}/{day}/{year} is an invalid date.")

# end
