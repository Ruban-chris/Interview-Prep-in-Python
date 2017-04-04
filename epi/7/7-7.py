
def mnemonics(pn):
    charMap = {
        2: 'abc',
        3: 'def',
        4: 'ghi',
        5: 'jkl',
        6: 'mno',
        7: 'pqrs',
        8: 'tuv',
        9: 'wxyz'
    }
    pnAsList = list(pn)
    if len(pnAsList) == 1:
        return [[x] for char in charMap[pnAsList[0]]]
    else:
        popped = pnAsList.pop
        result = []
        for array in mnemonics("".join(pnAsList)):
            for char in charMap[popped]:
                arrayCopy = copy(array)
                arraycopy.insert(popped, 0)
                result.append(arrayCopy)
        return result
    
print(mnemonics('234'))