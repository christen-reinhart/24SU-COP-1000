#!/usr/bin/env python3

# Script name: Assignment 4-2
# Author Name: Christen Reinhart
# Date of Latest Revision: 06/04/2024
# Purpose: Calculculate Bonus

# This Calculates Bonus
# Input: Productivity Bonus Numbers
# Output: Calculate Bonus

# start

# Input data
employee_name = input("Enter the employee's name: ")
num_shifts = int(input("Enter the number of shifts: "))
num_transactions = int(input("Enter the number of transactions: "))
transaction_value = float(input("Enter the transaction dollar value: "))

# Calculate productivity score
productivity_score = (transaction_value / num_transactions) / num_shifts

# Determine the bonus using nested if statements
if productivity_score <= 30:
    bonus = 50.00
else:
    if 31 <= productivity_score <= 69:
        bonus = 75.00
    else:
        if 70 <= productivity_score <= 199:
            bonus = 100.00
        else:
            if productivity_score >= 200:
                bonus = 200.00

# Output the employee's name and bonus
print(f"Employee Name: {employee_name}")
print(f"Employee Bonus: ${bonus}")
                
# end
