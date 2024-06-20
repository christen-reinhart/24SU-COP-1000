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
        print("\nThe AutoCountry sales manager has authorized the purchase and selling of the following vehicles:")
        for vehicle in allowed_vehicles:
            print(vehicle)
        print()  # Add a newline for better readability
    elif choice == '2':
        print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")
        break
    else:
        print("Invalid choice. Please enter 1 or 2.\n")


