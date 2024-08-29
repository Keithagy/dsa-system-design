from collections import defaultdict
from typing import Dict, List


class Solution:
    # initial thought is to use a hash map to keep indexes
    # question would be whether Counters are hashable
    # if they aren't, i can sort the characters and match them on that basis
    # each sort would be s log s, where s is the length of the string
    # n * slogs
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupings: Dict[str, List[str]] = defaultdict(list)
        for s in strs:
            k = "".join(sorted(s))
            groupings[k].append(s)
        return list(groupings.values())

