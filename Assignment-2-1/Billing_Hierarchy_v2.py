#!/usr/bin/env python3

# Script name: Assignment 2-1
# Author Name: Christen Reinhart
# Date of Latest Revision: 07/20/2024
# Purpose: Calculate Phone Billing in Python

# usage and costs
minutes = 200  # Number of minutes used
minutecost = 1  # Cost per minute
textmessage = 300  # Number of text messages sent
textcost = 2  # Cost per text message
SALES_TAX_AMOUNT = 0.06  # Sales tax rate

# total bill
subtotal = (minutes * minutecost) + (textmessage * textcost)
tax_amount = subtotal * SALES_TAX_AMOUNT
totalbill = subtotal + tax_amount

# output the total bill
print(f"Total phone bill: ${totalbill:.2f}")


