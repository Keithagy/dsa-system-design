from typing import List


class Solution:
    # when closed == open only can add open
    # when closed == open == n, append
    # input = 3
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        path = []

        # n = 3
        # 0,0
        # |  path = [(]
        #       | 0,1
        #       | path = [((]
        #               | 0,2
        #               | path = [(((]
        #                       | 0,3
        #                       | path = [((()]
        #                               | 1,3
        #                               | path = [((())]
        #                                       | 2,3
        #                                       | path = [((()))]
        #                                               | 3,3
        #                                               | result.append
        #                                       | path = [((())]
        #                               | path = [((()]
        #                       | path = [(((]
        #               | path = [((]
        #               | path = [(()]
        #                       | 1,2
        #                       | path = [(()(]
        #                               | 1,3
        #                               | path = [(()(]
        #
        def inner(close_count: int, open_count: int) -> None:
            if close_count == open_count == n:
                result.append("".join(path))
                return

            if open_count < n:
                path.append("(")
                inner(close_count, open_count + 1)
                path.pop()

            if close_count < open_count:
                path.append(")")
                inner(close_count + 1, open_count)
                path.pop()

        inner(0, 0)
        return result

