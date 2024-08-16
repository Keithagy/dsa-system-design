from typing import List


class Solution:
    # Build up from smaller case
    # You can always break empty string
    # Breaking up "a" is just checking if "a" is in wordset.
    # From there, if you know that "a" can be broken, you can know if "ab" can be broken
    # by looking at whether "b" is in the word set.
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False for _ in range(n + 1)]  # go up until full length of word
        words = set(wordDict)
        dp[0] = True  # You can always break empty string

        for i in range(1, n + 1, 1):
            for j in range(0, i, 1):
                if dp[j] and s[j:i] in words:
                    dp[i] = True
                    break
        return dp[-1]

