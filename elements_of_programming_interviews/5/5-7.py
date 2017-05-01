def exp(x,y):
    print(x)
    print(y)
    if y == 0:
        return 1
    if y == -1:
        return 1/x
    if y == 1:
        return x
    yIsEven = y % 2 is 0
    if yIsEven:
        return exp(x * x, y/2)
    else:
        if y > 0:
            return x * exp(x, y - 1)
        else:
            return 1/x * exp(x, y + 1)

# print(exp(2,-4))

def expIter(x,y):
    if y is 0:
        return 1
    if x is 0:
        return 0
    if y is 1:
        return x
    if y is -1:
        return -x
        
    if y < 0:
        x = 1/x
        y = -y
    
    result = 1
    
    while y > 0:
        if y % 2 is 0:
            y = y/2
            x = x * x
        else:
            y -= 1
            result = result * x
    
    return result
    
print(expIter(2, -4))