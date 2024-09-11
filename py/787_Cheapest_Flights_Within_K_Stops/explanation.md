## Explanation: Cheapest Flights Within K Stops

### Analysis of problem & input data

This problem is a variation of the shortest path problem in a weighted graph, with an additional constraint on the number of stops. The key characteristics of this problem are:

1. Directed graph: The flights form a directed graph where cities are nodes and flights are edges.
2. Weighted edges: Each flight has a cost (price) associated with it.
3. Limited stops: We need to find the cheapest path with at most K stops.
4. Single source, single destination: We're looking for a path from a specific source to a specific destination.

The key principle that makes this question simpler is understanding that it's a variation of Dijkstra's algorithm or Bellman-Ford algorithm, but with a twist. Instead of finding the shortest path, we're finding the cheapest path with a constraint on the number of stops.

This problem can be solved using various approaches:

1. Breadth-First Search (BFS) with pruning
2. Bellman-Ford algorithm (with modifications)
3. Dijkstra's algorithm (with modifications)

The optimal solution for this problem typically involves a dynamic programming approach or a modified version of the Bellman-Ford algorithm, as it needs to consider both the cost and the number of stops.

### Test cases

1. Basic case: As given in Example 1
2. No possible route: When there's no valid path from src to dst within K stops
3. Direct flight is cheapest: When the direct flight (if exists) is the cheapest option
4. Maximum stops utilized: When the cheapest path uses exactly K stops
5. Large graph with multiple possible paths
6. Graph with cycles
7. Graph where cheapest path exceeds K stops

Here's a Python code to set up these test cases:

```python
def test_cheapest_flights():
    # Function to be implemented
    def find_cheapest_price(n, flights, src, dst, k):
        pass  # Implementation here

    # Test case 1: Basic case
    assert find_cheapest_price(4, [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], 0, 3, 1) == 700

    # Test case 2: No possible route
    assert find_cheapest_price(3, [[0,1,100],[1,2,100]], 0, 2, 0) == -1

    # Test case 3: Direct flight is cheapest
    assert find_cheapest_price(3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 1) == 500

    # Test case 4: Maximum stops utilized
    assert find_cheapest_price(5, [[0,1,100],[1,2,100],[2,3,100],[3,4,100],[0,4,1000]], 0, 4, 3) == 400

    # Test case 5: Large graph with multiple possible paths
    large_graph = [[0,1,100],[0,2,500],[1,2,100],[1,3,600],[2,3,200],[2,4,400],[3,4,100],[4,5,100]]
    assert find_cheapest_price(6, large_graph, 0, 5, 2) == 700

    # Test case 6: Graph with cycles
    cyclic_graph = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
    assert find_cheapest_price(4, cyclic_graph, 0, 3, 2) == 400

    # Test case 7: Graph where cheapest path exceeds K stops
    assert find_cheapest_price(6, large_graph, 0, 5, 1) == -1

    print("All test cases passed!")

test_cheapest_flights()
```

### Solutions

#### Overview of solution approaches

##### Solutions worth learning

1. Bellman-Ford Algorithm (Neetcode solution)
2. Breadth-First Search (BFS) with Queue
3. Dijkstra's Algorithm with Priority Queue

Count: 3 solutions (1 Neetcode solution)

##### Rejected solutions

1. Depth-First Search (DFS): While DFS can work, it's not optimal for this problem as it doesn't guarantee finding the cheapest path first and may explore unnecessary paths.
2. Floyd-Warshall Algorithm: This algorithm finds the shortest paths between all pairs of vertices, which is overkill for this problem and has a higher time complexity.

#### Worthy Solutions

##### Bellman-Ford Algorithm (Neetcode solution)

```python
from typing import List

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Initialize prices array with infinity for all cities except src
        prices = [float('inf')] * n
        prices[src] = 0

        # Iterate k+1 times (allowing for k stops)
        for i in range(k + 1):
            # Create a copy of prices to store updated values
            tmp_prices = prices.copy()

            # For each flight, update the price if a cheaper route is found
            for s, d, p in flights:  # s: source, d: destination, p: price
                if prices[s] == float('inf'):
                    continue
                if prices[s] + p < tmp_prices[d]:
                    tmp_prices[d] = prices[s] + p

            # Update prices for the next iteration
            prices = tmp_prices

        # Return the price to destination, or -1 if not reachable
        return prices[dst] if prices[dst] != float('inf') else -1
```

