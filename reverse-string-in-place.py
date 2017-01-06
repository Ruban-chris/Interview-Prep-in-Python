def reverseString(string):
    # guard case
    if len(string) is 0:
        return

    string_list = list(string)

    # meet in the middle
    left_idx = 0
    right_idx = len(string) - 1
    while left_idx < right_idx:
        character = string_list[right_idx]
        string_list[right_idx] = string_list[left_idx]
        string_list[left_idx] = character

        left_idx += 1
        right_idx -= 1

    return print(''.join(string_list))

reverseString('abcdefg')
reverseString('asd')

# Complexity
# O(n) time because we're looping through the string n/2 times
# O(n) space because we're creating string_list
