from typing import List


class Solution:
    # initial hunch: you have 2 alternating subseries to choose from, odds or evens
    # sum(odds) + sum(evens) == sum(nums)
    # but what about [100,1,2,200]?
    # in this case you actually want to "switch tracks"
    # each switch would come with an opp cost, because you forgo the next a to get the rest of b
    # (unless you switch tracks yet again)
    # simplest solution is probably a backtracking one
    # you explore every valid permutation of take/skip, and track largest value
    # only test largest value at the end of the list
    # return largest observed value at the end
    # actually, we want DP for this, which gives us O(n) time
    # backtracking would be n^2

    # [100,1,2,200]
    def rob(self, nums: List[int]) -> int:
      # {
      #
      # }
      memo = {}

      # idx 0, amount 0 >> 300
          # idx 2, amount 100 >> 300
              # idx 4, amount 102 >> 102
              # idx 3, amount 100 >> 300
                # idx 4, amount 300 >> 300
                # idx 5, amount 100 >> 100
          # idx 1, amount 0 >> ...
      def dp(idx:int)->int:
        if idx >= len(nums):
          return 0
        if (idx) in memo:
          return memo[idx]
        take = dp(idx+2) + nums[idx]
        skip = dp(idx+1)
        memo[idx] =max(take, skip)
        return memo[idx]
      return dp(0)
