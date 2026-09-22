def main():
    password = get_password()
    print_asterisks(password)


def get_password():
    password = input("Password: ")
    while len(password) < 10:
        print("Password does not meet minimum requirement.")
        password = input("Password: ")
    return password


def print_asterisks(password):
    print(len(password) * "*")


main()
