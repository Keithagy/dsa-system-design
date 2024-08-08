from typing import List


def linearSearch(haystack: List[int], needle: int) -> bool:
    for hay in haystack:
        if hay == needle:
            return True
    return False


linearSearch([1, 2, 3], 3)
