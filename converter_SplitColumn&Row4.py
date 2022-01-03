# Split TSVfile to Column & row - Save to list of dictionary.

input_file_name = " "
data = {}

with open(input_file_name, "r", enconding="utf-8-sig") as input_file:
    for line_num, line in enumerate(input_file):
        line = line.strip()
        cols = line.split("\t")

        if line_num == 0:
            col_names = cols
            for col_name in col_names: # assign default dictionary
                data[col_name] = []
            continue

        for col_name, col in zip(col_names, cols):
            data[col_name].append(col)

print(data)