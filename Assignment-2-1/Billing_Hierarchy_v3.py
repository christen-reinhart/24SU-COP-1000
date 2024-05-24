#Sequential Statements 2-4 Pseudocode

#start

Declarations
    string = prompt "weekly salary"
    string = number dependents "enter number
    
    num calculate state tax 
    num calculate federal tax 
    
#end



#Understanding Arithmetic 2-3 Pseudocode

start 

   Declarations
	string prompt = "enter amount"
   num retail price
	num wholesale price
   num profit
   num sale price
   
   output prompt 
   input "amount"
   output prompt 
   Input "number of people"
   output "pay values"
   	
End 

#Assigning Age Variables 2-2 Pseudocode

Start 

   Declarations 
   string  "current age" 
   string number "current year"
   output prompt "enter currnet age"
   input "age"
   output prompt "enter currnt year"
   input "year" 
   
End 

Assignment 2-2 Revised 

# Pseudocode for calculating age in the year 2050

BEGIN

    # Define variables for current age and current year
    SET myCurrentAge TO 45
    SET currentYear TO 2024

    # Calculate age in the year 2050
    SET myNewAge TO myCurrentAge + (2050 - currentYear)

    # Print current age
    DISPLAY "My Current Age is " + myCurrentAge

    # Print age in 2050
    DISPLAY "I will be " + myNewAge + " in 2050."

END


Assignment 2-3 Revised 

# Pseudocode for calculating prices and discounts

BEGIN

    # Define items and their prices
    SET itemName TO "TV Stand"
    SET retailPrice TO 325.00
    SET wholesalePrice TO 200.00

    # Calculate profit
    SET profit TO retailPrice - wholesalePrice

    # Calculate sale price with a 10% discount
    SET salePrice TO retailPrice * 0.90

    # Calculate sale profit
    SET saleProfit TO salePrice - wholesalePrice

    # Print the results
    DISPLAY "Item Name: " + itemName
    DISPLAY "Retail Price: $" + retailPrice
    DISPLAY "Wholesale Price: $" + wholesalePrice
    DISPLAY "Profit: $" + profit
    DISPLAY "Sale Price: $" + salePrice
    DISPLAY "Sale Profit: $" + saleProfit

END


Assignment 2-4 Revised 

# Pseudocode for calculating paycheck

BEGIN

    # Prompt user for input and initialize variables
    DISPLAY "Enter the weekly salary: "
    INPUT salary

    DISPLAY "Enter the number of dependents: "
    INPUT numDependents

    # Calculate state tax withholding at 6.5%
    stateTax = salary * 0.065

    # Calculate federal tax withholding at 28.0%
    federalTax = salary * 0.28

    # Calculate dependent deductions at 2.5% of the salary for each dependent
    dependentDeduction = salary * 0.025 * numDependents

    # Calculate total withholding as stateTax + federalTax + dependentDeduction
    totalWithholding = stateTax + federalTax + dependentDeduction

    # Calculate take-home pay as salary - totalWithholding
    takeHomePay = salary - totalWithholding

    # Output the results
    DISPLAY "State Tax: $" + stateTax
    DISPLAY "Federal Tax: $" + federalTax
    DISPLAY "Dependent Deductions: $" + dependentDeduction
    DISPLAY "Salary: $" + salary
    DISPLAY "Take Home Pay: $" + takeHomePay

END



