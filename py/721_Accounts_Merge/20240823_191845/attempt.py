from collections import defaultdict
from typing import List, Set


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        reverse_lookup = {}
        graph = defaultdict(set)
        for account in accounts:
            name = account[0]
            for email in account[1:]:
                reverse_lookup[email] = name
                graph[email].add(account[1])
                graph[account[1]].add(email)

        visited = set()
        result = []

        def dfs(email: str, merged: Set[str]) -> None:
            if email in visited:
                return
            visited.add(email)
            merged.add(email)
            for neighbor in graph[email]:
                dfs(neighbor, merged)

        for email in graph:
            if email not in visited:
                merged = set()
                dfs(email, merged)
                result.append([reverse_lookup[email]] + sorted(merged))

        return result

