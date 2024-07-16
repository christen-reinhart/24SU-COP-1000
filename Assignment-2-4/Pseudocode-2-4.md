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
