from typing import List


class Solution:
    # at least element in the array, you can either take or skip that element
    # if you take the element, you stay on that element
    # if you skip, you move on to the next
    # you can prune the call graph by returning early upon hitting the target (cannot take or skip fruther from this position)
    # for each element, you can take or skip >> 2 decisions
    # n elements
    # So runtime is O(2^n) (exponentional)
    # is there a way to reuse calculations from subarrays?
    # nums [1,2,3], target = 4
    # consider [1]
    #   >> (1,1,1,1)
    # >> 1
    # consider [1,2]
    #   >> (1,1,1,1)
    #   >> (1,1,2) (can add 1 way by subbing 2 `1`s)
    #   >> (2,2) (can sub more `1`s)
    #   >> (1,2,1) (you can sub in between)
    # I don't see a way to easily compute the same function with a sub array without repeating, actually.
    # unless the dp is for the inner function that says you have a certain amount and you want to add a certain quantity to it
    # e.g. for all subarrays leading up to the full array you will need to calc add(1,0).
    #
    # [1,2] target 4 (len 2)
    #   0,0
    #       take => 0,1
    #           take => 0,2
    #               take => 0,3
    #                   take => 0,4
    #                           >> 1
    #                   skip => 1,3
    #                        take => 1,5
    #                               >> 0
    #                        skip => 2,3
    #                               >> 0
    #                        >> 0
    #                   >> 1
    #               >> 1
    #
    #
    #
    #
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = {}

        def ways_to_add_to_target(idx: int, amount: int) -> int:
            if idx >= len(nums) or amount > target:
                return 0  # no ways to add to target
            if amount == target:
                return 1  # you have found a way to add to target
            if (idx, amount) in memo:
                return memo[(idx, amount)]

            ways_if_add = 0
            for j in range(len(nums)):
                ways_if_add += ways_to_add_to_target(j, amount + nums[j])
            memo[(idx, amount)] = ways_if_add
            return memo[(idx, amount)]

        return ways_to_add_to_target(0, 0)

