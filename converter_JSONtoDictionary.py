# JSON to Dictionary

import ujson

input_file_name = " "

with open(input_file_name, "r", encoding="utf-8") as input_file:
    text = input_file.read()

data = ujson.loads(text)

print(data.keys())
print(data)

