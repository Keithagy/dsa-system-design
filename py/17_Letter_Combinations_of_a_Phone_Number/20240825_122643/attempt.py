from typing import List


class Solution:
    # this is a backtracking problem.
    # for each subsequent number, you have 3/4 choices
    # push, progress, and pop in sequence.
    # time: O(4^n) where 4 is worst case nubmer of letters and n is len digitgs
    # space: O(4^n), since it's combinatorial
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }

        def combine(idx: int, path: str) -> List[str]:
            if idx >= len(digits):
                return [path] if path else []
            result = []
            for option in mapping[digits[idx]]:
                result.extend(combine(idx + 1, path + option))
            return result

        return combine(0, "")

