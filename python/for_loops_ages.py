#!/usr/bin/env python3.7

ages = {'Ana': 34, 'Edino': 35, 'Eder': 32, 'Javier': 36}
for key in ages:
    print(f"All people names: ")
    print(key)

print("")

for name, age in ages.items():
    print(f"Person named: {name}")
    print(f"Age of: {age}")

