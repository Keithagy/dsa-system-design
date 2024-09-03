from typing import List
from collections import deque


class Solution:
    # Key observation: x does not have to be an actual element in the List
    # in fact, it can be out of bounds
    # so what we need is to find the closest idx that gives us x
    # when applying binary search, we can apply the predicate:
    # arr[idx] >= x
    # so, left gives smallest idx s.t predicate is true
    # so, it can be larger, or it can be smaller.
    # either way, left and right both start pointing at the same element, and then you can walk out from that element
    # and add the one which gives a smaller mod(diff)
    #
    # O(nlogn) time for the binary search, O(k) comparisons thereafter
    # O(1) space for binary search, O(k) space for result
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left, right = 0, len(arr) - 1

        def predicate(idx: int) -> bool:
            return arr[idx] >= x

        while left < right:
            mid = left + ((right - left) // 2)
            if predicate(mid):
                right = mid
            else:
                left = mid + 1

        def diffAbs(candidate: int) -> int:
            return abs(candidate - x)

        if 1 <= left < len(arr) and diffAbs(arr[left - 1]) <= diffAbs(arr[left]):
            left = right = left - 1

        result = deque()

        while len(result) != k:
            if right > len(arr) - 1:
                result.appendleft(arr[left])
                left -= 1
                continue
            if left < 0:
                result.append(arr[right])
                right += 1
                continue
            a, b = diffAbs(arr[left]), diffAbs(arr[right])
            if a <= b:
                # left is closer
                # also handles case where absdiff is equal but a < b, since we have a sorted list
                result.appendleft(arr[left])
                if left == right:
                    right += 1
                left -= 1
                continue
            result.append(arr[right])
            right += 1
        return list(result)

