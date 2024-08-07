#!/usr/bin/env python3
# Script name: Project 0-6 
# Author Name: Christen Reinhart
# Date of Latest Revision: 07/27/2024
# Purpose: Vehicle Finder
# Note: "Test Passed"

# start

# File name for vehicles
allowed_vehicles_file = 'allowed_vehicles.txt'

# Function to read the list of vehicles
def read_allowed_vehicles():
    try:
        with open(allowed_vehicles_file, 'r') as file:
            vehicles = [line.strip() for line in file]
        return vehicles
    except FileNotFoundError:
        return []

# Function to write the list of vehicles
def write_allowed_vehicles(vehicles):
    try:
        with open(allowed_vehicles_file, 'w') as file:
            for vehicle in vehicles:
                file.write(vehicle + '\n')
    except IOError:
        print("Error writing to the allowed vehicles file.")

# Function to print all authorized vehicles
def print_all_vehicles():
    print("\nThe AutoCountry sales manager has authorized the purchase and selling of the following vehicles:")
    for vehicle in allowed_vehicles:
        print(vehicle)
    print()

# Function to search for an authorized vehicle
def search_vehicle():
    vehicle = get_user_input("Please enter the full vehicle name: ")
    if vehicle in allowed_vehicles:
        print(f"\n{vehicle} is an authorized vehicle.")
    else:
        print(f"\n{vehicle} is not an authorized vehicle. If you received this in error, please check the spelling and try again.")
    print()

# Function to add an authorized vehicle
def add_vehicle():
    new_vehicle = get_user_input("Please enter the full vehicle name you would like to add: ")
    if new_vehicle not in allowed_vehicles:
        allowed_vehicles.append(new_vehicle)
        write_allowed_vehicles(allowed_vehicles)
        print(f'\nYou have added "{new_vehicle}" as an authorized vehicle.')
    else:
        print(f'\n"{new_vehicle}" is already an authorized vehicle.')
    print()

# Function to delete an authorized vehicle
def delete_vehicle():
    remove_vehicle = get_user_input("Please enter the full vehicle name you would like to REMOVE: ")
    if remove_vehicle in allowed_vehicles:
        confirm = get_user_input(f'Are you sure you want to remove "{remove_vehicle}" from the Authorized Vehicles List? (yes/no): ').lower()
        if confirm == 'yes':
            allowed_vehicles.remove(remove_vehicle)
            write_allowed_vehicles(allowed_vehicles)
            print(f'\nYou have REMOVED "{remove_vehicle}" as an authorized vehicle.')
        else:
            print(f'\n"{remove_vehicle}" was not removed.')
    else:
        print(f'\n"{remove_vehicle}" is not an authorized vehicle.')
    print()

# Function to get user input with trimming
def get_user_input(prompt):
    return input(prompt).strip()

# Load the list of vehicles from the file
allowed_vehicles = read_allowed_vehicles()

# If the file is empty, initialize it with the default list
if not allowed_vehicles:
    allowed_vehicles = [
        'Ford F-150', 
        'Chevrolet Silverado', 
        'Tesla CyberTruck', 
        'Toyota Tundra', 
        'Rivian R1T', 
        'Ram 1500'
    ]
    write_allowed_vehicles(allowed_vehicles)

# Main loop to display the menu
while True:
    print("""
********************************
AutoCountry Vehicle Finder v0.6
********************************
Please enter the following number below from the following menu:

1. PRINT all Authorized Vehicles
2. SEARCH for Authorized Vehicle
3. ADD Authorized Vehicle
4. DELETE Authorized Vehicle
5. Exit
""")
    
    choice = get_user_input("Enter your choice: ")
    
    if choice == '1':
        print_all_vehicles()
    elif choice == '2':
        search_vehicle()
    elif choice == '3':
        add_vehicle()
    elif choice == '4':
        delete_vehicle()
    elif choice == '5':
        print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")
        break
    else:
        print("Invalid choice. Please enter 1, 2, 3, 4, or 5.\n")

# end
