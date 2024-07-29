from typing import List, Tuple


def quicksort(input: List[int], low: int, high: int) -> None:
    if low < high:
        p = partition(input, low, high)
        quicksort(input, low, p)
        quicksort(input, p + 1, high)


def partition(input: List[int], low: int, high: int) -> int:
    middle = low + (high - low) // 2
    pivot = input[middle]
    start = low - 1
    end = high + 1
    while True:
        start += 1
        while input[start] < pivot:
            start += 1

        end -= 1
        while input[end] > pivot:
            end -= 1

        if start >= end:
            return end
        input[start], input[end] = input[end], input[start]


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
