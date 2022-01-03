# split word from unstructured text. (count Frequency)

input_file_name =" "
wordform_counter = {}

with open(input_file_name, "r", encoding="utf-8") as input_file:
    for line in input_file:
        wordforms = line.split()

        for wordform in wordforms:
            wordform_counter[wordform] = wordform_counter.get(wordform, 0) + 1

for wordform, count in wordform_counter.items():
    print("{}\t{}".format(wordform, count))
