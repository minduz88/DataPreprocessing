import re
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

import re

in_file ="C:\\Files\\NorthKorea'sDailyTrend_2020.txt"
out_file ="C:\Files\Data_splitSentences_Result.txt"

with open(in_file, 'r', encoding='UTF-8') as in_file:
    with open(out_file, 'w', encoding='UTF-8') as out_file:
        for line in in_file:
            wordforms = re.split("(?<=[.?!])\s+", line)

            for wordform in wordforms:
                print(wordform)
                out_file.write(wordform)   