def isOneAway(s1, s2):
    if len(s1) is len(s2):
        editsCounter = 0
        for i in range(len(s1)):
            if editsCounter > 1:
                return False
            if s1[i] is not s2[i]:
                editsCounter += 1
        return True
    else:
        if abs(len(s1) - len(s2)) > 1:
            return False
        if len(s1) > len(s2):
            ls = s1
            ss = s2
        else:
            ls = s2
            ss = s1
        for i in range(len(ss)):
            if (ls[i] is not ss[i]) and (i + 1 < len(ls)):
                if (ls[i + 1] is not ss[i]):
                    return False
        return True

print(isOneAway('asjdfu8we;hgbjklasvlhas', 'asjdfu8we;hgbjklasvlhas'))

# what i can do better
# break into helper functions
# len(s1) + 1 check can get rid of abs line and ls, ss assignment
# dont need an editsCounter either

