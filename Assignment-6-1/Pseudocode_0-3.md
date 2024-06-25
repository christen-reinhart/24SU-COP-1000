# !/usr/bin/env python3

# Script name: Project 0-3 Pseudocode
# Author Name: Christen Reinhart
# Date of Latest Revision: 06/27/2024
# Purpose: Arrays
# Input: Truck Brands
# Output: Array

# CarFinder v0.3 Pseudocode

# Program Name: AutoCountry Vehicle Finder

# Data Structures
# - allowed_vehicles: Array of Vehicles (stores names of authorized vehicles)

# Main Loop
WHILE True DO
    # Display Menu
    PRINT "********************************"
    PRINT "AutoCountry Vehicle Finder v0.3"
    PRINT "********************************"
    PRINT "Please enter the following number below from the following menu:"
    PRINT "1. PRINT all Authorized Vehicles"
    PRINT "2. SEARCH for Authorized Vehicle"
    PRINT "3. ADD Authorized Vehicle"
    PRINT "4. Exit"
    
    # Get user choice
    choice = INPUT "Enter your choice: "
    
    # Process choice
    IF choice = "1" THEN
        PRINT "The AutoCountry sales manager has authorized the purchase and selling of the following vehicles:"
        FOR vehicle IN allowed_vehicles DO
            PRINT vehicle
        END FOR
        PRINT ""  # Add a newline for better readability
    
    ELSE IF choice = "2" THEN
        # Search for a specific authorized vehicle
        search_vehicle = INPUT "Please enter the full vehicle name: "
        IF search_vehicle IN allowed_vehicles THEN
            PRINT search_vehicle + " is an authorized vehicle."
        ELSE
            PRINT search_vehicle + " is not an authorized vehicle. Please check the spelling and try again."
        END IF
        PRINT ""  # Add a newline for better readability
    
    ELSE IF choice = "3" THEN
        # Add a new authorized vehicle
        new_vehicle = INPUT "Please enter the full vehicle name you would like to add: "
        IF new_vehicle NOT IN allowed_vehicles THEN
            ADD new_vehicle TO allowed_vehicles
            PRINT 'You have added "' + new_vehicle + '" as an authorized vehicle.'
        ELSE
            PRINT '"' + new_vehicle + '" is already an authorized vehicle.'
        END IF
        PRINT ""  # Add a newline for better readability
    
    ELSE IF choice = "4" THEN
        # Exit the program
        PRINT "Thank you for using the AutoCountry Vehicle Finder, good-bye!"
        BREAK  # Exit the loop
    
    ELSE
        # Handle invalid input
        PRINT "Invalid choice. Please enter 1, 2, 3, or 4."
        PRINT ""  # Add a newline for separation
    END IF
END WHILE
