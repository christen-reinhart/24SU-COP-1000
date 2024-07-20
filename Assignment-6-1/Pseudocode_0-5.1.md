# !/usr/bin/env python3

# Script name: Project 0-5 Pseudocode
# Author Name: Christen Reinhart
# Date of Latest Revision: 07/11/2024
# Purpose: Arrays
# Input: Truck Brands
# Output: Array

# CarFinder v0.5 Pseudocode

# Program Name: AutoCountry Vehicle Finder

# start

# define allowed_vehicles_file as 'allowed_vehicles.txt'

# function read_allowed_vehicles():
# if file does not exist(allowed_vehicles_file):
# return empty list
# end if

# open allowed_vehicles_file for reading
# vehicles = read all lines from file and strip newline characters
# close file

# return vehicles
# end function

# function write_allowed_vehicles(vehicles):
# open allowed_vehicles_file for writing
# for each vehicle in vehicles:
# write vehicle + newline character to file
# end for
# close file
# end function

# allowed_vehicles = call read_allowed_vehicles()

# if allowed_vehicles is empty:
# allowed_vehicles = [
# 'Ford F-150', 
# 'Chevrolet Silverado', 
# 'Tesla CyberTruck', 
# 'Toyota Tundra', 
# 'Rivian R1T', 
# 'Ram 1500'
# ]
# call write_allowed_vehicles(allowed_vehicles)
# end if

# while true:
# print """
# ********************************
# AutoCountry Vehicle Finder v0.5
# ********************************
# Please enter the following number below from the following menu:

# 1. print all Authorized Vehicles
# 2. search for Authorized Vehicle
# 3. add Authorized Vehicle
# 4. delete Authorized Vehicle
# 5. Exit
# """

# choice = get user input and strip whitespace

# if choice == '1':
# print "The AutoCountry sales manager has authorized the purchase and selling of the following vehicles:"
# for each vehicle in allowed_vehicles:
# print vehicle
# end for
# print newline

# else if choice == '2':
# search_vehicle = get user input and strip whitespace
# if search_vehicle in allowed_vehicles:
# print search_vehicle + " is an authorized vehicle."
# else:
# print search_vehicle + " is not an authorized vehicle. If you received this in error, please check the spelling and try again."
# end if
# print newline

# else if choice == '3':
# new_vehicle = get user input and strip whitespace
# if new_vehicle not in allowed_vehicles:
# add new_vehicle to allowed_vehicles
# call write_allowed_vehicles(allowed_vehicles)
# print 'You have added "' + new_vehicle + '" as an authorized vehicle.'
# else:
# print '"' + new_vehicle + '" is already an authorized vehicle.'
# end if
# print newline

# else if choice == '4':
# remove_vehicle = get user input and strip whitespace
# if remove_vehicle in allowed_vehicles:
# confirm = get user input ('yes' or 'no') and strip whitespace
# if confirm == 'yes':
# remove remove_vehicle from allowed_vehicles
# call write_allowed_vehicles(allowed_vehicles)
# print 'You have removed "' + remove_vehicle + '" as an authorized vehicle.'
# else:
# print '"' + remove_vehicle + '" was not removed.'
# end if
# else:
# print '"' + remove_vehicle + '" is not an authorized vehicle.'
# end if
# print newline

# else if choice == '5':
# print "Thank you for using the AutoCountry Vehicle Finder, good-bye!"
# break

# else:
# print "Invalid choice. Please enter 1, 2, 3, 4, or 5."
# print newline

# end while

# end

