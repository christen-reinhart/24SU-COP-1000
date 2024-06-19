#!/usr/bin/env python3

# Script name: Assignment 5
# Author Name: Christen Reinhart
# Date of Latest Revision: 06/11/2024
# Purpose: Pseudocode for Loop

# This Calculates Bonus
# Input: Productivity Bonus Numbers
# Output: Calculate Bonus

# start

    # declarations
    # string name
    # string QUIT = "ZZZ"
# output "Enter name"
# input name
# while name <> QUIT
    # output "Hello ", name
    # input name
# endwhile
# output "Goodbye"
# stop

# Initialize variables
QUIT = "ZZZ"

# Prompt user to enter a name
name = input("Enter name: ")

# Loop until the entered name is equal to QUIT
while name != QUIT:
    # Output greeting with the entered name
    print("Hello", name)
    
    # Prompt user to enter a name again
    name = input("Enter name: ")

# Output goodbye message
print("Goodbye")
