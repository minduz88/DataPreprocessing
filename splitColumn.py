# read CSV file and split Column (Using function "open")

input_file_name ="C:\Files\fileName.csv"
line = []

input_file = open(input_file_name, "r", endcoding="utf-8-sig")

for line in input_file:
    line = line.strip() # delete '\n'
    lines.append(line)

input_file.close()

# to see output result by formatting.
print("Total result column's numbers that given file name {} is {}." .format(input_file_name, len(lines)))
# printing result top 3 entity.
print(lines[0:3])
