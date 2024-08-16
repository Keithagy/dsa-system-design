from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        memo = {}
        words = set(wordDict)

        def canBreak(s: str) -> bool:
            print(s)
            if s == "":
                return True
            if s in memo:
                return memo[s]
            for i in range(len(s)):
                if canBreak(s[:i]) and s[i:] in words:
                    memo[s] = True
                    return True
            memo[s] = False
            return False

        result = canBreak(s)
        print(memo)
        return result

