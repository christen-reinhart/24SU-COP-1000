#!/usr/bin/env python3

# Script name: Assignment 2-1
# Author Name: Christen Reinhart
# Date of Latest Revision: 05/23/2024
# Purpose: Calculate Phone Billing in Python

# Function to calculate the total bill
def calculate_total_bill(minutes, minutecost, textmessage, textcost, sales_tax_amount):
    
 
    subtotal = (minutes * minutecost) + (textmessage * textcost)
    tax_amount = subtotal * sales_tax_amount
    totalbill = subtotal + tax_amount
    return totalbill

# Define usage and costs
minutes = 200  # Number of minutes used
minutecost = 1  # Cost per minute
textmessage = 300  # Number of text messages sent
textcost = 2  # Cost per text message
SALES_TAX_AMOUNT = 0.06  # Sales tax rate

# Calculate the total bill
totalbill = calculate_total_bill(minutes, minutecost, textmessage, textcost, SALES_TAX_AMOUNT)

# Output the total bill
print("Total phone bill")


