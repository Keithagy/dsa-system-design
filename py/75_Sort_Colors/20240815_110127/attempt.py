from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def quicksort(low: int, high: int) -> None:
            if not low < high:
                return

            def partition(low: int, high: int) -> int:
                pivot = nums[low + ((high - low) // 2)]
                low -= 1
                high += 1
                while low < high:
                    low += 1
                    while nums[low] < pivot:
                        low += 1
                    high -= 1
                    while nums[high] > pivot:
                        high -= 1
                    if low < high:
                        nums[low], nums[high] = nums[high], nums[low]
                return high  # the partition index is where low and high meet

            part_idx = partition(low, high)
            quicksort(low, part_idx)
            quicksort(part_idx + 1, high)

        quicksort(0, len(nums) - 1)
