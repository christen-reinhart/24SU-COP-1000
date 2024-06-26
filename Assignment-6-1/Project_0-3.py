# !/usr/bin/env python3

# Script name: Project 0-3 
# Author Name: Christen Reinhart
# Date of Latest Revision: 06/28/2024
# Purpose: Vehicle Finder

# Input: Array with Trucks for car Finder
# Output: Options

# start
# CarFinder v0.3

# List of allowed vehicles
allowed_vehicles = ['Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan']

# While true print banner below
while True:
    # Display menu
    print("""
********************************
AutoCountry Vehicle Finder v0.3
********************************
Please enter the following number below from the following menu:

1. PRINT all Authorized Vehicles
2. SEARCH for Authorized Vehicle
3. ADD Authorized Vehicle
4. Exit
""")
    
    # Get user choice
    choice = input("Enter your choice: ").strip()
    
    if choice == '1':
        # Print all authorized vehicles
        print("\nThe AutoCountry sales manager has authorized the purchase and selling of the following vehicles:")
        for vehicle in allowed_vehicles:
            print(vehicle)
        print()  
    
    elif choice == '2':
        # Search for a specific authorized vehicle
        search_vehicle = input("Please enter the full vehicle name: ").strip()
        if search_vehicle in allowed_vehicles:
            print(f"\n{search_vehicle} is an authorized vehicle.")
        else:
            print(f"\n{search_vehicle} is not an authorized vehicle. If you received this in error, please check the spelling and try again.")
        print()  

    elif choice == '3':
        # Add a new authorized vehicle
        new_vehicle = input("Please enter the full vehicle name you would like to add: ").strip()
        if new_vehicle not in allowed_vehicles:
            allowed_vehicles.append(new_vehicle)
            print(f'\nYou have added "{new_vehicle}" as an authorized vehicle.')
        else:
            print(f'\n"{new_vehicle}" is already an authorized vehicle.')
        print()  
    
    elif choice == '4':
        # Exit the program
        print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")
        break
    
    else:
        # Handle invalid input
        print("Invalid choice. Please enter 1, 2, 3, or 4.\n")
        
# end
