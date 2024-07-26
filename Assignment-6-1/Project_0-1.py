# !/usr/bin/env python3
# Script name: Project 0-1
# Author Name: Christen Reinhart
# Date of Latest Revision: 06/20/2024
# Purpose: Array
# Input: Truck Brands
# Output: Trucks for Sale
# Note: "Test Passed"
# start

# list of vehicles
allowed_vehicles = ['Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan']



# while true print banner
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

# end
        
        



