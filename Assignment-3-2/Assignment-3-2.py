# !/usr/bin/env python3
# Script name: Assignment 3-2
# Author Name: Christen Reinhart
# Date of Latest Revision: 07/20/2024
# Purpose: Calculate accept or reject

# start 

# input data for test score and rank
testScore = int(input("Enter the test score: "))
classRank = int(input("Enter the class rank: "))

# admission score print Accept or Reject
if testScore >= 90:
    if classRank >= 25:
        print("Accept")
    else:
        print("Reject")
else:
    if testScore >= 80:
        if classRank >= 50:
            print("Accept")
        else:
            print("Reject")
    else:
        if testScore >= 70:
            if classRank >= 75:
                print("Accept")
            else:
                print("Reject")
        else:
            print("Reject")
            
# end
