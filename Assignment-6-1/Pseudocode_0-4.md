# !/usr/bin/env python3

# Script name: Project 0-4 Pseudocode
# Author Name: Christen Reinhart
# Date of Latest Revision: 07/04/2024
# Purpose: Arrays
# Input: Truck Brands
# Output: Array

# CarFinder v0.4 Pseudocode

# Program Name: AutoCountry Vehicle Finder


WHILE True DO
    # Display Menu
    PRINT "********************************"
    PRINT "AutoCountry Vehicle Finder v0.4"
    PRINT "********************************"
    PRINT "Please enter the following number below from the following menu:"
    PRINT "1. PRINT all Authorized Vehicles"
    PRINT "2. SEARCH for Authorized Vehicle"
    PRINT "3. ADD Authorized Vehicle"
    PRINT "4. DELETE Authorized Vehicle"
    PRINT "5. Exit"
    
    # Get user choice
    choice = INPUT "Enter your choice: "
    
    # Process choice
    IF choice = "1" THEN
        PRINT "The AutoCountry sales manager has authorized the purchase and selling of the following vehicles:"
        FOR vehicle IN allowed_vehicles DO
            PRINT vehicle
        END FOR
        PRINT ""  
    
    ELSE IF choice = "2" THEN
        # Search for a specific authorized vehicle
        search_vehicle = INPUT "Please enter the full vehicle name: "
        IF search_vehicle IN allowed_vehicles THEN
            PRINT search_vehicle + " Is an authorized vehicle."
        ELSE
            PRINT search_vehicle + " Is not an authorized vehicle. Please check the spelling and try again."
        END IF
        PRINT ""  
    
    ELSE IF choice = "3" THEN
        # Add a new authorized vehicle
        new_vehicle = INPUT "Please enter the full vehicle name you would like to add: "
        IF new_vehicle NOT IN allowed_vehicles THEN
            ADD new_vehicle TO allowed_vehicles
            PRINT 'You have added "' + new_vehicle + '" as an authorized vehicle.'
        ELSE
            PRINT '"' + new_vehicle + '" is already an authorized vehicle.'
        END IF
        PRINT ""  
    
    ELSE IF choice = "4" THEN
        # Delete an authorized vehicle
        remove_vehicle = INPUT "Please enter the full vehicle name you would like to REMOVE: "
        IF remove_vehicle IN allowed_vehicles THEN
            confirm = INPUT 'Are you sure you want to remove "' + remove_vehicle + '" from the Authorized Vehicles List? (yes/no): '
            IF confirm = "yes" THEN
                REMOVE remove_vehicle FROM allowed_vehicles
                PRINT 'You have REMOVED "' + remove_vehicle + '" as an authorized vehicle.'
            ELSE
                PRINT '"' + remove_vehicle + '" was not removed.'
            END IF
        ELSE
            PRINT '"' + remove_vehicle + '" Is not an authorized vehicle.'
        END IF
        PRINT ""  

    ELSE IF choice = "5" THEN
        # Exit the program
        PRINT "Thank you for using the AutoCountry Vehicle Finder, good-bye!"
        BREAK  # Exit the loop
    
    ELSE
        # Handle invalid input
        PRINT "Invalid choice. Please enter 1, 2, 3, 4, or 5."
        PRINT ""  
    END IF
END WHILE
