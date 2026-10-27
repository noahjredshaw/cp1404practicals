from guitar import Guitar

gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
another_guitar = Guitar("Another Guitar", 2013, 10)

print(f"{gibson.name} get_age() - Expected 100, got {gibson.get_age()}")
print(f"{another_guitar.name} get_age() - Expected 13, got {another_guitar.get_age()}")

print(f"{gibson.name} is_vintage() - Expected True, got {gibson.is_vintage()}")
print(f"{another_guitar.name} is_vintage() - Expected False, got {another_guitar.is_vintage()}")
