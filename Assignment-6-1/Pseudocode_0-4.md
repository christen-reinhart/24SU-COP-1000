# !/usr/bin/env python3

# Script name: Project 0-4 Pseudocode
# Author Name: Christen Reinhart
# Date of Latest Revision: 07/04/2024
# Purpose: Arrays
# Input: Truck Brands
# Output: Array

# CarFinder v0.4 Pseudocode

# Program Name: AutoCountry Vehicle Finder

# start

# while true do
# Display Menu
# print "********************************"
# print "AutoCountry Vehicle Finder v0.4"
# print "********************************"
# print "Please enter the following number below from the following menu:"
# print "1. print all Authorized Vehicles"
# print "2. search for Authorized Vehicle"
# print "3. add Authorized Vehicle"
# print "4. delete Authorized Vehicle"
# print "5. Exit"
    
# Get user choice
# choice = input "Enter your choice: "
    
# Process choice
# if choice = "1" then
# print "The AutoCountry sales manager has authorized the purchase and selling of the following vehicles:"
# for vehicle in allowed_vehicles do
# print vehicle
# end for
# print ""  
    
# else if choice = "2" then
# Search for a specific authorized vehicle
# search_vehicle = input "Please enter the full vehicle name: "
# if search_vehicle in allowed_vehicles then
# print search_vehicle + " is an authorized vehicle."
# else
# print search_vehicle + " is not an authorized vehicle. Please check the spelling and try again."
# end if
# print ""  
    
# else if choice = "3" then
# Add a new authorized vehicle
# new_vehicle = input "Please enter the full vehicle name you would like to add: "
# if new_vehicle not in allowed_vehicles then
# add new_vehicle to allowed_vehicles
# print 'You have added "' + new_vehicle + '" as an authorized vehicle.'
# else
# print '"' + new_vehicle + '" is already an authorized vehicle.'
# end if
# print ""  
    
# else if choice = "4" then
# Delete an authorized vehicle
# remove_vehicle = input "Please enter the full vehicle name you would like to remove: "
# if remove_vehicle in allowed_vehicles then
# confirm = input 'Are you sure you want to remove "' + remove_vehicle + '" from the Authorized Vehicles List? (yes/no): '
# if confirm = "yes" then
# remove remove_vehicle from allowed_vehicles
# print 'You have removed "' + remove_vehicle + '" as an authorized vehicle.'
# else
# print '"' + remove_vehicle + '" was not removed.'
# end if
# else
# print '"' + remove_vehicle + '" is not an authorized vehicle.'
# end if
# print ""  

# else if choice = "5" then
# Exit the program
# print "Thank you for using the AutoCountry Vehicle Finder, good-bye!"
# break  # Exit the loop
    
# else
# Handle invalid input
# print "Invalid choice. Please enter 1, 2, 3, 4, or 5."
# print ""  
# end if
# end while

