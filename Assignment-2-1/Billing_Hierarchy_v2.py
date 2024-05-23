#!/usr/bin/env python3

# Script name: Assignment 2-1
# Author Name: Christen Reinhart
# Date of Latest Revision: 05/23/2024
# Purpose: Calculate Phone Billing in Python

# Function to calculate the total bill
def calculate_total_bill(minutes, minutecost, textmessage, textcost, tax):
    """
    Calculate the total bill based on minutes and text messages used.

    :param minutes: Number of minutes used
    :param minutecost: Cost per minute
    :param textmessage: Number of text messages sent
    :param textcost: Cost per text message
    :param tax: Additional fixed tax amount
    :return: Total bill amount
    """
    totalbill = (minutes * minutecost) + (textmessage * textcost) + tax
    return totalbill

# Define usage and costs
minutes = 200  # Number of minutes used
minutecost = 1  # Cost per minute
textmessage = 300  # Number of text messages sent
textcost = 2  # Cost per text message
tax = 2  # Fixed tax amount

# Calculate the total bill
totalbill = calculate_total_bill(minutes, minutecost, textmessage, textcost, tax)

# Output the total bill
print(f"Total phone bill: ${totalbill:.2f}")

