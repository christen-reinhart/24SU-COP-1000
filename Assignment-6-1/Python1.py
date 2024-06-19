#!/usr/bin/env python3

# Script name: Assignment 6
# Author Name: Christen Reinhart
# Date of Latest Revision: 06/19/2024
# Purpose: Arrays

# This 
# Input: Pending
# Output: Pending

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

