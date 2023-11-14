from typing import List


def linear_search(haystack: List[int], needle: int) -> bool:
    for i in range(len(haystack)):
        num = haystack[i]
        if num == needle:
            return True
    return False
