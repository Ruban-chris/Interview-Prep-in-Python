# i will assume all elements are either alpha or number

def greatest_equal_subarray(array):
    alpha_count = 0
    num_count = 0
    diffs = {}
    sub_array_length = 0
    sub_start = 0
    sub_end = 0
    for i, el in enumerate(array):
        if str(el).isalpha():
            alpha_count += 1
        else:
            num_count += 1
        difference = alpha_count - num_count
        if difference == 0:
            if i + 1 > sub_array_length:
                sub_array_length = i + 1
                sub_start = 0
                sub_end = i
        if difference in diffs:
            candidate_length = i - diffs[difference]
            if candidate_length > sub_array_length:
                sub_start = diffs[difference] + 1
                sub_end = i
                sub_array_length = candidate_length
        else:
            diffs[difference] = i
    return array[sub_start: sub_end + 1]

assert(['1', '1', 'a', '1', 'a', '1', 'a', 'a', 'a', '1'] == greatest_equal_subarray(['1','1','a','1','a','1','a','a','a','1']))
assert(['1', '1', 'a', '1', 'a', '1', 'a', 'a'] == greatest_equal_subarray(['1','1','a','1','a','1','a','a','a']))
assert(['1', 'a', '1', 'a'] == greatest_equal_subarray(['1','1','a','1','a','1']))
assert(['1', 'a'] == greatest_equal_subarray(['1','a','a','a','a','1']))
