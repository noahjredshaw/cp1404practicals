from guitar import Guitar

guitars = [Guitar("Gibson L-5 CES", 1922, 16035.40),
           Guitar("Fender Stratocaster", 2014, 765.40), Guitar("Line 6 JTV-59", 2010, 1512.90)]

print("My guitars!")
# name = input("Name: ")
# while name != "":
#     year = int(input("Year: "))
#     cost = float(input("Cost: $"))
#     guitars.append(Guitar(name, year, cost))
#     print(f"{name} ({year}) : ${cost:.2f} added.")
#     name = input("Name: ")
# print("... Snip ...")
print("These are my guitars:")
vintage_string = ""
longest_name = ""
for guitar in guitars:
    if len(guitar.name) > len(longest_name):
        longest_name = guitar.name
    if guitar.is_vintage():
        vintage_string = "(vintage)"
    print(f"{guitar.name:{len(longest_name)}} ({guitar.year}), worth $ {guitar.cost:<6,.2f} {vintage_string}")
