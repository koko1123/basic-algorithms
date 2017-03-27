import random

"""
Canonical implementation of Randomized selection
to find the nth order statistic in a list of numbers
piggy-backing on quicksort
"""


def quick_sort(arr, n = 0):
    quick_sort_helper(arr, 0, len(arr) - 1, n)


def quick_sort_helper(arr, start, end, n):
    if end - start < 1:
        return
    p = partition(arr, start, end)
    if p == n + 1:
        print(arr[n])
        return
    elif p > n + 1:
        quick_sort_helper(arr, start, p, n)
    else:
        quick_sort_helper(arr, p, end, n)


def partition(arr, start, end):
    # partition around a random pivot, return index of the pivot
    pivot_index = random.randint(start, end)
    pivot = arr[pivot_index]
    i = start + 1
    arr[start], arr[pivot_index] = arr[pivot_index], arr[start]
    for j in range(start + 1, end + 1):
        if arr[j] < pivot:
            arr[j], arr[i] = arr[i], arr[j]
            i += 1

    arr[i - 1], arr[start] = arr[start], arr[i - 1]
    return i - 1


nums = [6, 5, 4, 3, 2, 1]
quick_sort(nums, 3)  # should print 2
print(nums)
