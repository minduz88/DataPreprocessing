# Split CSVfile to Column & row - Save to list of dictionary.

input_file_name = " "
data = {}

with open(input_file_name, "r", enconding="utf-8-sig") as input_file:
    for i, line in enumerate(input_file):
        line = line.strip()
        line = line[1:-1]
        cols = line.split('","')

        if i == 0:
            col_names = cols
            for col_name in col_names:
                data[col_name] = []
            continue

        for col_name, col in zip(col_names, cols):
            data[col_name].append(col)

print(data.keys)
print(data['locationName'])
print(data)