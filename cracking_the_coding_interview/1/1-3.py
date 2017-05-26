# Write a method to replace all spaces in a string with '%20'.  You may assume
# that the string has sufficient space at the end to hold the additional characters,
# and that you are given the "true" length of the string. (Note: if implementing in Java,
# Please use a character array so that you can perform this operation in place.)

# 'asdf asdf asdf    '

# Ideas
# going to start from the end of the array. and have a write index and a read index and real space encountered
# if the char is an empty string, decrement the read index.
# else write the char to the write index and decremenet the write index.
# when we encounter a real spce, we write '%' , '2', '0'
def URLify(string):
    string_as_list = list(string)
    should_replace_spaces = False
    write_index = len(string_as_list) - 1
    i = len(string_as_list) - 1
    while i >= 0:
        if string_as_list[i] != ' ':
            string_as_list[write_index] = string_as_list[i]
            i-=1
            write_index -=1
            should_replace_spaces = True
        else:
            if should_replace_spaces:
                for char in '02%':
                    string_as_list[write_index] = char
                    write_index -= 1
            i -= 1
    return ''.join(string_as_list)

assert('Mr%20John%20Smith' == URLify('Mr John Smith    '))
