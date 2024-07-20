# start

# Set the minimum amount for the year
# set MIN_YEAR to 0 

# Set the minimum amount for the month
# set MIN_MONTH to 1 

# Set the maximum amount for the month
# set MAX_MONTH to 12 

# Set the minimum amount for the day
# set MIN_DAY to 1 

# Set the maximum amount for the day
# set MAX_DAY to 31 

# Set Valid Date to True
# set validDate to True 

# Prompt the user to enter the year within the MIN and MAX
# prompt "Enter year: " and read year 

# Prompt the user to enter the month within the MIN and MAX
# prompt "Enter month (1-12): " and read month 

# Prompt the user to enter the day within the MIN and MAX
# prompt "Enter day: " and read day 

# If the year is less than MIN_YEAR then set validDate to False
# if year < MIN_YEAR then 
# set validDate to False 

# If the month is not within the MIN and MAX then set validDate to False
# else if month < MIN_MONTH or month > MAX_MONTH then 
# set validDate to False 

# else 
# If the day is not within the MIN and MAX then set validDate to False
# if day < MIN_DAY or day > MAX_DAY then 
# set validDate to False 
# end if 
# end if 

# Check if validDate is True
# if validDate is True then 
# print month "/" day "/" year " is a valid date."
# else 
# print month "/" day "/" year " is an invalid date." 
# end if 

# end

