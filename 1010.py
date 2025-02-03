# -*- coding: utf-8 -*-
# Read input values


code1, units1, price1 = input().split()
code2, units2, price2 = input().split()

# Convert inputs to appropriate types
units1 = int(units1)
price1 = float(price1)
units2 = int(units2)
price2 = float(price2)

# Calculate total amount
total = (units1 * price1) + (units2 * price2)

# Print the result with correct formatting
print(f"VALOR A PAGAR: R$ {total:.2f}")
