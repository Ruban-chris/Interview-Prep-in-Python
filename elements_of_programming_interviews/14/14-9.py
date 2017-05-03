# team photo day
# Design an algorithm that takes as input two teams and the heights of the players
# in the teams and checks if it is possible to place players to take the photo subject
# to the placement constraint.

# assume lengths of teamA and teamB are the same

def canTakePhoto(teamA, teamB):
    if len(teamA) is 0: return True
    sortedA = sorted(teamA)
    sortedB = sorted(teamB)
    backRowTeam = sortedA if sortedA[0] > sortedB[0] else sortedB
    frontRowTeam = sortedB if sortedB[0] < sortedA[0] else sortedA
    for i, height in enumerate(backRowTeam):
        if height <= frontRowTeam[i]:
            return False
    return True


assert(canTakePhoto([5,3,7], [2,6,4]) == True)
assert(canTakePhoto([5,3,1], [2,4,1]) == False)
