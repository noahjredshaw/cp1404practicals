COLOURS_TO_HEX = {"Absolute Zero": "#0048ba", "Acid Green": "#b0bf1a", "Alice Blue": "#f0f8ff", "Alizarin Crimson": "#e32636", "Amaranth": "#e52b50"}

colour = input("Colour: ").title()
while colour != "":
    try:
        print(COLOURS_TO_HEX[colour])
    except KeyError:
        print("Invalid colour!")
    colour = input("Colour: ").title()
print("Wasn't that colourful?")