# How would you check if a given array entry can be added to two more to get 
# the specified number?

# Problem statement
# find 3 entries in the array (not necessarily distinct) that add up to a given number
# Constraints
# can the number be negative? im going to assume yes they can be negative
# are the numbers real numbers or integers? i am going to assume they are real numbers. ie they can be floats
# can i assume that all the entries are numbers?  i am going to assume yes

# Input
# array, n

# Output
# array of three numbers that add up to n

# Ideas
# We can try a brute force approach, trying every possibility until we find an answer. 
# There could be multiple answers, but we're just looking for one.
# combination n choose 3. O(n! / 3!(n-3)!)

# the brute-force algorithm is to consider all possible triples by three nested for loops iterating over all entries
the time complexity is O(n ** 3) and the space complexity is O(1)

# we can use recursion to try every possibility.

[1,2,3,-1,-2,-3,0]
# when our list is 2 long, we can then search for an element whose addition to the list equals the number we're looking for. else we return false
# we can generate a list of every possible combination of 2. then for each list we try to find an element. if we use a generator, we can avoid a lot of space
# complexity related to storing the combinations.


[1, 2, -3]
[1, 3, ]
[1, -1, ]
[1, -2, ]
[1, -3, ]
[1, 0, ]


# Test cases
# [0, 0, 0], 0
# [], 0
# [math.inf, 1, 0], math.inf => doesn't matter what the other values are as long as one is inf
# [1,1,2,2,3,3,-1,-1,-2,-2,-3,-3,0], 0

# Code
