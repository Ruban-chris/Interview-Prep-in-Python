def hashString(string, modulus):
    kMult = 997
    val = 0
    for char in string:
        val = (val * kMult + char) % modulus
    return val

def groupAnagrams(words):
    if len(words) is 0: return []
    groups = {}
    for word in words:
        hv = hashString(word, len(words))
        if hv in groups:
            groups[hv] = groups[hv].append(word)
        else:
            groups[hv] = [word]
    results = []
    for k,v in groups.items():
        if len(v) > 1:
            results.append(v)
    return results
    
myWords = ['debitcard', 'elvis', 'silent', 'badcredit', 'lives', 'freedom', 'listen', 'levis', 'money']

print(groupAnagrams(myWords))

def findAnagrams(words):
    sortedStringToAnagrams = {}
    for word in words:
        
        sortedCharArray = list(word)
        sortedCharArray = sorted(sortedCharArray)
        sortedString = sortedCharArray.join('')
        
        if sortedString in sortedStringToAnagrams:
            sortedStringToAnagrams[sortedString].append(word)
        else:
            sortedStringToAnagrams[sortedString] = [sortedString]
        
        