"""array_processor.py - Computational Array Techniques Module
CSE1021 Algorithmic Toolkit"""

def reverse_array(arr):#Reverses the order of elements in an array using index swapping
    arr=list(arr)
    ra= arr.copy()
    left = 0
    right = len(ra) - 1
    while left < right:
        (ra[left], ra[right]) = (ra[right], ra[left])
        left += 1
        right -= 1
    return ra

def remove_duplicates(arr): #Removes duplicate elements from an array while preserving original order
    arr=list(arr)
    ui = []
    seen = set()
    for item in arr:
        if item not in seen:
            seen.add(item)
            ui.append(item)
    return ui

def partition_array(arr, pivot): #Partitions array elements into three groups: < pivot, == pivot, > pivot
    arr, pivot = list(arr), int(pivot)
    less = []
    equal = []
    greater = []
    for num in arr:
        if num < pivot:
            less.append(num)
        elif num == pivot:
            equal.append(num)
        else:
            greater.append(num)
    return less, equal, greater


def kth_smallest_element(arr, k): #Finds the Kth smallest element in an unsorted list (1-indexed)
    arr, k = list(arr), int(k)
    if k <= 0 or k > len(arr):
        raise ValueError("Invalid value for k.")
    t = arr.copy()
    t.sort()
    return t[k - 1]