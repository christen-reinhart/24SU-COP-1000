#!/usr/bin/env python3

# Script name: Assignment 4-1
# Author Name: Christen Reinhart
# Date of Latest Revision: 07/20/2024
# Purpose: Calculculate Sign Cost

# start

# Prompting user for input
numChars = int(input("Enter the number of characters: "))
woodType = input("Enter the type of wood (oak or pine): ").strip().lower()
color = input("Enter the color of characters (black, white, or gold): ").strip().lower()

# base charge
charge = 35.00

# additional characters if more than 5
if numChars > 5:
    charge += (numChars - 5) * 4

# type of wood
if woodType == "oak":
    charge += 20.00

# color of characters
if color == "gold":
    charge += 15.00

# Output the charge for this sign
print(f"The charge for this sign is ${charge:.2f}")

# end



