from typing import List, Tuple


def quicksort(arr: List[int], low: int, high: int) -> List[int]:
    if len(arr) == 0:
        return []
    middle = low + (high - low) // 2
    pivot = arr[middle]
    left = [x for x in arr if x < pivot]
    right = [y for y in arr if y > pivot]
    sorted = (
        quicksort(left, 0, len(left) - 1)
        + [pivot] * (len(arr) - len(left) - len(right))
        + quicksort(right, 0, len(right) - 1)
    )
    return sorted


cases: List[Tuple[List[int], List[int]]] = [
    ([4, 3, 2, 1, 5], [1, 2, 3, 4, 5]),
    ([4, 7, 8, 2, 4, 3, 1], [1, 2, 3, 4, 4, 7, 8]),
    ([10, 2], [2, 10]),
    ([1], [1]),
    ([], []),
]

for input, expected in cases:
    print("Input: ", input)
    result = quicksort(input, 0, len(input) - 1)
    print("Result: ", result)
    print("Expected: ", expected)
    print("Pass: ", result == expected)
