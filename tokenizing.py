# Use & Definition split sentences

import re
from konlpy.tag import Komoran

    
def split_sentences(text):
    all_sentences = []
    lines = [line for line in text.strip().splitlines() if line.strip()]
    
    for line in lines:
        sentences = re.split("(?<=[.?!])\s+", line)
        all_sentences += sentences
    
    return all_sentences



def main():
    my_text = """첫 번째 문장.
       
    두번째 문장, 세 번째 문장? 네 번째와 다섯 번째.

"""

    komoran = Komoran()
    results = []
    sentences = split_sentences(my_text)
    
    for sentence in sentences:
        print(sentence)
        
    for sentence in sentences:
        part = komoran.pos(sentence)     # List of Morpheme analysis results in a sentence (by tuple)
        results.append(part)             # List of part list
        
    print(results)
    

main()
