# This program calculates prices for custom house signs.


# Declare and initialize variables here.
charge = 0.00   # Charge for this sign.
numChars = 8    # Number of characters.
color = "gold"  # Color of characters.
woodType = "oak" # Type of wood.

# Write assignment and if statements here as appropriate.

# Base charge for the sign.
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

# Output Charge for this sign.
print("The charge for this sign is $" + str(charge))
