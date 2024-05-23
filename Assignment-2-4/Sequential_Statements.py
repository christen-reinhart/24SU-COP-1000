# Initialize variables with input from the user
salary = float(input("Enter the weekly salary: "))
numDependents = int(input("Enter the number of dependents: "))

# Calculate state withholding tax at 6.5%
stateTax = salary * 0.065

# Calculate federal withholding tax at 28.0%
federalTax = salary * 0.28

# Calculate dependent deductions at 2.5% of the salary for each dependent
dependentDeduction = salary * 0.025 * numDependents

# Calculate total withholding as stateTax + federalTax + dependentDeduction
totalWithholding = stateTax + federalTax + dependentDeduction

# Calculate take-home pay as salary - totalWithholding
takeHomePay = salary - totalWithholding

# Output statements
print("State Tax: $" + str(stateTax))
print("Federal Tax: $" + str(federalTax))
print("Dependent Deductions: $" + str(dependentDeduction))
print("Salary: $" + str(salary))
print("Take Home Pay: $" + str(takeHomePay))

