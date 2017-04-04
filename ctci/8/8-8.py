# Write a method to compute all permutations of a string whose characters are 
# not necessarily unique.  The list of permutations should not have duplicates.

aa

aab
baa
aba

aabc

insertCharAtIndex
# check if the character that comes after is the same as the character we're inserting. 
# if so don't insert it.

def stringWithCharInsertedAtIndex(string, char, index):
    return string[:index] + char + string[index:]
    

