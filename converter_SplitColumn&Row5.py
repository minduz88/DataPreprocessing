# Split TSVfile to Column & row - Save to list of dictionary. (Use defaultdict())

from collections import defaultdict

data = defaultdict(list) # set default value "list" in dictionary 
input_file_name = " "

with open(input_file_name, "r", enconding="utf-8-sig") as input_file:
    for line_num, line in enumerate(input_file):
        line = line.strip()
        cols = line.split("\t")

        if line_num == 0:
            col_names = cols
            continue

        for col_name, col in zip(col_names, cols):
            data[col_name].append(col)

print(data)