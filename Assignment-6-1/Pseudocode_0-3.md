# !/usr/bin/env python3

# Script name: Project 0-3 Pseudocode
# Author Name: Christen Reinhart
# Date of Latest Revision: 06/27/2024
# Purpose: Arrays
# Input: Truck Brands
# Output: Array
# Note: "Test Passed"
# CarFinder v0.3 Pseudocode

# Program Name: AutoCountry Vehicle Finder

# start

# Data Structures
# - allowed_vehicles: Array of Vehicles (stores names of authorized vehicles)

# Main Loop
# while true do
# Display Menu
# print "********************************"
# print "AutoCountry Vehicle Finder v0.3"
# print "********************************"
# print "Please enter the following number below from the following menu:"
# print "1. print all Authorized Vehicles"
# print "2. search for Authorized Vehicle"
# print "3. add Authorized Vehicle"
# print "4. Exit"
    
# Get user choice
# choice = input "Enter your choice: "
    
# Process choice
# if choice = "1" then
# print all authorized vehicles
# for vehicle in allowed_vehicles do
# print vehicle
# end for
# print newline
    
# else if choice = "2" then
# search_vehicle = input "Please enter the full vehicle name: "
# if search_vehicle in allowed_vehicles then
# print search_vehicle + " is an authorized vehicle."
# else
# print search_vehicle + " is not an authorized vehicle. Please check the spelling and try again."
# end if
# print newline
    
# else if choice = "3" then
# new_vehicle = input "Please enter the full vehicle name you would like to add: "
# if new_vehicle not in allowed_vehicles then
# add new_vehicle to allowed_vehicles
# print 'You have added "' + new_vehicle + '" as an authorized vehicle.'
# else
# print '"' + new_vehicle + '" is already an authorized vehicle.'
# end if
# print newline
    
# else if choice = "4" then
# print "Thank you for using the AutoCountry Vehicle Finder, good-bye!"
# break  # Exit the loop
    
# else
# print "Invalid choice. Please enter 1, 2, 3, or 4."
# print newline
# end if
# end while

# end


