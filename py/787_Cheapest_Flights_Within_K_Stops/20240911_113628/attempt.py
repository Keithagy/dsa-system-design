from collections import defaultdict, deque
from typing import List


class Solution:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        """
        You want to BFS whilst tracking minimum cost for getting to the destination.
        You want to keep a visted set to avoid being stuck in cycles.
        you visit every node once, so that's O(n) time.
        You need a graph and a set for visited, so that's O(n) space >> can optimize this if we instead delete from the graph but it's O(n) anyway since you need the graph
        you also need a queue, so that's O(max( neighborCount ))
        you can keep track of stops made for each path and abandon early if exceeds k
        """
        graph = defaultdict(set)
        for [fromPort, toPort, price] in flights:
            graph[fromPort].add((toPort, price))

        min_price = float("inf")
        visited_from = [set() for _ in range(n)]
        q = deque([(src, -1, 0)])
        while q:
            (nowPort, stops, spent) = q.popleft()
            if nowPort == dst:
                min_price = min(min_price, spent)
                continue
            if stops == k:
                continue  # abandon exploration since max stops exceeded
            for optionPort, price in graph[nowPort]:
                price_if_take_option = price + spent
                if (optionPort, price_if_take_option) not in visited_from[nowPort]:
                    visited_from[nowPort].add(optionPort)
                    q.append((optionPort, stops + 1, price_if_take_option))

        return min_price if min_price != float("inf") else -1

