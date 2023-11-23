from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return max(nums[0], 0)
        fragments = []
        # cur_frag = (0,1,0) # start_i, end_i, net_sum
        i = 0
        while i < len(nums):
            while nums[i] >= 0:
                i +=1

            net_sum = nums[i]            
            j = i + 1
            while j < len(nums) and nums[j] >=0:
                net_sum += nums[j]
                j += 1
            fragments.append(i,j, net_sum)
            i = j

        result_start, result_end = 0,0 # implies return empty array if all negative 
        k = 0
        while k < len(fragments) and fragments[k][2] <= 0:
            k += 1
        result_start, result_end = fragments[k][0], fragments[k][1]
        k += 1
        while k < len(fragments) and fragments[k][2] >= 0:
            result_end = 
        for (start, end, net_sum) in fragments:
            if net_sum >= 0:
                result_start = result_start if result_start > 0 else start
                end
