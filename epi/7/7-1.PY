#Implement string/integer conversion functions
def stringToInteger(string):
    order = len(string) - 1
    integer = 0
    for char in string:
        integer += int(char) * 10 ** order
        order -= 1
    return integer

# print(stringToInteger('4567'));
    
def integerToString(integer):
    array = []
    while integer is not 0:
        array.insert(0, str(integer % 10))
        integer = integer // 10
    return ''.join(array)
    
print(integerToString(stringToInteger(integerToString(4562423423))))