Time Complexity: O(K \* E), where K is the number of stops and E is the number of flights (edges).
Space Complexity: O(N), where N is the number of cities (nodes).

Explanation:

- We iterate K+1 times, as we're allowed K stops (which means K+1 flights).
- In each iteration, we consider all flights and update the prices if a cheaper route is found.
- This approach is based on the principle of relaxation in the Bellman-Ford algorithm.
- We use a temporary array `tmp_prices` to avoid using updated prices within the same iteration.

Key intuitions and invariants:

- After i iterations, `prices[j]` represents the cheapest price to reach city j using at most i flights.
- We don't need to track the actual path, only the minimum price.
- The algorithm terminates after K+1 iterations, ensuring we don't exceed the stop limit.

##### Breadth-First Search (BFS) with Queue

```python
from typing import List
from collections import defaultdict, deque

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Create adjacency list representation of the graph
        graph = defaultdict(list)
        for s, d, p in flights:
            graph[s].append((d, p))

        # Initialize queue with (node, price, stops)
        queue = deque([(src, 0, k + 1)])

        # Keep track of minimum price to reach each node
        min_price = [float('inf')] * n

        while queue:
            curr, price, stops = queue.popleft()

            # If we've reached the destination, return the price
            if curr == dst:
                return price

            # If we've run out of stops or found a more expensive route, skip
            if stops == 0 or price >= min_price[curr]:
                continue

            # Update minimum price for current node
            min_price[curr] = price

            # Explore neighbors
            for neighbor, cost in graph[curr]:
                queue.append((neighbor, price + cost, stops - 1))

        # If we can't reach the destination within k stops, return -1
        return -1 if min_price[dst] == float('inf') else min_price[dst]
```

Time Complexity: O(N \* K), where N is the number of cities and K is the number of stops.
Space Complexity: O(N \* K) for the queue in the worst case.

Explanation:

- We use BFS to explore all possible routes within the given number of stops.
- The queue stores tuples of (current city, cumulative price, remaining stops).
- We keep track of the minimum price to reach each city to avoid exploring more expensive routes.

Key intuitions and invariants:

- BFS ensures we explore routes with fewer stops before those with more stops.
- By tracking minimum prices, we can prune more expensive routes early.
- The algorithm terminates when we reach the destination or explore all possible routes within K stops.

##### Dijkstra's Algorithm with Priority Queue

```python
from typing import List
import heapq
from collections import defaultdict

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Create adjacency list representation of the graph
        graph = defaultdict(list)
        for s, d, p in flights:
            graph[s].append((d, p))

        # Initialize priority queue with (price, node, stops)
        pq = [(0, src, k + 1)]

        # Keep track of minimum price and stops to reach each node
        best = {}

        while pq:
            price, node, stops = heapq.heappop(pq)

            # If we've reached the destination, return the price
            if node == dst:
                return price

            # If we've run out of stops, skip
            if stops == 0:
                continue

            # If we've found a more expensive or longer route, skip
            if node in best and (price > best[node][0] or stops < best[node][1]):
                continue

            # Update best price and stops for current node
            best[node] = (price, stops)

            # Explore neighbors
            for neighbor, cost in graph[node]:
                heapq.heappush(pq, (price + cost, neighbor, stops - 1))

        # If we can't reach the destination within k stops, return -1
        return -1
```

Time Complexity: O((N + E) _log(N_ K)), where N is the number of cities, E is the number of flights, and K is the number of stops.
Space Complexity: O(N \* K) for the priority queue and best dictionary in the worst case.

Explanation:

- We use Dijkstra's algorithm with a priority queue to explore routes in order of increasing price.
- The priority queue stores tuples of (cumulative price, current city, remaining stops).
- We keep track of the best (price, stops) combination for each city to avoid exploring suboptimal routes.

Key intuitions and invariants:

- Dijkstra's algorithm ensures we explore cheaper routes before more expensive ones.
- By tracking both price and stops, we can handle the stop constraint effectively.
- The algorithm terminates when we reach the destination or explore all possible routes within K stops.

#### Rejected Approaches

