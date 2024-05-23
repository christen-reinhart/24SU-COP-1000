#!/usr/bin/env python3

# Script name: Assignment 2-4
# Author Name: Christen Reinhart
# Date of Latest Revision: 05/23/2024
# Purpose: Arithmetic with Python

# This Calculates paycheck
# Input:  paycheck amounts and percentages
# Output: Calculate pay amounts

#Begin

# Initialize variables with input from the user
salary = float(input("Enter the weekly salary: "))
numDependents = int(input("Enter the number of dependents: "))

# Calculate state tax witholding at 6.5%
stateTax = salary * 0.065

# Calculate federal tax witholding at 28.0%
federalTax = salary * 0.28

# Calculate dependent deductions at 2.5% of the salary for each dependent
dependentDeduction = salary * 0.025 * numDependents

# Calculate total withholding as stateTax + federalTax + dependentDeduction
totalWithholding = stateTax + federalTax + dependentDeduction

# Calculate take-home pay as salary - totalWithholding
takeHomePay = salary - totalWithholding

# Output statements
print("State Tax: $" + str(stateTax))
print("Federal Tax: $" + str(federalTax))
print("Dependent Deductions: $" + str(dependentDeduction))
print("Salary: $" + str(salary))
print("Take Home Pay: $" + str(takeHomePay))

#End