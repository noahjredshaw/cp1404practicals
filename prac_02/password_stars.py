minimum_password_length = 10
password = input("Password: ")
while len(password) < minimum_password_length:
    print("Password does not meet minimum requirement.")
    password = input("Password: ")
print(len(password) * "*")