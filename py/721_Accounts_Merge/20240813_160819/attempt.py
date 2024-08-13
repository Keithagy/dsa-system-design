from typing import List


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # accounts need to be merged via common email
        # suggests a need for reverse-indexing ("email" -> [occurs in these accounts])
        # every person is a collection of sublists to be merged >> enqueue sublist if it hasn't already been "in the path"
        # the "path" aspect ensures that cycles are correctly handled, if 2 sublists point to each other (e.g. if we have 2 lists that perfectly copy each other)

        return []

