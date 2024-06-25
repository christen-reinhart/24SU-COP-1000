# !/usr/bin/env python3

# Script name: Project 0-2 Pseudocode
# Author Name: Christen Reinhart
# Date of Latest Revision: 06/25/2024
# Purpose: Arrays
# Input: Truck Brands
# Output: Array

# CarFinder v0.2 Pseudocode

# Program Name: AutoCountry Vehicle Finder

# Data Structures
# - allowed_vehicles: Array of Vehicles (stores names of authorized vehicles)

# Main Loop
WHILE True DO
    # Display Menu
    PRINT "********************************"
    PRINT "AutoCountry Vehicle Finder v0.2"
    PRINT "********************************"
    PRINT "Please enter the following number below from the following menu:"
    PRINT "1. PRINT all Authorized Vehicles"
    PRINT "2. SEARCH for Authorized Vehicle"
    PRINT "3. Exit"
    
    # Get user choice
    choice = INPUT "Enter your choice: "
    
    # Process choice
    IF choice = "1" THEN
        PRINT "The AutoCountry sales manager has authorized the purchase and selling of the following vehicles:"
        FOR vehicle IN allowed_vehicles DO
            PRINT vehicle
        END FOR
    ELSE IF choice = "2" THEN
        search_vehicle = INPUT "Please enter the full vehicle name: "
        IF search_vehicle IN allowed_vehicles THEN
            PRINT search_vehicle + " is an authorized vehicle."
        ELSE
            PRINT search_vehicle + " is not an authorized vehicle. Please check the spelling and try again."
        END IF
    ELSE IF choice = "3" THEN
        PRINT "Thank you for using the AutoCountry Vehicle Finder, good-bye!"
        EXIT  # Break the loop and end the program
    ELSE
        PRINT "Invalid choice. Please enter 1, 2, or 3."
    END IF
    PRINT ""  # Add a newline for separation
END WHILE



