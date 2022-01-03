# USE reader().

import csv

input_file_name = " "
data = []

with open(input_file_name, "r", enconding="utf-8-sig") as input_file:
    reader = csv.reader(input_file)
    for i, line in enumerate(reader):
        if i == 0:
            continue

        data.append(line)

print(data[:3])
