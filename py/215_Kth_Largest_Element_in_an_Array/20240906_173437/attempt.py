from typing import List
import heapq


class Solution:
    # you can have negative numbers
    # you must not ignore repeats
    # can you solve it without sorting?
    # sorting then couting would be O(( nlogn ))
    # is a heap considered sorting? i think it is
    # you can use a monotonic stack. to do it in n time and n space
    # nope, monotonic stack doesn't work because it relies on seeing the largest elements in order
    # using a fix sized min heap is probably your best bet with n log k and k space
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            if not heap or len(heap) < k:
                heapq.heappush(heap, num)
            else:
                if num > heap[-1]:  # should be on leaderboard
                    heapq.heapreplace(heap, num)
        return heap[0]

