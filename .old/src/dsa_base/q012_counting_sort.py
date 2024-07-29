from typing import List, Tuple


def counting_sort(input: List[int]) -> List[int]:
    if len(input) <= 1:
        return input
    min_v, max_v = min(input), max(input)
    buckets = [0] * (max_v - min_v + 1)
    for num in input:
        bucket_no = num - min_v
        buckets[bucket_no] += 1

    result = []
    for bucket_no in range(len(buckets)):
        value = bucket_no + min_v
        count = buckets[bucket_no]
        result.extend([value] * count)

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
    result = counting_sort(input)
    print("Result: ", result)
    print("Expected: ", expected)
    print("Pass: ", result == expected)
