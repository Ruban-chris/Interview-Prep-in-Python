def isSubstring(s1, s2):
    return s1 in s2

def isRotation(s1, s2):
    rIdx = None
    i = 1
    while rIdx is None and i < len(s1):
        s1x = s1[0:i]
        s2y = s2[len(s1) - i:]
        print('s1x', s1x)
        print('s2y', s2y)
        if s1x == s2y:
            print('hey')
            rIdx = i
        else:
            print('i', i)
            i += 1
    if rIdx is not None:
        s2x = s2[:i]
        return isSubstring(s2x, s1)
    else:
        return False

print(isRotation('waterbottle', 'erbottlewat'))