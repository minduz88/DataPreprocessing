# JSON TO TSV

import ujson

input_file_name = " "
output_file_name = " "

with open(input_file_name, "r", encoding="utf-8") as input_file, \
        open(output_file_name, "w", encoding="utf-8") as output_file:

    for line in input_file:
        data =ujson.loads(line)
        items = data.values()
        print("\t".join(items), file=ouput_file)