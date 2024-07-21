#!/usr/bin/env python3

# Script name: Project 0-5 
# Author Name: Christen Reinhart
# Date of Latest Revision: 07/20/2024
# Purpose: Vehicle Finder
# Input: Truck Brands
# Output: Array

# Program Name: AutoCountry Vehicle Finder

# start

# Define the file name
file_name = 'allowed_vehicles.txt'

# Initialize the allowed vehicles list from the file
def load_vehicles(file_name):
    try:
        with open(file_name, 'r') as file:
            vehicles = [line.strip() for line in file.readlines()]
        if not vehicles:
            raise FileNotFoundError
    except FileNotFoundError:
        vehicles = [
            'Ford F-150', 
            'Chevrolet Silverado', 
            'Tesla CyberTruck', 
            'Toyota Tundra', 
            'Nissan Titan', 
            'Rivian R1T', 
            'Ram 1500'
        ]
    return vehicles

# Save the allowed vehicles list to the file
def save_vehicles(file_name, vehicles):
    with open(file_name, 'w') as file:
        for vehicle in vehicles:
            file.write(f"{vehicle}\n")

# Load the initial list of allowed vehicles
allowed_vehicles = load_vehicles(file_name)

# While true print banner below
while True:
    # Display menu
    print("""
********************************
AutoCountry Vehicle Finder v0.5
********************************
Please enter the following number below from the following menu:

1. PRINT all Authorized Vehicles
2. SEARCH for Authorized Vehicle
3. ADD Authorized Vehicle
4. DELETE Authorized Vehicle
5. Exit
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
            save_vehicles(file_name, allowed_vehicles)
            print(f'\nYou have added "{new_vehicle}" as an authorized vehicle.')
        else:
            print(f'\n"{new_vehicle}" is already an authorized vehicle.')
        print()  
    
    elif choice == '4':
        # Delete an authorized vehicle
        remove_vehicle = input("Please enter the full vehicle name you would like to REMOVE: ").strip()
        if remove_vehicle in allowed_vehicles:
            confirm = input(f'Are you sure you want to remove "{remove_vehicle}" from the Authorized Vehicles List? (yes/no): ').strip().lower()
            if confirm == 'yes':
                allowed_vehicles.remove(remove_vehicle)
                save_vehicles(file_name, allowed_vehicles)
                print(f'\nYou have REMOVED "{remove_vehicle}" as an authorized vehicle.')
            else:
                print(f'\n"{remove_vehicle}" was not removed.')
        else:
            print(f'\n"{remove_vehicle}" is not an authorized vehicle.')
        print()

    elif choice == '5':
        # Exit the program
        print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")
        break
    
    else:
        # Handle invalid input
        print("Invalid choice. Please enter 1, 2, 3, 4, or 5.\n")
        
# end

