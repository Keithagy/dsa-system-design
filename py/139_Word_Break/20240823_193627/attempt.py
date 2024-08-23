from typing import List


class Solution:
    # identify substring that matches, call same function on the remnant substring
    # maybe frame in terms of taking and skipping
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
        Output: false
        """

        memo = {}

        """
        "catsandog"
        cat
        sand >> False
        og >> False

        """

        def canBreak(s: str) -> bool:
            if not s:
                return True
            if s in memo:
                return memo[s]
            for word in wordDict:
                substring = s[: len(word)]
                if word == substring and canBreak(s[len(word) :]):
                    memo[s] = True
                    return memo[s]
            memo[s] = False
            return memo[s]

        return canBreak(s)

