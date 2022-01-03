# split sentens(e.g ., ?, ! and so on) - use replace() 

input_file_name =" "
sentences = []

with open(input_file_name, "r", encoding="utf-8") as input_file:
    for line in input_file:

        line = line.strip().replace(", ", " .\n").replace("? ", " ?\n").replace("! ", " !\n")