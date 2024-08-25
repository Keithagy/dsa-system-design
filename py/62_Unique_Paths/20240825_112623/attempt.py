class Solution:
    # number of ways to get to a different square
    # given by number of ways to get to square above
    # + number of ways to get to square to left
    # it's always 1 unique path (no) actions to get to 0,0
    # then, calculating (0,1) and (1,0) from there is O(1)
    # you need to repeat that mxn times to get to (m,n)
    # so runtime complexity is O(mxn)
    # space complexity is O(mxn) because you need to save each step
    # (maybe there is possibility to use only 1d array? we can explore this if there is time)
    def uniquePaths(self, m: int, n: int) -> int:

        memo = {}

        # m 1
        # n 2
        #
        #
        # r 1
        # c 2
        #       r 1
        #       c 1
        # return 1
        #
        # m 2
        # n 1
        #
        # r 2
        # c 1
        #       r 1
        #       c 1
        #
        # m 2
        # n 2
        #
        # r 2
        # c 2
        #       r 1
        #       c 2
        #
        #       r 2
        #       c 1
        def waysTo(r: int, c: int) -> int:
            if r == 1 and c == 1:
                return 1
            if (r, c) in memo:
                return memo[(r, c)]
            result = 0
            if 2 <= r:
                result += waysTo(r - 1, c)
            if 2 <= c:
                result += waysTo(r, c - 1)
            memo[(r, c)] = result
            return memo[(r, c)]

        return waysTo(m, n)

