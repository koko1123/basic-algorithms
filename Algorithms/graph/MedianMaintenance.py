"""
implements the median maintainence algorithm for a "stream" of numbers
"""
import heapq
# store the smaller half
smaller_half_max_heap = []
# store the larger half
larger_half_min_heap = []


def find_median():
    # even numbered elements
    if len(smaller_half_max_heap) == len(larger_half_min_heap):
        return (smaller_half_max_heap[0] + larger_half_min_heap[0])/2
    # odd numbered elements return the first element of the larger two
    if len(smaller_half_max_heap) > len(larger_half_min_heap):
        return -1 * smaller_half_max_heap[0]
    else:
        return larger_half_min_heap[0]


def place_element(element):
    if len(smaller_half_max_heap) == 0 & len(larger_half_min_heap) == 0:
        # default to the larger half
        heapq.heappush(larger_half_min_heap, element)

    elif abs(smaller_half_max_heap[0]) > element:
        # janky solution to my maxheap, but I understand this is canonical to python
        heapq.heappush(smaller_half_max_heap, -1 * element)

    elif larger_half_min_heap[0] < element:
        heapq.heappush(larger_half_min_heap, element)

    if abs(len(smaller_half_max_heap) - len(larger_half_min_heap)) > 1:
        rebalance_halves()


def rebalance_halves():
    if len(smaller_half_max_heap) > len(larger_half_min_heap):
        heapq.heappush(larger_half_min_heap, -1 * heapq.heappop(smaller_half_max_heap))
    else:
        heapq.heappush(smaller_half_max_heap, -1 * heapq.heappop(larger_half_min_heap))

# input routine
sum_of_medians = 0
with open('medianStream.txt') as input_file:
    for number in input_file:
        place_element(int(number))
        sum_of_medians += find_median()

# print last four digits of the sum of all our medians
print(sum_of_medians % 10000)