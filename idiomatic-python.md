# figure out how to generate permutations
# list comprehension
# using enumerate
# copy list with list()

# floating point underflow occurs when a a value is too close to 0 to 
# distinguish it from 0

# integer underflow occurs when the value would be less than the minimum integer
# representable in that class

# Heaps
```py
heap = []
heap = heapify([1,2,3,4,5])

heappush(heap, item)
heappush(heap, (5, 'something'))

heappop(heap)
heappushpop(heap, item)
heapreplace(heap,item)

merge(iterables)
```

# remove key from dictionary
```
dict.pop('key', None)
```

# optional parameters
```
def myfunc(a,b, *args, **kwargs):
   for ar in args:
      print ar
myfunc(a,b,c,d,e,f)
```

# for map
tuples = [(time.time(), x) for x in args[0]]

# how to concat two arrays
[1] + [2]
