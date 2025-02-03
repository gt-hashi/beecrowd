fuel_efficiency = 12

hours = int(input())
kph = int(input())

dist = hours*kph

fuel_needed = dist/fuel_efficiency

print(f"{fuel_needed:.3f}")