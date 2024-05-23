# Furniture.py - This program calculates profits and sales prices for a furniture company.

itemName = "TV Stand"
retailPrice = 325.00
wholesalePrice = 200.00

# Calculate profit
profit = retailPrice - wholesalePrice

# Calculate sale price (assuming a 10% discount)
salePrice = retailPrice * 0.90  # 10% discount is equivalent to 90% of the retail price

# Calculate sale profit
saleProfit = salePrice - wholesalePrice

# Print the results
print("Item Name: " + itemName)
print("Retail Price: $" + str(retailPrice))
print("Wholesale Price: $" + str(wholesalePrice))
print("Profit: $" + str(profit))
print("Sale Price: $" + str(salePrice))
print("Sale Profit: $" + str(saleProfit))

