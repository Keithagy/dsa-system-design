from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lcp_terminal_idx = len(strs[0])
        for s in strs:
            lcp_terminal_idx = min(lcp_terminal_idx, len(s))
            for i in range(lcp_terminal_idx):
                if strs[0][i] != s[i]:
                    lcp_terminal_idx = i
                    break
            if lcp_terminal_idx == 0:
                break
        return strs[0][:lcp_terminal_idx]

