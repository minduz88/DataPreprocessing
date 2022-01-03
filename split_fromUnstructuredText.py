# split word from unstructured text.

input_file_name =" "

with open(input_file_name, "r", encoding="utf-8") as input_file:
    for line in input_file:
        wordforms = line.split()

        for wordform in wordforms:
            print(wordform)