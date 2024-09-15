from typing import List


class Solution:
    # you can binary search for the smallest idx such that nums[i] - x > = 0
    # because earliest idx is smaller, difference is more negative
    # then you can walk out the window from there
    # but, the idx you find might be exact (in the case that it is closest), or it might be 1 left (in the case that the last element to be smaller than target is actually closest)
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left, right = 0, len(arr) - 1

        def predicate(idx: int) -> bool:
            return arr[idx] >= x

        def findCloser(a: int, b: int) -> int:
            mod_a_diff, mod_b_diff = abs(a - x), abs(b - x)
            if mod_a_diff < mod_b_diff or mod_a_diff == mod_b_diff and a < b:
                return a
            return b

        while left < right:
            mid = left + ((right - left) // 2)
            if predicate(mid):
                right = mid
            else:
                left = mid + 1

        left = (
            left - 1
            if left - 1 >= 0 and findCloser(arr[left], arr[left - 1]) == arr[left - 1]
            else left
        )

        right = left

        while (right - left + 1) < k:
            next_left, next_right = left - 1, right + 1
            next_closest = None
            if next_right >= len(arr):
                next_closest = next_left
            elif next_left < 0:
                next_closest = next_right
            else:
                next_closest = (
                    next_left
                    if findCloser(arr[next_left], arr[next_right]) == arr[next_left]
                    else next_right
                )
            if next_closest == next_left:
                left = next_left
            else:
                right = next_right

        return arr[left : right + 1]
