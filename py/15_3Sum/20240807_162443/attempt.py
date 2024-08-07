from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        deduped_triplets = set()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    sum = nums[i] + nums[j] + nums[k]
                    if sum == 0:
                        frequencies = {}
                        for num in [nums[i], nums[j], nums[k]]:
                            frequencies[num] = frequencies.setdefault(num, 0) + 1
                        if frozenset(frequencies) not in deduped_triplets:
                            deduped_triplets.add(frozenset(frequencies.items()))
        result = []
        for triplet in deduped_triplets:
            answer = []
            for num, freq in triplet:
                for _ in range(freq):
                    answer.append(num)

            result.append(answer)
        return result
