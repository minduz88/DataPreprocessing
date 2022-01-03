# dictionary to JSON

import ujson

input_file_name = " "

str = ujson.dumps(input_file_name, ensure_ascii=False)

output_file_name = " "

with open(output_file_name, "w", encoding="utf-8") as output_file:
    print(str, file=output_file)