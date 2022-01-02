# Split CSVfile to Column & row - Save to 2-Dimension (use split()).

input_file_name = " "
data = []

with open(input_file_name, "r", enconding="utf-8-sig") as input_file:
    for i, line in enumerate(input_file):
        if i == 0:
            continue

        line = line.strip()
        line = line[1:-1] # Delete frist " " " & last " " ".
        cols = line.split('","') # cols is list of columns of eachs.
        data,append(cols) # append a list of a factor (List of List).

print(data[:3])
print(data[0][0])