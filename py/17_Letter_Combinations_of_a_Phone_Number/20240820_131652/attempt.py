from typing import List


class Solution:
    # Variation of the permutations question
    def letterCombinations(self, digits: str) -> List[str]:
        values = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }
        dp = [
            [] for _ in range(len(digits) + 1)
        ]  # dp[i] gives possibilities for digits[:i]
        for i in range(1, len(digits) + 1, 1):
            c = digits[i - 1]
            values_for_c = values[c]
            if not dp[i - 1]:
                print(i, len(dp))
                dp[i] = values_for_c
                continue

            for c in values_for_c:
                for existing in dp[i - 1]:
                    dp[i].append(existing + c)
        return dp[-1]

