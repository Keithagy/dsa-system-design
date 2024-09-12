from typing import List


class Solution:
    # you need a modified binary search.
    # You want the smallest i s.t nums[i] < nums[i+1]
    # Consider: [1,2,4,5,6,7,0]
    #                  ^
    # Consider: [2,4,5,6,7,0,1]
    #                  ^
    # Consider: [4,5,6,7,0,1,2] >> both
    #                  ^
    # Consider: [5,6,7,0,1,2,4] >> both
    #                  ^
    # Consider: [6,7,0,1,2,4,5]
    #                  ^
    # You always have a sorted half,
    # and the min could be in the sorted half or not
    # you can look in the sorted half and find that in log n
    # the pivot is always the first element
    # if one is sorted and one is not, then min is in the unsorted (because that's where the wrap happens)
    #   specifically, you keep looking in the unsorted
    # if both are sorted, then you can just compare the min of left sub and min of right sub
    #
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        min_found = 5001  # larger than constraint
        while left < right:
            mid = left + ((right - left) // 2)
            min_found = min(min_found, nums[mid])
            # which half is sorted?
            if (
                nums[left] <= nums[max(mid - 1, left)]
                and nums[min(mid + 1, right)] <= nums[right]
            ):
                # both are sorted
                return min(
                    nums[left],
                    nums[min(mid + 1, right)],
                    nums[mid],
                )
            # only one half is sorted; min is in unsorted because that's where wrap happens
            # left half
            if nums[left] <= nums[max(mid - 1, left)]:
                left = mid + 1
            else:
                right = mid

        return min(min_found, nums[left])

