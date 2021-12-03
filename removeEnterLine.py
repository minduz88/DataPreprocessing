print("\n\nSTART REMOVE ENTERLINE ..\n\n")

in_file ="C:\Files\Data_removeEnterLine.txt"
out_file ="C:\Files\Data_removeEnterLine_Result.txt"

with open(in_file, "r", encoding="utf-8") as in_file:
    with open(out_file, "w", encoding="utf-8") as out_file:
        
        textData = in_file.read()
        lines = textData.replace("\n"," ").replace("\" \"", "\"\n\"")

        out_file.write(lines)

#print result
with open("C:\Files\Data_removeEnterLine_Result.txt", "r", encoding="utf-8") as out_file2:
    
    lines = out_file2.read()
    print(lines)

print("\n\n FINISHED REMOVE ENTERLINE.")