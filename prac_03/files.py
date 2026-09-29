# # 1.
# filename = "name.txt"
# out_file = open(filename, "w")
# name = input("Name: ")
# print(name, file=out_file)
# out_file.close()
#
# # 2.
# filename = "name.txt"
# in_file = open(filename, "r")
# name = in_file.read().strip()
# print(f"Hi {name}!")
# in_file.close()

# 3.
with open("numbers.txt", "r") as in_file:
    number_one = int(in_file.readline())
    number_two = int(in_file.readline())
    sum_of_numbers = number_one + number_two
    print(f"Sum of {number_one} and {number_two} = {sum_of_numbers}")
