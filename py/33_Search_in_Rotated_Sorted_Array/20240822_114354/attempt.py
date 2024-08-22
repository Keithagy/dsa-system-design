from typing import List, Optional


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binSrc(left: int, right: int) -> Optional[int]:
            if left >= right:
                return None if nums[left] != target else left
            mid = left + ((right - left) // 2)
            if nums[mid] == target:
                return mid
            else:
                if nums[left] <= nums[mid]:
                    if nums[left] <= target <= nums[mid]:
                        return binSrc(left, mid - 1)
                    return binSrc(mid + 1, right)
                else:
                    if nums[mid] <= target <= nums[right]:
                        return binSrc(mid + 1, right)
                    return binSrc(left, mid - 1)

        result = binSrc(0, len(nums) - 1)
        return result if result is not None else -1

