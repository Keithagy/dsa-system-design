from typing import List


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        def lexNumbers(soFar: int) -> List[int]:
            if soFar > n:
                return []
            result = [soFar]
            for i in range(10):
                result.extend(lexNumbers((soFar * 10) + i))
            return result

        result = []
        for j in range(1, 10):
            result.extend(lexNumbers(j))
        return result

