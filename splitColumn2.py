# read CSV file and split Column (Using function "open").

input_file_name ="C:\Files\fileName.csv"
lines = []

with open(input_file_name, "r", endconding="utf-8-sig") as input_file:
    for line in input_file:
        line = line.strip()
        lines.append(line)

# to see output result by formatting.
print("Total result column's numbers that given file name {} is {}." .format(input_file_name, len(lines)))
# printing result top 3 entity.
print(lines[0:3])
