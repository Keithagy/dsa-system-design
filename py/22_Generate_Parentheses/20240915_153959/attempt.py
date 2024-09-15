from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def explore(openCount: int, closeCount: int, path: List[str]) -> None:
            if openCount == closeCount == n:
                result.append("".join(path))
                return
            if openCount < n:
                path.append("(")
                explore(openCount + 1, closeCount, path)
                path.pop()
            # you can only add close if close < open
            if closeCount < openCount:
                path.append(")")
                explore(openCount, closeCount + 1, path)
                path.pop()

        explore(0, 0, [])
        return result

