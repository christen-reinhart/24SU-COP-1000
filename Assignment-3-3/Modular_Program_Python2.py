# !/usr/bin/env python3

# Script name: Assignment 3-3
# Author Name: Christen Reinhart
# Date of Latest Revision: 05/30/2024
# Purpose: Calculate Date

# This Calculates Dates
# Input: Interactive Year, Month, Day
# Output: Calculate date based upon inputs

#start

validDate = True
MIN_YEAR = 0
MIN_MONTH = 1
MAX_MONTH = 12
MIN_DAY = 1
MAX_DAY = 31

# input from user
year = int(input("Enter year: "))
month = int(input("Enter month: "))
day = int(input("Enter day: "))

# check date is valid
if year <= MIN_YEAR or month < MIN_MONTH or month > MAX_MONTH or day < MIN_DAY or day > MAX_DAY:
    validDate = False

# output 
if validDate:
    print(f"{month}/{day}/{year} is a valid date.")
else:
    print(f"{month}/{day}/{year} is an invalid date.")
    
#end
