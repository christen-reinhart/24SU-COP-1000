#!/usr/bin/env python3

# Script name: Project 0-1
# Author Name: Christen Reinhart
# Date of Latest Revision: 06/20/2024
# Purpose: Arrays
# Reference Chat GPT: https://chatgpt.com/share/08c15ca8-32e9-4464-958f-2968157a9e3f
# Initial Draft With Assistance
# This 
# Input: Truck Brands
# Output: Array

# List of allowed vehicles
allowed_vehicles = ['Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan']

while True:
    print("""
********************************
AutoCountry Vehicle Finder v0.1
********************************
Please Enter the following number below from the following menu:

1. PRINT all Authorized Vehicles
2. Exit
""")
    
    choice = input("Enter your choice: ").strip()
    
    if choice == '1':
        print("\nThe AutoCountry sales manager has authorized the purchase of the following vehicles:")
        for vehicle in allowed_vehicles:
            print(vehicle)
        print()  
    elif choice == '2':
        print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")
        break
    else:
        print("Invalid choice. Please enter 1 or 2.\n")
        
        
# Pseudocode

# Program Name: AutoCountry Vehicle Finder

# Data Structures
# - authorized_vehicles: Array of Strings (stores names of authorized vehicles)

# Main Loop
#While True:
#  - Display Menu:
#    "********************************"
#    "********************************"
#    "Please Enter a choice:"
#    "1. PRINT all Authorized Vehicles"
#    "2. Exit"
#  - Get user choice (choice: String)
#  - Convert choice to uppercase (choice = UPPERCASE(choice))
#  - If choice is equal to "1":
#    - Print message: "The AutoCountry sales manager has authorized..."
#    - Loop through each vehicle in authorized_vehicles:
#      - Print vehicle name
#   - Print newline
#  - Else if choice is equal to "2":
#    - Print message: "Thank you for using the AutoCountry Vehicle Finder, good-bye!"
#    - Break loop (exit program)
#  - Else:
#    - Print message: "Invalid choice. Please enter 1 or 2."


