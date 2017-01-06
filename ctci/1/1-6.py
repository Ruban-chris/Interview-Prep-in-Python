def compressString(string): 
    compressedStringArray = []
    counter = 0
    i = 0
    for char in string:
        counter += 1
        if (i + 1 >= len(string)) or (char is not string[i + 1]):
            compressedStringArray.append(char)
            compressedStringArray.append(str(counter))
            counter = 0
        i += 1
            
    print('compressedStringArray', compressedStringArray)
    if len(compressedStringArray) < len(string):
        return ''.join(compressedStringArray)
    else:
        return string

print(compressString('aabcccccaaa'))    