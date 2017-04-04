def treeAsList(node):
    queue = []
    queue.append(node)
    numberOfNodesAtSameDepth = len(queue)
    currentDepth = 0
    results = [[]]
    
    while len(queue) > 0:
        el = queue.pop(0)
        numberOfNodesAtSameDepth -= 1
        
        if el is not None:
            results[currentDepth].append(el)k
            queue.append(el.left)
            queue.append(el.right)
        
        if numberOfNodesAtSameDepth == 0:
            currentDepth += 1
            numberOfNodesAtSameDepth = len(queue)
            results.append([])
    
    return results
