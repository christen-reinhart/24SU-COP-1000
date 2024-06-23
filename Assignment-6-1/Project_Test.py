#!/usr/bin/env python3

# Script name: Project 0-1
# Author Name: Christen Reinhart
# Date of Latest Revision: 06/23/2024
# Purpose: Array
# Input: Truck Brands
# Output: Trucks for Sale

# List of allowed vehicles
allowed_vehicles = ['Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan']

def print_banner():
    print("""
********************************
AutoCountry Vehicle Finder v0.2
********************************
Please Enter the following number below from the following menu:

1. PRINT all Authorized Vehicles
2. SEARCH for Authorized Vehicle
3. Exit
""")

def print_authorized_vehicles(vehicles):
    print("\nThe AutoCountry sales manager has authorized the purchase of the following vehicles:")
    for vehicle in vehicles:
        print(vehicle)
    print()

def search_vehicle(vehicles, search_query):
    if search_query in vehicles:
        print(f"\n{search_query} is an authorized vehicle")
    else:
        print(f"\n{search_query} is not an authorized vehicle, if you received this in error please check the spelling and try again")
    print()

def main():
    while True:
        print_banner()
        
        choice = input("Enter your choice: ").strip()
        
        if choice == '1':
            print_authorized_vehicles(allowed_vehicles)
        elif choice == '2':
            search_query = input("Please Enter the full Vehicle name: ").strip()
            search_vehicle(allowed_vehicles, search_query)
        elif choice == '3':
            print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.\n")

if __name__ == "__main__":
    main()
