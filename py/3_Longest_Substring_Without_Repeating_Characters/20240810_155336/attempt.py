from typing import Dict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen_pos: Dict[str, int] = {}
        start = 0
        max_length = 0
        for i in range(len(s)):
            c = s[i]
            if c in last_seen_pos and last_seen_pos[c] >= start:
                # we have seen this character before, so we move `start`
                start = last_seen_pos[c] + 1
            length = i - start + 1
            max_length = max(length, max_length)
            last_seen_pos[c] = i
        return max_length

