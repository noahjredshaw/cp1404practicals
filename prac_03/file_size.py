def main():
    filename = input("Enter filename: ")
    while filename != "":
        try:
            number_of_lines = determine_file_size(filename)
            print(f"{filename} has {number_of_lines} lines.")
        except FileNotFoundError:
            print(f"Error: {filename} does not exist.")
        filename = input("Enter filename: ")


def determine_file_size(filename):
    number_of_lines = 0
    with open(filename, "r") as in_file:
        for line in in_file: # A weak warning is raised here, but no issues may occur.
            number_of_lines += 1
    return number_of_lines


main()
