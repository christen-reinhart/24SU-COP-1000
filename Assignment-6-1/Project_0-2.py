#!/usr/bin/env python3

# Script name: Project 0-2 
# Author Name: Christen Reinhart
# Date of Latest Revision: 06/24/2024
# Purpose: Vehicle Finder

# Input: Array with Trucks for car Finder
# Output: Options

# start

# CarFinder v0.2

# List of allowed vehicles
allowed_vehicles = ['Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan']

while True:
    print("""
********************************
AutoCountry Vehicle Finder v0.2
********************************
Please Enter the following number below from the following menu:

1. PRINT all Authorized Vehicles
2. SEARCH for Authorized Vehicle
3. Exit
""")
    
    choice = input("Enter your choice: ").strip()
    
    if choice == '1':
        print("\nThe AutoCountry sales manager has authorized the purchase and selling of the following vehicles:")
        for vehicle in allowed_vehicles:
            print(vehicle)
        print()  # Add a newline for better readability
    elif choice == '2':
        search_vehicle = input("Please enter the full vehicle name: ").strip()
        if search_vehicle in allowed_vehicles:
            print(f"\n{search_vehicle} is an authorized vehicle")
        else:
            print(f"\n{search_vehicle} is not an authorized vehicle, if you received this in error please check the spelling and try again")
        print()  # Add a newline for better readability
    elif choice == '3':
        print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.\n")



