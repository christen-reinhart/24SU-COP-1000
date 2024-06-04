This program calculates prices for custom house signs.
"""

# Function to calculate the charge based on input parameters
def calculate_charge(numChars, woodType, color):
    charge = 35.00

    # Charge for additional characters if more than 5.
    if numChars > 5:
        charge += (numChars - 5) * 4

    # Charge for type of wood.
    if woodType == "oak":
        charge += 20.00

    # Charge for color of characters.
    if color == "gold":
        charge += 15.00

    return charge

# Prompting user for input
numChars = int(input("Enter the number of characters: "))
woodType = input("Enter the type of wood (oak or pine): ").strip().lower()
color = input("Enter the color of characters (black, white, or gold): ").strip().lower()

# Calculating the charge
charge = calculate_charge(numChars, woodType, color)

# Output the charge for this sign
print(f"The charge for this sign is ${charge:.2f}")
