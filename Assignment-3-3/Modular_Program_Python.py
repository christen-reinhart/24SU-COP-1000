#!/usr/bin/env python3

# Script name: Assignment 3-
# Author Name: Christen Reinhart
# Date of Latest Revision: 05/30/2024
# Purpose: Calculculate Year

# This Calculates Dates
# Input: Year, Month, Day
# Output: Calculate the proper year based upon inputs

Start

# Summary:
# In this lab, you add the input and output statements to a partially completed Python program.
# When completed, the user should be able to enter a year, a month, and a day. The program then determines if the date is valid.
# Valid years are those that are greater than 0, valid months include the values 1 through 12, and valid days include the values 1 through 31.

# Constants
MIN_YEAR = 1
MIN_MONTH = 1
MAX_MONTH = 12
MIN_DAY = 1
MAX_DAY = 31

# Main function to check if a date is valid
def main():
    validDate = True

    # Get the year, month, and day from the user
    try:
        year = int(input("Enter year: "))
        month = int(input("Enter month (1-12): "))
        day = int(input("Enter day: "))
    except ValueError:
        print("Invalid input. Please enter numeric values for year, month, and day.")
        return

    # Check year
    if year < MIN_YEAR:
        validDate = False
    # Check month
    elif month < MIN_MONTH or month > MAX_MONTH:
        validDate = False
    else:
        # Check day based on month
        if month in [4, 6, 9, 11] and (day < MIN_DAY or day > 30):  # April, June, September, November have 30 days
            validDate = False
        elif month == 2 and (day < MIN_DAY or day > 28):  # February has 28 days (ignoring leap years)
            validDate = False
        elif day < MIN_DAY or day > MAX_DAY:  # All other months
            validDate = False

    # Output the result
    if validDate:
        print(f"{month}/{day}/{year} is a valid date.")
    else:
        print(f"{month}/{day}/{year} is an invalid date.")

# Run the main function
if __name__ == "__main__":
    main()
