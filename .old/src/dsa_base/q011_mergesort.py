from typing import List, Tuple


def mergesort(input: List[int]) -> List[int]:
    if len(input) <= 1:
        return input

    middle = len(input) // 2
    left_sub = mergesort(input[0:middle])
    right_sub = mergesort(input[middle : len(input)])
    return merge(left_sub, right_sub)


def merge(left_sub: List[int], right_sub: List[int]) -> List[int]:
    result = []
    i = 0
    j = 0
    while i < len(left_sub) and j < len(right_sub):
        left_val = left_sub[i]
        right_val = right_sub[j]
        smaller = min(left_val, right_val)
        if smaller == left_val:
            result.append(smaller)
            i += 1
        if smaller == right_val:
            result.append(smaller)
            j += 1

    if i < len(left_sub):
        result += left_sub[i : len(left_sub)]
    if j < len(right_sub):
        result += right_sub[j : len(right_sub)]
    return result


cases: List[Tuple[List[int], List[int]]] = [
    ([4, 3, 2, 1, 5], [1, 2, 3, 4, 5]),
    ([4, 7, 8, 2, 4, 3, 1], [1, 2, 3, 4, 4, 7, 8]),
    ([10, 2], [2, 10]),
    ([1], [1]),
    ([], []),
]

for input, expected in cases:
    print("Input: ", input)
    result = mergesort(input)
    print("Result: ", result)
    print("Expected: ", expected)
    print("Pass: ", result == expected)
