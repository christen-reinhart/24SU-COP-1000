#!/usr/bin/env python3

# Script name: Assignment Pseudocode d
# Author Name: Christen Reinhart
# Date of Latest Revision: 06/11/2024
# Purpose: Loop

# Performs Loop
# Input: 2, 5, 9
# Output: j, k, n

# start

# Constants
j = 2
k = 5
n = 9

# Variable initialization
m = 6

# Outer loop until j is greater than k
while j <= k:
    # Reset m to 6 at the beginning of each outer loop iteration
    m = 6
    # Inner loop until m is no longer less than n
    while m < n:
        print("Goodbye")  # Print "Goodbye"
        m = m + 1  # Increment m by 1
    # Increment j by 1 at the end of each outer loop iteration
    j = j + 1

# end


