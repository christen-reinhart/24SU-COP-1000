#!/usr/bin/env python3

# Script name: Assignment 4-2
# Author Name: Christen Reinhart
# Date of Latest Revision: 06/07/2024
# Purpose: Pseudocode for Calculculating Bonus with nested if statements


# Input:

//employee_name = get_input("Enter the employee's name")
//num_shifts = get_input("Enter the number of shifts")
//num_transactions = get_input("Enter the number of transactions")
//transaction_value = get_input("Enter the transaction dollar value")

# Calculate productivity score:

//productivity_score = (transaction_value / num_transactions) / num_shifts

# Determine the bonus:

if productivity_score <= 30:
    bonus = 50.00
else if 31 <= productivity_score <= 69:
    bonus = 75.00
else if 70 <= productivity_score <= 199:
    bonus = 100.00
else if productivity_score >= 200:
    bonus = 200.00

# Output:

display_output("Employee Name: " + employee_name)
display_output("Employee Bonus: $" + bonus)
