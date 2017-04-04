def stringFromDict(name, words):
    return stringFromDictHelper(name, words, {})

def stringFromDictHelper(name, words, memo):
    if len(name) is 0:
        return True
    result = False
    atLeastOneMatched = False
    
    for word in words:
        wordLength = len(word)
        subString = name[:wordLength]
        if word == subString:
            atLeastOneMatched = True
            result |= stringFromDictHelper(name[wordLength:], words, memo)
    if atLeastOneMatched:
        return result
    else:
        return False

print(stringFromDict('foobarbazfooabracadabra', ['foo', 'bar', 'baz', 'abra', 'cad', 'abracad', 'abracadabra']))


# how to do the memoization
