"""
Script to count inversions
using mergeSort routine in this directory as the skeleton
"""


def merge_sort(arr):
    if len(arr) <= 1:
        return arr, 0
    half = int(len(arr)/2)
    first_sorted_half, x = merge_sort(arr[:half])
    second_sorted_half, y = merge_sort(arr[half:])
    merged_halves, z = merge(first_sorted_half, second_sorted_half)

    return merged_halves, z


def merge(first_half, second_half):
    n = len(first_half) + len(second_half)
    i = 0
    j = 0
    split_inversions = 0
    ans = []
    for k in range(n):
        if i >= len(first_half):
            ans.append(second_half[j])
            j += 1
            continue
        if j >= len(second_half):
            ans.append(first_half[i])
            split_inversions += len(first_half) - i
            i += 1
            continue

        if first_half[i] > second_half[j]:
            ans.append(second_half[j])
            j += 1
            split_inversions += len(first_half) - i
        elif first_half[i] < second_half[j]:
            ans.append(first_half[i])
            i += 1

    return ans, split_inversions


#input_file = open('Inversions.txt', 'r')
#numbers = [int(x) for x in input_file.read().split()]
numbers = [6, 5, 4, 3, 2, 1]
print(merge_sort(numbers)[1])
