"""
Emails
Estimate: 10 minutes
Actual:   ... minutes
"""

email_to_name = {}
email = input("Email: ")
while email != "":
    name = " ".join(email.split("@")[0].title().split("."))
    print(f"Is your name {name}?", end=" ")
    choice = input("(Y/n) ").upper()
    if choice != "" and choice != "Y":
        name = input("Name: ")
    email_to_name[email] = name
    email = input("Email: ")
for email, name in email_to_name.items():
    print(f"{name} ({email})")
