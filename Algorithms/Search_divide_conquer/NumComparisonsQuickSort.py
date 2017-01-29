import random
"""
Modify canonical quicksort to count number of comparisons
"""


def quick_sort(arr):
    print(quick_sort_helper(arr, 0, len(arr)-1))


def quick_sort_helper(arr, start, end):
    if end - start <= 1:
        return 0
    p = partition(arr, start, end)
    left_sum = quick_sort_helper(arr, start, p - 1)
    right_sum = quick_sort_helper(arr, p + 1, end)
    return end - start + 1 + left_sum + right_sum


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

# nums = [6, 5, 4, 3, 2, 1]
# quick_sort(nums)
# print(nums)
input_file = open('quicksortInput.txt', 'r')
unsorted_array = [int(x) for x in input_file.read().split()]
quick_sort(unsorted_array)
