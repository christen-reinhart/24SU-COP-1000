# !/usr/bin/env python3

# Script name: Project 0-4 Pseudocode
# Author Name: Christen Reinhart
# Date of Latest Revision: 07/04/2024
# Purpose: Arrays
# Input: Truck Brands
# Output: Array

# CarFinder v0.4 Pseudocode

# Program Name: AutoCountry Vehicle Finder

START

DEFINE file_name AS 'allowed_vehicles.txt'

FUNCTION load_vehicles(file_name)
    IF file_name does not exist THEN
        RETURN [
            'Ford F-150', 
            'Chevrolet Silverado', 
            'Tesla CyberTruck', 
            'Toyota Tundra', 
            'Nissan Titan', 
            'Rivian R1T', 
            'Ram 1500'
        ]
    END IF
    OPEN file_name FOR reading
    READ all lines from file_name INTO list vehicles
    STRIP newline characters from each line in vehicles
    RETURN vehicles
END FUNCTION

FUNCTION save_vehicles(file_name, vehicles)
    OPEN file_name FOR writing
    FOR EACH vehicle IN vehicles DO
        WRITE vehicle TO file_name WITH newline
    END FOR
END FUNCTION

SET allowed_vehicles TO load_vehicles(file_name)

WHILE TRUE DO
    PRINT """
    ********************************
    AutoCountry Vehicle Finder v0.4
    ********************************
    Please enter the following number below from the following menu:

    1. PRINT all Authorized Vehicles
    2. SEARCH for Authorized Vehicle
    3. ADD Authorized Vehicle
    4. DELETE Authorized Vehicle
    5. Exit
    """

    SET choice TO input("Enter your choice: ").strip()

    IF choice IS '1' THEN
        PRINT "\nThe AutoCountry sales manager has authorized the purchase and selling of the following vehicles:"
        FOR EACH vehicle IN allowed_vehicles DO
            PRINT vehicle
        END FOR
        PRINT newline
    
    ELSE IF choice IS '2' THEN
        SET search_vehicle TO input("Please enter the full vehicle name: ").strip()
        IF search_vehicle IN allowed_vehicles THEN
            PRINT f"\n{search_vehicle} is an authorized vehicle."
        ELSE
            PRINT f"\n{search_vehicle} is not an authorized vehicle. If you received this in error, please check the spelling and try again."
        END IF
        PRINT newline
    
    ELSE IF choice IS '3' THEN
        SET new_vehicle TO input("Please enter the full vehicle name you would like to add: ").strip()
        IF new_vehicle NOT IN allowed_vehicles THEN
            ADD new_vehicle TO allowed_vehicles
            CALL save_vehicles(file_name, allowed_vehicles)
            PRINT f'\nYou have added "{new_vehicle}" as an authorized vehicle.'
        ELSE
            PRINT f'\n"{new_vehicle}" is already an authorized vehicle.'
        END IF
        PRINT newline
    
    ELSE IF choice IS '4' THEN
        SET remove_vehicle TO input("Please enter the full vehicle name you would like to REMOVE: ").strip()
        IF remove_vehicle IN allowed_vehicles THEN
            SET confirm TO input(f'Are you sure you want to remove "{remove_vehicle}" from the Authorized Vehicles List? (yes/no): ').strip().lower()
            IF confirm IS 'yes' THEN
                REMOVE remove_vehicle FROM allowed_vehicles
                CALL save_vehicles(file_name, allowed_vehicles)
                PRINT f'\nYou have REMOVED "{remove_vehicle}" as an authorized vehicle.'
            ELSE
                PRINT f'\n"{remove_vehicle}" was not removed.'
            END IF
        ELSE
            PRINT f'\n"{remove_vehicle}" is not an authorized vehicle.'
        END IF
        PRINT newline
    
    ELSE IF choice IS '5' THEN
        PRINT "Thank you for using the AutoCountry Vehicle Finder, good-bye!"
        BREAK

    ELSE
        PRINT "Invalid choice. Please enter 1, 2, 3, 4, or 5.\n"
    END IF
END WHILE

END
