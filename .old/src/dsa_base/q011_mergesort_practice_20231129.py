from typing import List, Tuple


def mergesort(input: List[int]) -> List[int]:
    if len(input) <= 1:
        return input
    middle = len(input) // 2
    left_sub = mergesort(input[:middle])
    right_sub = mergesort(input[middle:])
    return merge(left_sub, right_sub)


def merge(left_sub: List[int], right_sub: List[int]) -> List[int]:
    result = []
    left_i = 0
    right_i = 0

    while left_i < len(left_sub) and right_i < len(right_sub):
        left_val = left_sub[left_i]
        right_val = right_sub[right_i]

        smaller_val = min(left_val, right_val)
        if smaller_val == left_val:
            result.append(left_val)
            left_i += 1

        if smaller_val == right_val:
            result.append(right_val)
            right_i += 1
    if left_i == len(left_sub) and right_i == len(right_sub):
        return result
    if left_i < len(left_sub):
        result.extend(left_sub[left_i:])
        return result
    result.extend(right_sub[right_i:])
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
