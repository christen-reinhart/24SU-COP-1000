#!/usr/bin/env python3
# Script name: Project 0-4 
# Author Name: Christen Reinhart
# Date of Latest Revision: 07/04/2024
# Purpose: Vehicle Finder

# Input: Array with Trucks for car Finder
# Output: Options

# start
# CarFinder v0.4

# List of allowed vehicles
allowed_vehicles = [
    'Ford F-150', 
    'Chevrolet Silverado', 
    'Tesla CyberTruck', 
    'Toyota Tundra', 
    'Nissan Titan', 
    'Rivian R1T', 
    'Ram 1500'
]

# While true print banner below
while True:
    # Display menu
    print("""
********************************
AutoCountry Vehicle Finder v0.4
********************************
Please enter the following number below from the following menu:

1. PRINT all Authorized Vehicles
2. SEARCH for Authorized Vehicle
3. ADD Authorized Vehicle
4. DELETE Authorized Vehicle
5. Exit
""")
    
    # user choice
    choice = input("Enter your choice: ").strip()
    
    if choice == '1':
        # authorized vehicles
        print("\nThe AutoCountry sales manager has authorized the purchase and selling of the following vehicles:")
        for vehicle in allowed_vehicles:
            print(vehicle)
        print()  
    
    elif choice == '2':
        # Search authorized vehicle
        search_vehicle = input("Please enter the full vehicle name: ").strip()
        if search_vehicle in allowed_vehicles:
            print(f"\n{search_vehicle} is an authorized vehicle.")
        else:
            print(f"\n{search_vehicle} is not an authorized vehicle. If you received this in error, please check the spelling and try again.")
        print()  

    elif choice == '3':
        # Add authorized vehicle
        new_vehicle = input("Please enter the full vehicle name you would like to add: ").strip()
        if new_vehicle not in allowed_vehicles:
            allowed_vehicles.append(new_vehicle)
            print(f'\nYou have added "{new_vehicle}" as an authorized vehicle.')
        else:
            print(f'\n"{new_vehicle}" is already an authorized vehicle.')
        print()  
    
    elif choice == '4':
        # Delete vehicle
        remove_vehicle = input("Please enter the full vehicle name you would like to REMOVE: ").strip()
        if remove_vehicle in allowed_vehicles:
            confirm = input(f'Are you sure you want to remove "{remove_vehicle}" from the Authorized Vehicles List? (yes/no): ').strip().lower()
            if confirm == 'yes':
                allowed_vehicles.remove(remove_vehicle)
                print(f'\nYou have REMOVED "{remove_vehicle}" as an authorized vehicle.')
            else:
                print(f'\n"{remove_vehicle}" was not removed.')
        else:
            print(f'\n"{remove_vehicle}" is not an authorized vehicle.')
        print()

    elif choice == '5':
        # exit program
        print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")
        break
    
    else:
        # handle invalid input
        print("Invalid choice. Please enter 1, 2, 3, 4, or 5.\n")
        
# end
