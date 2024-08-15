from typing import Dict, List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo: Dict[str, bool] = {}
        words = set(wordDict)

        def inner(s) -> bool:
            if s in memo:
                return memo[s]
            # compare up to full string
            for end in range(len(s) + 1):  # candidate subsetting is end-exclusive
                candidate = s[:end]
                if candidate not in words:
                    continue
                left_over = s[end:]
                if left_over == "" or inner(left_over):
                    memo[candidate] = True
                    return True
            # don't need this part. If "leetcode" matches "leet", "code" automatically gets checked in the recusive call.
            # for start in range(len(s)):
            #     candidate = s[start:]
            #     if candidate not in words:
            #         continue
            #     left_over = s[:start]
            #     if left_over == "" or inner(left_over):
            #         memo[candidate] = True
            #         return True
            memo[s] = False
            return False

        return inner(s)

    # Let's consider inputs:
    # s = "hello", wordDict = ["apple","pen"]
    #   Here, you iterate through the string and you check "h", "he", "hel", ..., "hello", "ello", "llo", ..., "o", and you see that there is no match. return False
    # s = "apple", wordDict = ["apple","pen"]
    #   Here, you do the same as before, you get a match at "apple", and you don't have any other letters unaccounted for. return True
    # s = "applepenapple", wordDict = ["apple","pen"]
    #   Here, you get to apple, then you segment, and you recusively call on penapple, which matches pen, then you recursively call on apple. return True, implying and operation between recursive calls
    # s = "ohapple", wordDict = ["apple","pen"]
    #   Here, you get to apple, then you, then you segment, and you recursively call on "oh", which is equivalent to the case of calling on "hello"
    # notice that the solution comes from calling the same operation on a subproblem >> e.g. if input is "ohoh", wordDict contains "oh". Or if input is "appohle", and segmenting gives you app,oh,le, and you have already checked app.
    # Opportunity to memoize
    # Solution would be O(n^2) in python since we are making copies of substrings (linear-complexity operation) for comparison up to n times.

