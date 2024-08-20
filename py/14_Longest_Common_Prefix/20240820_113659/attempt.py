from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        term_idx = len(strs[0])  # exclusive
        for s in strs[1:]:
            term_idx = min(term_idx, len(s))
            for i in range(term_idx):
                if s[i] == strs[0][i]:
                    continue
                term_idx = i
                break
        return strs[0][:term_idx]

