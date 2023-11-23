from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # You can solve this by iterating through candies twice
        # Once to identify the largest element (since candies is not ordered)
        # One to identify if candies[i] + extraCandies is greater than the largest element

        most_candies: int = 0  # candies[i] >= 1
        for count in candies:
            most_candies = max(most_candies, count)

        result: List[bool] = []
        for count in candies:
            result.append(count + extraCandies >= most_candies)

        return result
