# start

# Constants
# MIN_YEAR = 0
# MIN_MONTH = 1
# MAX_MONTH = 12
# MIN_DAY = 1
# MAX_DAY = 31

# variable to determine if the date is valid
# set validDate to True

# get the year, month, and day from the user
# try:
# year = convert input("Enter year: ") to integer
# month = convert input("Enter month (1-12): ") to integer
# day = convert input("Enter day: ") to integer
# except ValueError:
# print "Invalid input. Please enter numeric values for year, month, and day."
# set validDate to False

# check year
# if validDate then
# if year < MIN_YEAR then
# set validDate to False
# Check month
# elif month < MIN_MONTH or month > MAX_MONTH then
# set validDate to False
# else:
# check day based on month
# if month in [4, 6, 9, 11] and (day < MIN_DAY or day > 30) then
# set validDate to False
# elif month == 2 and (day < MIN_DAY or day > 28) then
# set validDate to False
# elif day < MIN_DAY or day > MAX_DAY then
# set validDate to False
# end if
# end if

# output the result
# if validDate then
# print month "/" day "/" year " is a valid date."
# else:
# print month "/" day "/" year " is an invalid date."
# end if

# end
