class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = []
        nums.sort()
        for i in range(n - 2):
            if i > 0 and nums[i - 1] == nums[i]:
                continue  # skip duplicates, since in sorted list all equal values are adjacent
            j, k = i + 1, n - 1
            while j < k:
                sum = nums[i] + nums[j] + nums[k]
                if sum == 0:
                    result.append([nums[i], nums[j], nums[k]])
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1
                    j += 1
                    k -= 1
                elif sum < 0:
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    j += 1
                else:
                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1
                    k -= 1
        return result

