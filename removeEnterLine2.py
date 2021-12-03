import re

print("\n\nSTART REMOVE ENTERLINE2 ..\n\n")

in_file ="C:\Files\Data_removeEnterLine.txt"
out_file ="C:\Files\Data_removeEnterLine_Result1.txt"

with open(in_file, "r", encoding="utf-8") as in_file:
    with open(out_file, "w", encoding="utf-8") as out_file:
        
        textData = in_file.read()
        lines = textData.replace("\n"," ").replace("\" \"", "\"\n\"")
        out_file.write(lines)


with open("C:\Files\Data_removeEnterLine_Result1.txt", "r", encoding="utf-8") as in_file2:
    with open("C:\Files\Data_removeEnterLine_Result2.txt", "w", encoding="utf-8") as out_file2:

        for line in in_file2.readlines():
            aline = re.sub("^.", "", line)
            bline = re.sub(".$", "", aline)
            out_file2.write(bline)
            print(bline)

print("\n\n FINISHED REMOVE ENTERLINE2.")