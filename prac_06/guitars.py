"""
Estimated time: 20 Minutes
Actual time: 15 Minutes
"""

from guitar import Guitar

guitars = []

print("My guitars!")
name = input("Name: ")
while name != "":
    year = int(input("Year: "))
    cost = float(input("Cost: $"))
    guitars.append(Guitar(name, year, cost))
    print(f"{name} ({year}) : ${cost:.2f} added.")
    name = input("Name: ")
print("... Snip ...")
print("These are my guitars:")
longest_name = ""
for i, guitar in enumerate(guitars):
    if len(guitar.name) > len(longest_name):
        longest_name = guitar.name
    vintage_string = "(vintage)" if guitar.is_vintage() else ""
    print(
        f"Guitar {i + 1}: {guitar.name:>{len(longest_name)}} ({guitar.year}), worth $ {guitar.cost:10,.2f} {vintage_string}")
