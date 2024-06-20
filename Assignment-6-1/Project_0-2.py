#!/usr/bin/env python3

# Script name: Project 0-2
# Author Name: Christen Reinhart
# Date of Latest Revision: 06/21/2024
# Purpose: Arrays

# Input: Array with Trucks for car Finder
# Output: Options

# start

# Script name: Project 0-1 (consider renaming for clarity)
# Author Name: Christen Reinhart
# Date of Latest Revision: 06/20/2024
# Purpose: Vehicle Finder

# List of authorized vehicles (consider storing in a file for easier updates)
authorized_vehicles = ['Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan']

while True:
  print("""
********************************
AutoCountry Vehicle Finder v0.1
********************************
Please Enter a choice:
1. PRINT all Authorized Vehicles
2. Exit
""")

  choice = input("Enter your choice (1 or 2): ").strip().upper()  # Handle both uppercase and lowercase input

  if choice == '1':
    print("\nThe AutoCountry sales manager has authorized the purchase and selling of the following vehicles:")
    for vehicle in authorized_vehicles:
      print(vehicle)
    print()  # Add a newline for better readability

  elif choice == '2':
    print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")
    break

  else:
    print("Invalid choice. Please enter 1 or 2.\n")
