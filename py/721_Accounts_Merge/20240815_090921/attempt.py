from typing import List
from collections import defaultdict


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        graph = defaultdict(set)
        email_to_name = {}
        for account in accounts:
            name = account[0]
            hub_email = account[1]
            for email in account[1:]:
                graph[hub_email].add(email)
                graph[email].add(hub_email)
                email_to_name[email] = name

        visited = set()
        result = []

        def dfs(email: str, component: List[str]) -> None:
            visited.add(email)
            component.append(email)
            associated_emails = graph[email]
            for associated in associated_emails:
                if associated not in visited:
                    dfs(associated, component)

        for email in graph:
            if email not in visited:
                component = []
                dfs(email, component)
                result.append([email_to_name[email]] + sorted(component))
        return result

