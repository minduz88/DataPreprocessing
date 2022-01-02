# Read a File and Split Column - read all of range that in file (Use the function of splitlines()).

input_file_name = " "

with open(input_file_name, "r", encoding="utf-8-sig") as input_file:
    text = input_file_name.read()

lines = text.splitlines()

print("a given text file {}'s number of Columns is {}." .format(input_file_name, len(lines)))