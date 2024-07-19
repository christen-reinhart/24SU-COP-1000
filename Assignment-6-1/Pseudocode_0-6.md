# !/usr/bin/env python3

# Script name: Project 0-6 Pseudocode
# Author Name: Christen Reinhart
# Date of Latest Revision: 07/21/2024
# Purpose: Arrays
# Input: Truck Brands
# Output: Array

# CarFinder v0.6 Pseudocode

# Program Name: AutoCountry Vehicle Finder

START

DEFINE allowed_vehicles_file AS 'allowed_vehicles.txt'

FUNCTION read_allowed_vehicles():
    IF file does not exist(allowed_vehicles_file):
        RETURN empty list
    END IF

    OPEN allowed_vehicles_file FOR reading
    vehicles = READ all lines from file and strip newline characters
    CLOSE file

    RETURN vehicles
END FUNCTION

FUNCTION write_allowed_vehicles(vehicles):
    OPEN allowed_vehicles_file FOR writing
    FOR EACH vehicle IN vehicles:
        WRITE vehicle + newline character TO file
    END FOR
    CLOSE file
END FUNCTION

FUNCTION print_all_vehicles():
    PRINT "The AutoCountry sales manager has authorized the purchase and selling of the following vehicles:"
    FOR EACH vehicle IN allowed_vehicles:
        PRINT vehicle
    END FOR
    PRINT newline
END FUNCTION

FUNCTION search_vehicle():
    search_vehicle = GET user input and strip whitespace
    IF search_vehicle IN allowed_vehicles:
        PRINT search_vehicle + " is an authorized vehicle."
    ELSE:
        PRINT search_vehicle + " is not an authorized vehicle. If you received this in error, please check the spelling and try again."
    END IF
    PRINT newline
END FUNCTION

FUNCTION add_vehicle():
    new_vehicle = GET user input and strip whitespace
    IF new_vehicle NOT IN allowed_vehicles:
        ADD new_vehicle TO allowed_vehicles
        CALL write_allowed_vehicles(allowed_vehicles)
        PRINT 'You have added "' + new_vehicle + '" as an authorized vehicle.'
    ELSE:
        PRINT '"' + new_vehicle + '" is already an authorized vehicle.'
    END IF
    PRINT newline
END FUNCTION

FUNCTION delete_vehicle():
    remove_vehicle = GET user input and strip whitespace
    IF remove_vehicle IN allowed_vehicles:
        confirm = GET user input ('yes' or 'no') and strip whitespace
        IF confirm == 'yes':
            REMOVE remove_vehicle FROM allowed_vehicles
            CALL write_allowed_vehicles(allowed_vehicles)
            PRINT 'You have REMOVED "' + remove_vehicle + '" as an authorized vehicle.'
        ELSE:
            PRINT '"' + remove_vehicle + '" was not removed.'
        END IF
    ELSE:
        PRINT '"' + remove_vehicle + '" is not an authorized vehicle.'
    END IF
    PRINT newline
END FUNCTION

allowed_vehicles = CALL read_allowed_vehicles()

IF allowed_vehicles IS empty:
    allowed_vehicles = [
        'Ford F-150', 
        'Chevrolet Silverado', 
        'Tesla CyberTruck', 
        'Toyota Tundra', 
        'Rivian R1T', 
        'Ram 1500'
    ]
    CALL write_allowed_vehicles(allowed_vehicles)
END IF

WHILE True:
    PRINT("""
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

    choice = GET user input and strip whitespace

    IF choice == '1':
        CALL print_all_vehicles()
    ELSE IF choice == '2':
        CALL search_vehicle()
    ELSE IF choice == '3':
        CALL add_vehicle()
    ELSE IF choice == '4':
        CALL delete_vehicle()
    ELSE IF choice == '5':
        PRINT "Thank you for using the AutoCountry Vehicle Finder, good-bye!"
        BREAK
    ELSE:
        PRINT "Invalid choice. Please enter 1, 2, 3, 4, or 5."
        PRINT newline
END WHILE

END
