# Moduling a part of split sentences.

def split_sentences(text):
    text = text.strip().replace(", ", " .\n").replace("? ", " ?\n").replace("! ", " !\n")
    sentences = text.splitlines()

    return sentences

input_file_name = " "
sentences = []

with open(input_file_name, "r", encoding="utf-8") as input_file:
    for line in input_file:
        sub_sentences = split_sentences(line)
        sentences += sub_sentences

for sentence in sentences[:5]:
    print(sentence)