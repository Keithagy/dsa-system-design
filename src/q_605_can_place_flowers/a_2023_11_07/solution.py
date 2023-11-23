from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        if len(flowerbed) == 0:
            return False
        if len(flowerbed) == 1:
            return n == 1 and flowerbed[0] == 0
        for spotIdx in range(len(flowerbed)):
            if n <= 0:
                return True

            if flowerbed[spotIdx] == 1:
                continue

            if spotIdx == 0:
                if flowerbed[spotIdx + 1] == 0:
                    flowerbed[spotIdx] = 1
                    n -= 1
                continue

            if spotIdx == len(flowerbed) - 1:
                if flowerbed[spotIdx - 1] == 0:
                    flowerbed[spotIdx] = 1
                    n -= 1
                continue

            if flowerbed[spotIdx - 1] == 0 and flowerbed[spotIdx + 1] == 0:
                flowerbed[spotIdx] = 1
                n -= 1
                continue

        return n <= 0
