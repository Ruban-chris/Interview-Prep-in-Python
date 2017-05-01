# knapsack problem
class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value

def optimumSubjectToCapacity(items, capacity):
    V = [[-1] * (capacity + 1) for i in range(len(items))]
    
    return optimumSubjectToItemAndCapacity(items, items.size() - 1, capacity, V)

def optimumSubjectToItemAndCapacity(items, k, availableCapacity, V):
    if k < 0:
        return 0
    
    if V[k][availableCapacity] == -1: 
        withoutCurrItem = optimumSubjectToItemAndCapacity(items, k - 1, availableCapacity, V)
        
        withCurrItem = 0 if availableCapacity < items.get(k).weight else items[k].value  + optimumSubjectToItemAndCapacity(items, k - 1, availableCapacity - items[k].weight, V)
        
        V[k][availableCapacity] = Math.max(withoutCurrItem, withCurrItem)
    
    return V[k][availableCapacity]