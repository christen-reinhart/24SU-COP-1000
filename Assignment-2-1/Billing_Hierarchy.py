#!/usr/bin/env python3

# Script name: Assignment 2-1
# Author Name: Christen Reinhart
# Date of Latest Revision: 05/23/2024
# Purpose: Calculate Phone Billing in Python

#start

# Declarations: define usage and costs
minutes = 200  # Number of minutes used
minutecost = 1  # Cost per minute
textmessage = 300  # Number of text messages sent
textcost = 2  # Cost per text message
SALES_TAX_AMOUNT = 0.06  # Sales tax rate

# Calculate the subtotal
subtotal = (minutes * minutecost) + (textmessage * textcost)

# Calculate the tax amount
tax_amount = subtotal * SALES_TAX_AMOUNT

# Calculate the final total bill
total_bill = subtotal + tax_amount

# Output the total bill
print("Total phone bill:", total_bill)

#End