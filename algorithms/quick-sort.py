def partition(array, left, right, pivot):
    while left <= right:
        while array[left] < pivot:
            left += 1
        while array[right] > pivot:
            right -= 1
        if left <= right:
            array[left], array[right] = array[right], array[left]
            left += 1
            right -= 1
    return left

def quicksort_helper(array, left, right):
    if left >= right: return
    pivot = array[(left + right) // 2]
    partition(array, left, right, pivot)
    index = partition(array,left,right,pivot)
    quicksort_helper(array, left, index - 1)
    quicksort_helper(array, index, right)

def quicksort(array):
    quicksort_helper(array, 0, len(array) - 1)
    return array

unsorted_array = [2,5,3,6,7,8,1,2,3,4,5,4,5,6,2,4]
assert [1, 2, 2, 2, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 7, 8] == quicksort(unsorted_array)
