import random
# compute a random subset
def random_subset(n, k):
    changed_elements = {}
    for i in range(k):
        random_index = random.randrange(i, n)
        rand_index_mapped = changed_elements.get(random_index, random_index)
        i_mapped = changed_elements.get(i,i)
        changed_elements[random_index] = i_mapped
        changed_elements[i] = rand_index_mapped
    return [changed_elements[i] for i in range(k)]

print(random_subset(5, 2))
