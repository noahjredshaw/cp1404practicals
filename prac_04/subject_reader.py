"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    """Program to load and display subject data from file."""
    subject_data = load_subject_data(FILENAME)
    print_subject_details(subject_data)
    print(subject_data)


def load_subject_data(filename=FILENAME):
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(filename)
    subject_data = []
    for line in input_file:
        print(line)  # See what a line looks like
        print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        print(parts)  # See what the parts look like (notice the integer is a string)
        # Make the number an integer as part of a new, poorly named, list
        data_pair = [parts[0], parts[1], int(parts[2])]
        subject_data.append(data_pair)
        print(data_pair)  # See if that worked
        print("----------")
    input_file.close()
    return subject_data


def print_subject_details(subject_data):
    for data_pair in subject_data:
        print(f"{data_pair[0]} is taught by {data_pair[1]} and has {data_pair[2]} students")

main()