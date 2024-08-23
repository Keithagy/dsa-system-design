from collections import defaultdict, deque
from typing import List
from typing_extensions import Set


class Solution:
    # each list is headed by the name of the account owner
    #   owner names might clash e.g. multiple "johns"
    # each list tail is emails
    #   if an email appears in two lists, suggests both those lists belong to the same person
    #   however, as mentioend earlier just because names are same doesn't mean they are the same person
    # return list of lists where head is name and tail is accounts
    #
    # input: [["John", "abc@xyz.com"], ["John", "123@abc.com"]]
    # out: [["John", "abc@xyz.com"], ["John", "123@abc.com"]]
    #
    # input: [["John", "abc@xyz.com", "123@abc.com"], ["John", "123@abc.com", "xcv@xcv.com"], ["Polly", "hello@123.com"]]
    # out: [["John", "abc@xyz.com", "123@abc.com", "xcv@xcv.com"], ["Polly", "hello@123.com"]]
    #
    # - email addresses can be visuazlied as a graph
    # - where email address values overlap, then they point to the same node
    # - tempting to incorporate the names into the graph, but that could make it difficult to avoid merging names on the basis that they have the same name
    # - probably good to handle the names via a lookup
    #
    # - approach
    # for each list, build the reverse lookup where key is email and value is name
    # also instantiate the nodes in the email graph (this should be undirected)
    # you will then get a graph with "islands" (each island belongs in the same list)
    # traverse each island to build the merged email list, then add to the front the name for the emails
    # when traversing, add to a visited set
    # that would allow you to find new islands to traverse by checking if that node is already in the visited set
    #
    # time complexity >> O(n) for graph building, O(m) for lookup building, O(n) for graph traversal, where n is number of emails and m is number of names
    # space complexity >> O(n) for the graph, O(n) for the lookup hashmap, O(n) for the final result nested list
    # should be linear time and space overall
    #
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        reverse_lookup = {}  # {"abc@xyz.com": "John", "123@abc.com": "John"}
        graph = defaultdict(
            set
        )  # {"abc@xyz.com": {"abc@xyz.com"}, "123@abc.com": {"123@abc.com"}}
        for acc_list in accounts:  # [["John", "abc@xyz.com"], ["John", "123@abc.com"]]
            match acc_list:
                case [name, *emails]:  # name = "John", emails = ["123@abc.com"]
                    for email in emails:
                        reverse_lookup[email] = name
                        graph[emails[0]].add(email)
                        graph[email].add(emails[0])
        visited = set()
        result = []

        def dfs(account: str, merged: Set[str]) -> None:
            if account in visited:
                return
            visited.add(account)
            merged.add(account)
            for next in graph[account]:
                dfs(next, merged)

        for account in graph:  # {"abc@xyz.com",
            if account not in visited:
                merged = set()
                dfs(account, merged)
                result.append([reverse_lookup[account]] + sorted(merged))
        return result

