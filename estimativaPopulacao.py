popA = 80000
popB = 200000
year = 0

while popA <= popB:
	popA += popA * 0.03
	popB += popB * 0.015
	year += 1

print("A população 'A' se iguala ou ultrapassa a população 'B' em", year,"anos.")