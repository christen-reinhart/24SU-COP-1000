#!/usr/bin/env python3

# Script name: Project Test
# Author Name: Christen Reinhart
# Date of Latest Revision: 06/21/2024
# Purpose: Arrays
# Reference Chat GPT: https://chatgpt.com/share/6e22c821-64b7-4926-83c7-f5743cb5a143
# Initial Draft With Assistance

# Input: 
# Output: Array

# carfinder.py

# List of allowed vehicles (consider storing in a file for easier updates)
AllowedVehiclesList = ['Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan']


def print_menu():
  """Prints the user menu with options."""
  print("********************************")
  print("AutoCountry Vehicle Finder v0.1")
  print("********************************")
  print("Please Enter the following number below from the following menu:\n")
  print("1. PRINT all Authorized Vehicles")
  print("2. Exit")


def print_allowed_vehicles():
  """Prints a message and the list of authorized vehicles."""
  print("\nThe AutoCountry sales manager has authorized the purchase and selling of the following vehicles:")
  for vehicle in AllowedVehiclesList:
    print(vehicle)
  print()  # Add a newline for better readability


def main():
  """Main function that runs the program in a loop."""
  while True:
    print_menu()
    try:
      choice = input("Enter your choice (1 or 2): ").strip().upper()  # Handle both uppercase and lowercase input
      if choice == '1':
        print_allowed_vehicles()
      elif choice == '2':
        print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")
        break
      else:
        print("Invalid choice. Please enter 1 or 2.\n")
    except ValueError:  # Handle non-numeric input errors
      print("Invalid input. Please enter a number (1 or 2).\n")


if __name__ == "__main__":
  main()
