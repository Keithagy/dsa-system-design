from typing import List, Tuple


# Certainly! Quicksort is a popular sorting algorithm known for its efficiency in sorting large datasets.
# The in-place version of Quicksort doesn't require additional storage space for sorting,
# as it rearranges the elements within the original array or list.
# Here's a basic implementation of in-place Quicksort in Python:
#
# In this implementation:
# quicksort is a recursive function that sorts the elements.
# partition rearranges the elements based on the pivot, which is chosen to be the middle element in this case.
# The array is sorted in place, meaning it doesn't require extra space for another array.
# Remember that the performance of Quicksort can vary depending on the choice of the pivot.
# In the worst case, its time complexity can degrade to O(n^2), but on average, it has a time complexity of O(n log n).
def quicksort(arr, low, high):
    if low < high:
        # Partitioning index
        pi = partition(arr, low, high)

        # Recursively sort elements before and after partition
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)


def partition(arr, low, high):
    # Choose the middle element as pivot
    mid = low + (high - low) // 2
    pivot = arr[mid]

    # Swap pivot with high for partition logic
    arr[mid], arr[high] = arr[high], arr[mid]

    # Pointer for the greater element
    i = low - 1

    # Traverse through all elements
    for j in range(low, high):
        # If current element is smaller than or equal to pivot
        if arr[j] <= pivot:
            # Increment index for smaller element
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


cases: List[Tuple[List[int], List[int]]] = [
    ([4, 3, 2, 1, 5], [1, 2, 3, 4, 5]),
    ([4, 7, 8, 2, 4, 3, 1], [1, 2, 3, 4, 4, 7, 8]),
    ([10, 2], [2, 10]),
    ([1], [1]),
    ([], []),
]

for input, expected in cases:
    print("Input: ", input)
    quicksort(input, 0, len(input) - 1)
    print("Result: ", input)
    print("Expected: ", expected)
    print("Pass: ", input == expected)
