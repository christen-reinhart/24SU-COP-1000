# !/usr/bin/env python3

# Script name: Project 0-1 Pseudocode
# Author Name: Christen Reinhart
# Date of Latest Revision: 06/20/2024
# Purpose: Display/Print Vehicles
# Input: Truck Brands
# Output: Array

# Pseudocode

# Program Name: AutoCountry Vehicle Finder

# Data Structures
# - authorized_vehicles: Array of Vehicles (stores names of authorized vehicles)

# Main Loop
WHILE True DO
    # Display Menu
    PRINT "********************************"
    PRINT "AutoCountry Vehicle Finder"
    PRINT "********************************"
    PRINT "Please enter the following number below from the following menu:"
    PRINT "1. PRINT all Authorized Vehicles"
    PRINT "2. Exit"
    
    # Get user choice
    choice = INPUT "Enter your choice: "
    
    # Process choice
    IF choice = "1" THEN
        PRINT "The AutoCountry sales manager has authorized the following vehicles:"
        FOR vehicle IN authorized_vehicles DO
            PRINT vehicle
        END FOR
    ELSE IF choice = "2" THEN
        PRINT "Thank you for using the AutoCountry Vehicle Finder, good-bye!"
        EXIT  # Break the loop and end the program
    ELSE
        PRINT "Invalid choice. Please enter 1 or 2."
    END IF
    PRINT ""  # Add a newline for separation
END WHILE


