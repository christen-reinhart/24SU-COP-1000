# !/usr/bin/env python3

# Script name: Project 0-5 Pseudocode
# Author Name: Christen Reinhart
# Date of Latest Revision: 07/20/2024
# Purpose: Arrays
# Input: Truck Brands
# Output: Print list of vehicles to a file
# Note: "Test Passed"
# CarFinder v0.5 Pseudocode

# Program Name: AutoCountry Vehicle Finder

# start

# Define the file name
# file_name = 'allowed_vehicles.txt'

# Load vehicles from the file or use default list
# try to open file_name for reading
# if file not found or empty then
# set vehicles to default list [
# 'Ford F-150', 
# 'Chevrolet Silverado', 
# 'Tesla CyberTruck', 
# 'Toyota Tundra', 
# 'Nissan Titan', 
# 'Rivian R1T', 
# 'Ram 1500'
# ]
# else
# read vehicles from file
# end if

# Save vehicles to the file
# open file_name for writing
# write each vehicle to file

# Load initial list of allowed vehicles
# allowed_vehicles = call load_vehicles(file_name)

# while true do
# Display menu
# print "1. print all Authorized Vehicles"
# print "2. search for Authorized Vehicle"
# print "3. add Authorized Vehicle"
# print "4. delete Authorized Vehicle"
# print "5. Exit"

# Get user choice
# choice = input choice

# if choice == '1' then
# print all authorized vehicles

# elif choice == '2' then
# search_vehicle = input vehicle name
# if search_vehicle in allowed_vehicles then
# print "authorized vehicle"
# else
# print "not an authorized vehicle"
# end if

# elif choice == '3' then
# new_vehicle = input new vehicle name
# if new_vehicle not in allowed_vehicles then
# add new_vehicle to allowed_vehicles
# save vehicles to file
# print "added new vehicle"
# else
# print "vehicle already authorized"
# end if

# elif choice == '4' then
# remove_vehicle = input vehicle name to remove
# if remove_vehicle in allowed_vehicles then
# confirm removal
# if confirmed then
# remove vehicle from allowed_vehicles
# save vehicles to file
# print "removed vehicle"
# else
# print "vehicle not removed"
# end if
# else
# print "vehicle not authorized"
# end if

# elif choice == '5' then
# print "good-bye!"
# break

# else
# print "Invalid choice"

# end while

# end
