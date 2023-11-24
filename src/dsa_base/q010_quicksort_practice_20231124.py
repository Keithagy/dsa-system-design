from typing import List, Tuple


def quicksort(input: List[int], low: int, high: int) -> None:
    if low < high:
        p = partition(input, low, high)
        quicksort(input, low, p)
        quicksort(input, p + 1, high)


def partition(input: List[int], start: int, end: int) -> int:
    low = start - 1
    high = end + 1

    middle = start + (end - start) // 2
    pivot = input[middle]

    while True:
        low += 1
        while input[low] < pivot:
            low += 1

        high -= 1
        while input[high] > pivot:
            high -= 1

        if low >= high:
            return high

        input[low], input[high] = input[high], input[low]


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
