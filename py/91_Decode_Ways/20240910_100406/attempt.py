from collections import abc


class Solution:
    # Your mapping keys run from "1" to "26"
    # implies at each step you can only ever choose to consume 1, or 2
    # you can check 1 and 2 individually -> if both none at any point, then you just return 0
    # this is a backtracking approach. You only need to worry about ways to group
    # at each step you have at worst 2 choices, which means you have 2 ^ n runtime.
    # you can definitely memoize this. You can always know that trying to decode "06" always gives 0, and trying to decode "115" has 3 possible groupings
    def numDecodings(self, s: str) -> int:
        valid_keys = set([str(i) for i in range(1, 27)])

        memo = {}

        def inner(s: str) -> int:
            if not s:
                return 1  # you can never have empty input s, so this indicates you have reached the end of a valid grouping.
            if s in memo:
                return memo[s]
            first_c = s[0]
            ways_if_consume_one = 0
            if first_c in valid_keys:
                ways_if_consume_one = inner(s[1:])
            first_two_c = s[:2] if len(s) >= 2 else ""
            ways_if_consume_two = 0
            if first_two_c in valid_keys:
                ways_if_consume_two = inner(s[2:])
            memo[s] = ways_if_consume_one + ways_if_consume_two
            return memo[s]

        return inner(s)

