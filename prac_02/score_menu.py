MENU = "(G)et score\n(P)rint result\n(S)how stars\n(Q)uit"


def main():
    score = get_valid_score()
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            print(determine_score_category(score))
        elif choice == "S":
            print_stars(score)
        else:
            print("Invalid choice.")
        print(MENU)
        choice = input(">>> ").upper()
    print("Finished.")


def get_valid_score():
    score = int(input("Score: "))
    while score < 0 or score > 100:
        print("Invalid score.")
        score = int(input("Score: "))
    return score


def determine_score_category(score):
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def print_stars(score):
    print(score * "*")


main()
