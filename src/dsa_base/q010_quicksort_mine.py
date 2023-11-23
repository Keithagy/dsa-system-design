from typing import List, Tuple


def quicksort(arr: List[int], low: int, high: int) -> None:
    if low < high:
        p = partition(arr, low, high)
        quicksort(
            arr, low, p
        )  # include p since this parition method does not necessarily place p correctly
        quicksort(arr, p + 1, high)


def partition(arr: List[int], low: int, high: int) -> int:
    middle = low + ((high - low) // 2)
    start = low - 1
    end = high + 1
    while True:
        start += 1
        while arr[start] < arr[middle]:
            start += 1

        end -= 1
        while arr[end] > arr[middle]:
            end -= 1

        if end <= start:
            return end

        arr[end], arr[start] = arr[start], arr[end]


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
