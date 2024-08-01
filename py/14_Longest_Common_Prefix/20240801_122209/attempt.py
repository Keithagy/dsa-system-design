from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lcp = strs[0]
        for s in strs[1:]:
            shorter = lcp if len(lcp) < len(s) else s
            for i in range(len(shorter)):
                test = shorter[i]
                if lcp[i] == test and s[i] == test:
                    continue
                else:
                    shorter = shorter[:i]
                    break
            lcp = shorter
        return lcp

