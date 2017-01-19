import random
"""
Canonical implementation of Quicksort (in place)
random pivot used
"""


def quick_sort(arr):
    quick_sort_helper(arr, 0, len(arr)-1)


def quick_sort_helper(arr, start, end):
    if end - start <= 1:
        return
    p = partition(arr, start, end)
    quick_sort_helper(arr, start, p - 1)
    quick_sort_helper(arr, p + 1, end)


def partition(arr, start, end):
    # partition around a random pivot, return index of the pivot
    pivot_index = random.randint(start, end)
    pivot = arr[pivot_index]
    i = start + 1
    arr[start], arr[pivot_index] = arr[pivot_index], arr[start]
    for j in range(start + 1, end+1):
        if arr[j] < pivot:
            arr[j], arr[i] = arr[i], arr[j]
            i += 1

    arr[i-1], arr[start] = arr[start], arr[i-1]
    return i-1

# test
chaos = [5, 6, 3, 7, 2, 4, 1]
quick_sort(chaos)
print(chaos)
