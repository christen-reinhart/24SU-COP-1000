#!/usr/bin/env python3

# Script name: Assignment 3-3
# Author Name: Christen Reinhart
# Date of Latest Revision: 05/30/2024
# Purpose: Calculate Date

# This Calculates Dates
# Input: Interactive Year, Month, Day
# Output: Calculate date based upon inputs

# Summary:
# This program determines if a date entered by the user is valid.
# When completed, the user should be able to enter a year, a month, and a day. The program then determines if the date is valid.
# Valid years are those that are greater than 0, valid months include the values 1 through 12, and valid days include the values 1 through 31.

#start

# Constants

validDate = True
MIN_YEAR = 0
MIN_MONTH = 1
MAX_MONTH = 12
MIN_DAY = 1
MAX_DAY = 31

# Get input from user
year = int(input("Enter year: "))
month = int(input("Enter month: "))
day = int(input("Enter day: "))

# Check if date is valid
if year <= MIN_YEAR or month < MIN_MONTH or month > MAX_MONTH or day < MIN_DAY or day > MAX_DAY:
    validDate = False

# Output result
if validDate:
    print(f"{month}/{day}/{year} is a valid date.")
else:
    print(f"{month}/{day}/{year} is an invalid date.")
    
#end
