#!/usr/bin/env python3

# Script name: Assignment 2-1
# Author Name: Christen Reinhart
# Date of Latest Revision: 05/23/2024
# Purpose: Assignment 2-3 Arithmetic with Python

# This Calculates prices and discounts
# Input:  Prices and numeric values
# Output: This program calculates profits and sales prices for a furniture company.

#Begin


#items and prices
itemName = "TV Stand"
retailPrice = 325.00
wholesalePrice = 200.00

# Calculate profit
profit = retailPrice - wholesalePrice

# Calculate sale price (10% discount)
salePrice = retailPrice * 0.90  # 10% discount 90% of the retail price

# Calculate sale profit
saleProfit = salePrice - wholesalePrice

# Print the results
print("Item Name: " + itemName)
print("Retail Price: $" + str(retailPrice))
print("Wholesale Price: $" + str(wholesalePrice))
print("Profit: $" + str(profit))
print("Sale Price: $" + str(salePrice))
print("Sale Profit: $" + str(saleProfit))

#End

