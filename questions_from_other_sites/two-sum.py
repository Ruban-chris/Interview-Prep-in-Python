def twoSum(numbers, target):
    index = 0
    numToFind = target - numbers[index]
    while index < len(numbers) - 1:
        for i in range(index + 1, len(numbers)):
            if numbers[i] == numToFind:
                return True
        index += 1
        numToFind = target - numbers[index]
    return False

print(twoSum([-1, 2, 4, 5, 7, 9], 7))
