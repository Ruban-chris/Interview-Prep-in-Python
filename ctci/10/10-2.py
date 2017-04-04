# Write a method to sort an array of strings so that all the anagrams
# are next to each other.
mystrings = ['iceman', 'what', 'rat',  'cares', 'acres', 'tar', 'races', 'scare', 'cinema', 'thaw']

def groupAnagramsTogether(strings):
    # guard case
    if len(strings) is 0: return strings
    
    result = []
    while len(strings) > 0:
        firstString = strings[0]
        strings.remove(firstString)
        result.append(firstString)
        for string in strings:
            if stringsAreAnagrams(firstString, string):
                result.append(string)
                strings.remove(string)
    return result

def stringToScore(string):
    # guard case
    if len(string) is 0: return 0
    numericScore = 0
    charScoreDefinition = {
        "a":1,
        "b":2,
        "c":3,
        "d":4,
        "e":5,
        "f":6,
        "g":7,
        "h":8,
        "i":9,
        "j":10,
        "k":11,
        "l":12,
        "m":13,
        "n":14,
        "o":15,
        "p":16,
        "q":17,
        "r":18,
        "s":19,
        "t":20,
        "u":21,
        "v":22,
        "w":23,
        "x":24,
        "y":25,
        "z":26
    }
    for char in string:
        numericScore += charScoreDefinition[char]
    return numericScore

def stringsAreAnagrams(string1, string2):
    if len(string1) != len(string2): return False
    string1Score = stringToScore(string1)
    string2Score = stringToScore(string2)
    if string1Score is string2Score:
        return True
    else:
        return False

print(groupAnagramsTogether(mystrings))
