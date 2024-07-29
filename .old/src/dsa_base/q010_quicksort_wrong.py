from typing import List, Tuple


def quicksort(input: List[int]) -> None:
    if len(input) <= 1:
        return
    left = 0
    right = len(input) - 1
    mid = right // 2
    index = partition(input, left, right, mid)
    quicksort_inner(input, left, index - 1)
    quicksort_inner(input, index + 1, right)


def partition(input: List[int], start_idx: int, end_idx: int, pivot_idx: int) -> int:
    pivot_value = input[pivot_idx]
    print("pivot: ", pivot_value, "index ", pivot_idx)

    lesser_subarray_end = start_idx - 1
    for i in range(start_idx, end_idx + 1):
        value = input[i]
        if value <= pivot_value:
            lesser_subarray_end += 1
            input[i], input[lesser_subarray_end] = input[lesser_subarray_end], input[i]

            if lesser_subarray_end == pivot_idx:
                pivot_idx = lesser_subarray_end
    lesser_subarray_end += 1
    input[pivot_idx], input[lesser_subarray_end] = (
        input[lesser_subarray_end],
        input[pivot_idx],
    )
    return lesser_subarray_end


def quicksort_inner(input: List[int], start_idx: int, end_idx: int):
    if len(input[start_idx:end_idx]) <= 1:
        return
    index = partition(
        input, start_idx, end_idx, start_idx + ((end_idx - start_idx) // 2)
    )
    quicksort_inner(input, start_idx, index - 1)
    quicksort_inner(input, index + 1, end_idx)


cases: List[Tuple[List[int], List[int]]] = [
    ([4, 3, 2, 1, 5], [1, 2, 3, 4, 5]),
    ([4, 7, 8, 2, 4, 3, 1], [1, 2, 3, 4, 4, 7, 8]),
    ([10, 2], [2, 10]),
    ([1], [1]),
    ([], []),
]

for input, expected in cases:
    print("Input: ", input)
    quicksort(input)
    print("Result: ", input)
    print("Expected: ", expected)
    print("Pass: ", input == expected)
