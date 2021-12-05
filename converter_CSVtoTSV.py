# A converter From CSV to TSV.

input_file_name = "C:\Files\\test.csv"
output_file_name = "C:\Files\\test.txt"

with open(input_file_name, "r", encoding="utf-8-sig") as input_file, \
    open(output_file_name, "w", encoding="utf-8") as output_file:
    for line in input_file:
        line = line.strip()
        line = line[1:-1]
        line = line.replace('","', "\t")
        print(line, file=output_file)

        # # split, join 사용
        # cols = line.split('","')
        # print("\t".join(cols), file=output_file)