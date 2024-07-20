# !/usr/bin/env python3

# Script name: Project 0-5 Pseudocode
# Author Name: Christen Reinhart
# Date of Latest Revision: 07/04/2024
# Purpose: Arrays
# Input: Truck Brands
# Output: Array

# CarFinder v0.5 Pseudocode

# Program Name: AutoCountry Vehicle Finder

# start

# DEFINE file_name AS 'allowed_vehicles.txt'

# FUNCTION load_vehicles(file_name)
# if file_name does not exist then
# return [
# 'Ford F-150', 
# 'Chevrolet Silverado', 
# 'Tesla CyberTruck', 
# 'Toyota Tundra', 
# 'Nissan Titan', 
# 'Rivian R1T', 
# 'Ram 1500'
# ]
# end if
# open file_name for reading
# read all lines from file_name into list vehicles
# strip newline characters from each line in vehicles
# return vehicles
# end function

# FUNCTION save_vehicles(file_name, vehicles)
# open file_name for writing
# for each vehicle in vehicles do
# write vehicle to file_name with newline
# end for
# end function

# set allowed_vehicles to load_vehicles(file_name)

# while true do
# print """
# ********************************
# AutoCountry Vehicle Finder v0.4
# ********************************
# Please enter the following number below from the following menu:

# 1. print all Authorized Vehicles
# 2. SEARCH for Authorized Vehicle
# 3. add Authorized Vehicle
# 4. delete Authorized Vehicle
# 5. Exit
# """

# set choice to input("Enter your choice: ").strip()

# if choice is '1' then
# print "\nThe AutoCountry sales manager has authorized the purchase and selling of the following vehicles:"
# for each vehicle in allowed_vehicles do
# print vehicle
# end for
# print newline
    
# else if choice is '2' then
# set search_vehicle to input("Please enter the full vehicle name: ").strip()
# if search_vehicle in allowed_vehicles then
# print f"\n{search_vehicle} is an authorized vehicle."
# else
# print f"\n{search_vehicle} is not an authorized vehicle. If you received this in error, please check the spelling and try again."
# end if
# print newline

# else if choice is '3' then
# set new_vehicle to input("Please enter the full vehicle name you would like to add: ").strip()
# if new_vehicle not in allowed_vehicles then
# add new_vehicle to allowed_vehicles
# call save_vehicles(file_name, allowed_vehicles)
# print f'\nYou have added "{new_vehicle}" as an authorized vehicle.'
# else
# print f'\n"{new_vehicle}" is already an authorized vehicle.'
# end if
# print newline
    
# else if choice is '4' then
# set remove_vehicle to input("Please enter the full vehicle name you would like to remove: ").strip()
# if remove_vehicle in allowed_vehicles then
# set confirm to input(f'Are you sure you want to remove "{remove_vehicle}" from the Authorized Vehicles List? (yes/no): ').strip().lower()
# if confirm is 'yes' then
# remove remove_vehicle from allowed_vehicles
# call save_vehicles(file_name, allowed_vehicles)
# print f'\nYou have removed "{remove_vehicle}" as an authorized vehicle.'
# else
# print f'\n"{remove_vehicle}" was not removed.'
# end if
# else
# print f'\n"{remove_vehicle}" is not an authorized vehicle.'
# end if
# print newline
    
# else if choice is '5' then
# print "Thank you for using the AutoCountry Vehicle Finder, good-bye!"
# break

# else
# print "Invalid choice. Please enter 1, 2, 3, 4, or 5.\n"
# end if
# end while

# end

