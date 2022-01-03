# TSV to JSON

import ujson

imput_file_name = " "
output_file_name =" "

with open(input_file_name, "r", encoding="utf-8") as input_file, \
        open(output_file_name, "w", encoding="utf-8") as output_file:
    for line_num, line in enumerate(input_file):
        line = line.strip()
        cols = line.split("\t")

        if line_num == 0:
            col_names = cols
            continue

        data = {col_name: col for col_name, col in zip(col_names, cols)}
        print(ujson.dumps(data, ensure_ascii=false))