#!/usr/bin/env python3

# Script name: Assignment Pseudocode d
# Author Name: Christen Reinhart
# Date of Latest Revision: 06/11/2024
# Purpose: Loop

# Performs Loop
# Input: 2, 5, 6, 9
# Output: j, k, m, n

# start

# Constants
j = 2
k = 5
m = 6
n = 9

# Outer loop until j is greater than k
while j <= k:
    # Inner loop until m is no longer less than n
    while m < n:
        print("Hello")  # Print "Hello"
        m = m + 1  # Increment m by 1
    # Increment j by 1 at the end of each outer loop iteration
    j = j + 1

# Print the final values of j, k, m, and n
print(j, k, m, n)

# end

# Pseudo Code Below

# start

# j = 2
# k = 5
# m = 6
# n = 9
# while j < k
    # while m < n 
    # output "Hello"
    # m = m + 1
    # endwhile
    # j = j + 1
# endwhile

# end

# Initialize variables
# j = 2
# k = 5
# m = 6
# n = 9

# Outer loop until j is less than k
# while j < k:
    # Inner loop until m is less than n
    # while m < n:
        # Output "Hello"
        # print("Hello")
        # Increment m by 1
        # m = m + 1
    
    # Reset m to 6 for the next iteration of the outer loop
    # m = 6
    # Increment j by 1
    # j = j + 1


