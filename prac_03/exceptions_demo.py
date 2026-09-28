"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
Answer: A ValueError will occur when the user inputs a string into the numerator/denominator fields.
2. When will a ZeroDivisionError occur?
Answer: A ZeroDivisionError will occur when the user attempts to put a '0' in the denominator field.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
Answer: Yes, by using a while loop to verify the user's input in the denominator field.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Denominator cannot be 0!")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")