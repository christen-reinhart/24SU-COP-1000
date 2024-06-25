#!/usr/bin/env python3

# Script name: Project 0-2 Pseudocode
# Author Name: Christen Reinhart
# Date of Latest Revision: 06/23/2024
# Purpose: Arrays
# Input: Truck Brands
# Output: Array

# CarFinder v0.2 Pseudocode

# Initialize the list of allowed vehicles
allowed_vehicles = ['Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan']

# Start an infinite loop to display the menu and handle user input
WHILE True DO
    # Print the menu
    PRINT "********************************"
    PRINT "AutoCountry Vehicle Finder v0.2"
    PRINT "********************************"
    PRINT "Please Enter the following number below from the following menu:"
    PRINT ""
    PRINT "1. PRINT all Authorized Vehicles"
    PRINT "2. SEARCH for Authorized Vehicle"
    PRINT "3. Exit"
    PRINT ""
    
    # Get the user's choice
    choice = INPUT "Enter your choice: "
    choice = TRIM(choice)
    
    # Handle the user's choice
    IF choice == '1' THEN
        # Print all authorized vehicles
        PRINT "\nThe AutoCountry sales manager has authorized the purchase and selling of the following vehicles:"
        FOR vehicle IN allowed_vehicles DO
            PRINT vehicle
        END FOR
        PRINT ""  # Add a newline for better readability
    
    ELSE IF choice == '2' THEN
        # Search for a specific authorized vehicle
        search_vehicle = INPUT "Please enter the full vehicle name: "
        search_vehicle = TRIM(search_vehicle)
        
        # Check if the searched vehicle is in the list of allowed vehicles
        IF search_vehicle IN allowed_vehicles THEN
            PRINT "\n" + search_vehicle + " is an authorized vehicle"
        ELSE
            PRINT "\n" + search_vehicle + " is not an authorized vehicle, if you received this in error please check the spelling and try again"
        END IF
        PRINT ""  # Add a newline for better readability
    
    ELSE IF choice == '3' THEN
        # Exit the program
        PRINT "Thank you for using the AutoCountry Vehicle Finder, good-bye!"
        BREAK  # Exit the loop
    
    ELSE
        # Handle invalid input
        PRINT "Invalid choice. Please enter 1, 2, or 3."
        PRINT ""
    END IF
END WHILE


# Pseudocode example 2

# Pseudocode

# Program Name: AutoCountry Vehicle Finder v0.2

# Data Structures
# - allowed_vehicles: Array of Vehicles (stores names of authorized vehicles)

# Main Loop
While True:
    # Display Menu
    Print "********************************"
    Print "AutoCountry Vehicle Finder v0.2"
    Print "********************************"
    Print "Please Enter the following number below from the following menu:"
    Print ""
    Print "1. PRINT all Authorized Vehicles"
    Print "2. SEARCH for Authorized Vehicle"
    Print "3. Exit"
    Print ""

    # Get user choice
    choice = Input "Enter your choice: "
    choice = Trim(choice)

    # If choice is "1":
    If choice == '1':
        # Print authorized vehicles
        Print "\nThe AutoCountry sales manager has authorized the purchase and selling of the following vehicles:"
        For each vehicle in allowed_vehicles:
            Print vehicle
        Print ""  # Add a newline for better readability
    
    # Else if choice is "2":
    Else if choice == '2':
        # Search for a specific vehicle
        search_vehicle = Input "Please enter the full vehicle name: "
        search_vehicle = Trim(search_vehicle)
        
        # Check if the searched vehicle is in the list
        If search_vehicle in allowed_vehicles:
            Print "\n" + search_vehicle + " is an authorized vehicle"
        Else:
            Print "\n" + search_vehicle + " is not an authorized vehicle, if you received this in error please check the spelling and try again"
        Print ""  # Add a newline for better readability
    
    # Else if choice is "3":
    Else if choice == '3':
        # Exit the program
        Print "Thank you for using the AutoCountry Vehicle Finder, good-bye!"
        Break  # Exit the loop
    
    # Else (invalid choice):
    Else:
        Print "Invalid choice. Please enter 1, 2, or 3."
        Print ""
