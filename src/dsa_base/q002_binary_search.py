from typing import List


# Assumes a sorted array, else it can't actually work
def binary_search(haystack: List[int], needle: int) -> bool:
    left, right = 0, len(haystack) - 1
    while left < right:
        mid = (right - left) // 2
        num = haystack[mid]
        if num < needle:
            left = mid + 1
        elif num > needle:
            right = mid
        return True
    return False
