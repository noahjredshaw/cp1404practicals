"""
CP1404/CP5632 - Practical
Program to determine score status
"""
import random


def main():
    score = float(input("Enter score: "))
    category = determine_score_category(score)
    print(f"User score {score} is {category}")
    if category == "Excellent":
        print("You win a prize!")
    score = random.randint(0, 100)
    print(f"Random: {score} = {determine_score_category(score)}")


def determine_score_category(score):
    if score < 0 or score > 100:
        return  "Invalid score"
    elif score >= 90:
        return  "Excellent"
    elif score >= 50:
        return  "Passable"
    else:
        return  "Bad"


main()
