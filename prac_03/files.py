# 1.
filename = "name.txt"
out_file = open(filename, "w")
name = input("Name: ")
print(name, file=out_file)
out_file.close()

# 2.
filename = "name.txt"
in_file = open(filename, "r")
name = in_file.read().strip()
print(f"Hi {name}!")
in_file.close()
