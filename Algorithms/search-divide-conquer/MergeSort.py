"""
Implementation of merge sort algorithm
"""


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    half = int(len(arr) / 2)
    first_sorted_half = merge_sort(arr[:half])
    second_sorted_half = merge_sort(arr[half:])
    return merge(first_sorted_half, second_sorted_half)


def merge(first_half, second_half):
    n = len(first_half) + len(second_half)
    i = 0
    j = 0
    ans = []
    for k in range(n):
        if i >= len(first_half):
            ans.append(second_half[j])
            j += 1
            continue
        if j >= len(second_half):
            ans.append(first_half[i])
            i += 1
            continue

        if first_half[i] > second_half[j]:
            ans.append(second_half[j])
            j += 1
        elif first_half[i] < second_half[j]:
            ans.append(first_half[i])
            i += 1

    return ans


unsorted_array = [3, 2, 1, 6, 4, 7, 5, 8, 10, 9]
print(merge_sort(unsorted_array))
