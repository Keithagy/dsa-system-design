from typing import List


class Solution:
    # input : n = 2
    # output: ["(())","()()"]

    # I believe this is a backtracking algo which relies on the fact that for every nth set of parens
    # all you need to do is explore the case where you nest the next, and where you don't nest
    # solution is accordingly O(2^(n-1)-1), since you fork 2 ways n times, and you don't have the option of nesting the first
    # whether you nest or not, you always find and operate on the most recent set of parens
    def generateParenthesis(self, n: int) -> List[str]:
        path = ["(", ")"]
        result = []

        def dfs(i: int, insertIdx: int) -> None:
            if i == n:
                result.append("".join(path))
                return
            # nest next
            path.insert(insertIdx, "(")
            path.insert(insertIdx + 1, ")")
            dfs(i + 1, insertIdx + 1)
            path.pop(insertIdx)
            path.pop(insertIdx)

            # don't nest
            path.insert(insertIdx + 1, "(")
            path.insert(insertIdx + 2, ")")
            dfs(i + 1, insertIdx + 2)
            path.pop(insertIdx + 1)
            path.pop(insertIdx + 1)

        dfs(1, 1)
        return result

