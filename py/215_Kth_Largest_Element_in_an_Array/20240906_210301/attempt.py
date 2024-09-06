import random
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quickSelect(left: int, right: int) -> int:
            pivot_idx = random.randint(left, right)  # choose random pivot
            pivot = nums[pivot_idx]  # store it for comparison later
            nums[right], nums[pivot_idx] = nums[pivot_idx], nums[right]  # swap to right

            store_idx = (
                left  # start writing the less-than-pivot partition from the left
            )
            for i in range(left, right):  # iterate through list
                if (
                    nums[i] < pivot
                ):  # less than pivot, so swap it down to the end of the partition, then increment the partiion
                    nums[store_idx], nums[i] = nums[i], nums[store_idx]
                    store_idx += 1
                # implicit: if encounter a larger-than-pivot number, i races ahead of the partition
            nums[store_idx], nums[right] = (
                nums[right],
                nums[store_idx],
            )  # swap in the rightmost number (the pivot) at the partition idx, because everything behind the partition is less than the pivot
            if (
                len(nums) - store_idx < k
            ):  # you're further up the leaderboard than you need to be
                return quickSelect(
                    left, store_idx - 1
                )  # look into the partition, down the leaderboard
            if (
                len(nums) - store_idx > k
            ):  # you're lower down the leaderboard than you need to be
                return quickSelect(
                    store_idx + 1, right
                )  # look beyond the partition, up the leaderboard

            return nums[store_idx]  # the pivot you chose happens to be the kth largest

        return quickSelect(0, len(nums) - 1)

