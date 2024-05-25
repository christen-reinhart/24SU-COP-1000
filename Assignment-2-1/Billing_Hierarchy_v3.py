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

#Pseudocode for calculating your age in  2050

Start

    #Define variables for current age and current year 
    set myCurrentAge to 45
    set currentYear to 2024

    #Calculate your age in the year 2050
    set myNewAge to myCurrentAge + (2050 - currentYear)

    #Print current age
    display "My Current Age is " + myCurrentAge

    #Print age in 2050
    display "I will be " + myNewAge + " in 2050."

End


Assignment 2-3 Revised 

#Pseudocode for calculating prices and discounts

Start

    #Define items and their prices 
    set itemName to "TV Stand"
    set retailPrice to 325.00
    set wholesalePrice to 200.00

    #Calculate profit
    set profit to retailPrice - wholesalePrice 

    #Calculate sale price with a 10% discount
    set salePrice to retailPrice * 0.90

    #Calculate sale profit
    set saleProfit to salePrice - wholesalePrice

    #Print the results
    display "Item Name: " + itemName
    display "Retail Price: $" + retailPrice
    display "Wholesale Price: $" + wholesalePrice
    display "Profit: $" + profit
    display "Sale Price: $" + salePrice
    display "Sale Profit: $" + saleProfit

End


Assignment 2-4 Revised 

#Pseudocode for calculating paycheck

Start 

    #Prompt user for input and initialize variables
    display "Enter the weekly salary: "
    input salary

    display "Enter the number of dependents: "
    input numDependents

    #Calculate state tax withholding at 6.5%
    stateTax = salary * 0.065

    #Calculate federal tax withholding at 28.0%
    federalTax = salary * 0.28

    #Calculate dependent deductions at 2.5% of the salary for each dependent
    dependentDeduction = salary * 0.025 * numDependents

    #Calculate total withholding as stateTax + federalTax + dependentDeduction
    totalWithholding = stateTax + federalTax + dependentDeduction

    #Calculate take home pay as salary - totalWithholding
    takeHomePay = salary - totalWithholding

    #Output the results
    display "State Tax: $" + stateTax
    display "Federal Tax: $" + federalTax
    display "Dependent Deductions: $" + dependentDeduction
    display "Salary: $" + salary
    display "Take Home Pay: $" + takeHomePay

End