1. Depth-First Search (DFS):

   - While DFS can find all possible paths, it's not efficient for this problem because:
     a) It doesn't guarantee finding the cheapest path first.
     b) It may explore unnecessary paths, leading to higher time complexity.
   - DFS is more suitable for problems where we need to find all possible paths or when the graph is very deep.

2. Floyd-Warshall Algorithm:

   - This algorithm finds the shortest paths between all pairs of vertices, which is overkill for this problem.
   - It has a time complexity of O(N^3), which is inefficient when we only need to find the path between two specific nodes.
   - It doesn't directly handle the constraint on the number of stops.

3. Basic Dijkstra's Algorithm without stop constraint:
   - While Dijkstra's algorithm is efficient for finding the shortest path, it doesn't inherently handle the stop constraint.
   - Without modification, it might find a cheaper path that exceeds the allowed number of stops.

#### Final Recommendations

For this problem, I recommend learning and implementing the Bellman-Ford Algorithm (Neetcode solution) for the following reasons:

1. Simplicity: It's relatively easy to understand and implement.
2. Efficiency: It handles the stop constraint naturally and has a good time complexity of O(K \* E).
3. Adaptability: The concept can be applied to similar problems with different constraints.

The BFS and modified Dijkstra's solutions are also worth understanding as they provide different perspectives on solving graph problems with constraints. They can be more efficient in certain scenarios, especially when the graph is sparse or when you need to find the cheapest path for multiple destinations.

### Visualization(s)

For this problem, a visual representation of how the Bellman-Ford algorithm works on a sample graph would be helpful. Here's a simple SVG visualization:

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 400">
  <!-- Cities -->
  <circle cx="100" cy="200" r="30" fill="lightblue" stroke="black" stroke-width="2"/>
  <text x="100" y="205" text-anchor="middle" font-size="20">A</text>

  <circle cx="300" cy="100" r="30" fill="lightblue" stroke="black" stroke-width="2"/>
  <text x="300" y="105" text-anchor="middle" font-size="20">B</text>

  <circle cx="300" cy="300" r="30" fill="lightblue" stroke="black" stroke-width="2"/>
  <text x="300" y="305" text-anchor="middle" font-size="20">C</text>

  <circle cx="500" cy="200" r="30" fill="lightblue" stroke="black" stroke-width="2"/>
  <text x="500" y="205" text-anchor="middle" font-size="20">D</text>

  <circle cx="700" cy="200" r="30" fill="lightgreen" stroke="black" stroke-width="2"/>
  <text x="700" y="205" text-anchor="middle" font-size="20">E</text>

  <!-- Flights -->
  <line x1="130" y1="190" x2="270" y2="110" stroke="black" stroke-width="2"/>
  <text x="200" y="130" text-anchor="middle" font-size="16">100</text>

  <line x1="130" y1="210" x2="270" y2="290" stroke="black" stroke-width="2"/>
  <text x="200" y="270" text-anchor="middle" font-size="16">500</text>

  <line x1="330" y1="100" x2="470" y2="190" stroke="black" stroke-width="2"/>
  <text x="400" y="130" text-anchor="middle" font-size="16">200</text>

  <line x1="330" y1="300" x2="470" y2="210" stroke="black" stroke-width="2"/>
  <text x="400" y="270" text-anchor="middle" font-size="16">100</text>

  <line x1="530" y1="200" x2="670" y2="200" stroke="black" stroke-width="2"/>
  <text x="600" y="190" text-anchor="middle" font-size="16">150</text>

  <!-- Legend -->
  <text x="50" y="50" font-size="18" font-weight="bold">Legend:</text>
  <circle cx="70" cy="80" r="10" fill="lightblue" stroke="black" stroke-width="2"/>
  <text x="90" y="85" font-size="16">City</text>
  <circle cx="70" cy="110" r="10" fill="lightgreen" stroke="black" stroke-width="2"/>
  <text x="90" y="115" font-size="16">Destination</text>
</svg>

```

This visualization shows a sample graph with 5 cities (A to E) and the flights between them. The numbers on the edges represent the flight costs. City A is the source, and City E is the destination. The Bellman-Ford algorithm would iterate through this graph, updating the minimum costs to reach each city while respecting the stop constraint.
