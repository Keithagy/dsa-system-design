## Explanation: Pacific Atlantic Water Flow

### Analysis of problem & input data

This problem is a classic example of a graph traversal problem, specifically designed to test understanding of depth-first search (DFS) or breadth-first search (BFS) on a 2D grid. The key characteristics of this problem are:

1. 2D grid representation: The island is represented as a 2D matrix, where each cell has a height value.
2. Two-way water flow: Water can flow from higher or equal height cells to lower height cells.
3. Dual ocean connectivity: We need to find cells that can reach both oceans.
4. Edge conditions: The Pacific Ocean is accessible from the top and left edges, while the Atlantic Ocean is accessible from the bottom and right edges.

The crucial insight that simplifies this problem is to approach it from the ocean's perspective rather than from each cell. Instead of checking if water from each cell can reach both oceans, we can start from the ocean edges and find all cells that can reach each ocean separately. Then, we find the intersection of these two sets.

This problem falls into the category of "graph traversal with multiple sources" and "reverse thinking" patterns. It's similar to problems like "Surrounded Regions" or "Number of Islands", but with the added complexity of dual connectivity.

### Test cases

1. Standard case (given in Example 1)
2. Single cell island (given in Example 2)
3. All cells with the same height
4. Strictly increasing heights from top-left to bottom-right
5. Strictly decreasing heights from top-left to bottom-right
6. Checkerboard pattern with alternating heights
7. Large grid with random heights

Here's a Python implementation of these test cases:

```python
def test_pacific_atlantic():
    solution = Solution()

    # Test case 1: Standard case
    heights1 = [
        [1,2,2,3,5],
        [3,2,3,4,4],
        [2,4,5,3,1],
        [6,7,1,4,5],
        [5,1,1,2,4]
    ]
    assert solution.pacificAtlantic(heights1) == [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]

    # Test case 2: Single cell island
    heights2 = [[1]]
    assert solution.pacificAtlantic(heights2) == [[0,0]]

    # Test case 3: All cells with the same height
    heights3 = [[1,1,1],[1,1,1],[1,1,1]]
    assert set(map(tuple, solution.pacificAtlantic(heights3))) == set([(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)])

    # Test case 4: Strictly increasing heights
    heights4 = [[1,2,3],[4,5,6],[7,8,9]]
    assert solution.pacificAtlantic(heights4) == [[0,2],[1,1],[1,2],[2,0],[2,1],[2,2]]

    # Test case 5: Strictly decreasing heights
    heights5 = [[9,8,7],[6,5,4],[3,2,1]]
    assert solution.pacificAtlantic(heights5) == [[0,0],[0,1],[0,2],[1,0],[1,1],[2,0]]

    # Test case 6: Checkerboard pattern
    heights6 = [[1,2,1,2],[2,1,2,1],[1,2,1,2]]
    assert set(map(tuple, solution.pacificAtlantic(heights6))) == set([(0,0),(0,1),(0,2),(0,3),(1,0),(1,1),(1,2),(1,3),(2,0),(2,1),(2,2),(2,3)])

    # Test case 7: Large grid with random heights
    import random
    random.seed(42)
    heights7 = [[random.randint(1, 100) for _ in range(100)] for _ in range(100)]
    result7 = solution.pacificAtlantic(heights7)
    assert len(result7) > 0  # We expect some cells to reach both oceans

    print("All test cases passed!")

test_pacific_atlantic()
```

### Solutions

#### Overview of solution approaches

##### Solutions worth learning

1. Depth-First Search (DFS) from ocean edges (Neetcode solution)
2. Breadth-First Search (BFS) from ocean edges
3. Union-Find (Disjoint Set) approach

Count: 3 solutions (1 Neetcode solution)

##### Rejected solutions

1. Brute Force DFS/BFS from each cell: This approach would be inefficient as it requires checking every cell individually, leading to redundant computations.
2. Dynamic Programming: While DP can be used for some grid-based problems, it's not well-suited here due to the non-linear nature of water flow.

#### Worthy Solutions

##### Depth-First Search (DFS) from ocean edges

```python
from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []

        m, n = len(heights), len(heights[0])

        def dfs(i: int, j: int, reachable: set, prev_height: int) -> None:
            # Base case: out of bounds or current height is lower than previous (water can't flow)
            if (i < 0 or i >= m or j < 0 or j >= n or
                (i, j) in reachable or heights[i][j] < prev_height):
                return

            # Mark current cell as reachable
            reachable.add((i, j))

            # Recursively explore neighboring cells
            for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                dfs(i + di, j + dj, reachable, heights[i][j])

        # Sets to store cells reachable from Pacific and Atlantic
        pacific_reachable = set()
        atlantic_reachable = set()

        # DFS from top and bottom edges
        for j in range(n):
            dfs(0, j, pacific_reachable, heights[0][j])  # Top edge (Pacific)
            dfs(m - 1, j, atlantic_reachable, heights[m - 1][j])  # Bottom edge (Atlantic)

        # DFS from left and right edges
        for i in range(m):
            dfs(i, 0, pacific_reachable, heights[i][0])  # Left edge (Pacific)
            dfs(i, n - 1, atlantic_reachable, heights[i][n - 1])  # Right edge (Atlantic)

        # Return the intersection of cells reachable from both oceans
        return list(pacific_reachable & atlantic_reachable)
```

Time Complexity: O(m \* n), where m is the number of rows and n is the number of columns in the heights matrix. We visit each cell at most twice (once for Pacific and once for Atlantic).

Space Complexity: O(m \* n) in the worst case, where all cells are reachable from both oceans. This space is used for the recursion stack and the sets storing reachable cells.

Key intuitions and invariants:

- Start DFS from the ocean edges, moving inward.
- Water can flow from a cell to its neighbor if the neighbor's height is greater than or equal to the current cell's height.
- Use separate sets to track cells reachable from each ocean.
- The final result is the intersection of these two sets.

##### Breadth-First Search (BFS) from ocean edges

```python
from typing import List
from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []

        m, n = len(heights), len(heights[0])

        def bfs(queue: deque, reachable: set) -> None:
            while queue:
                i, j = queue.popleft()
                for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    ni, nj = i + di, j + dj
                    if (0 <= ni < m and 0 <= nj < n and
                        (ni, nj) not in reachable and
                        heights[ni][nj] >= heights[i][j]):
                        reachable.add((ni, nj))
                        queue.append((ni, nj))

        pacific_queue = deque([(i, 0) for i in range(m)] + [(0, j) for j in range(1, n)])
        atlantic_queue = deque([(i, n-1) for i in range(m)] + [(m-1, j) for j in range(n-1)])

        pacific_reachable = set(pacific_queue)
        atlantic_reachable = set(atlantic_queue)

        bfs(pacific_queue, pacific_reachable)
        bfs(atlantic_queue, atlantic_reachable)

        return list(pacific_reachable & atlantic_reachable)
```

Time Complexity: O(m \* n), where m is the number of rows and n is the number of columns. Each cell is visited at most twice.

Space Complexity: O(m \* n) for the queues and sets in the worst case.

Key intuitions and invariants:

- Use queues to process cells in a breadth-first manner.
- Start from ocean edges and expand inward.
- Maintain separate sets for cells reachable from each ocean.
- The intersection of these sets gives the final result.

##### Union-Find (Disjoint Set) approach

```python
from typing import List

class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x: int, y: int) -> None:
        px, py = self.find(x), self.find(y)
        if px == py:
            return
        if self.rank[px] < self.rank[py]:
            self.parent[px] = py
        elif self.rank[px] > self.rank[py]:
            self.parent[py] = px
        else:
            self.parent[py] = px
            self.rank[px] += 1

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []

        m, n = len(heights), len(heights[0])
        uf = UnionFind(m * n + 2)  # +2 for Pacific and Atlantic "super nodes"
        pacific, atlantic = m * n, m * n + 1

        def get_id(i: int, j: int) -> int:
            return i * n + j

        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    uf.union(get_id(i, j), pacific)
                if i == m - 1 or j == n - 1:
                    uf.union(get_id(i, j), atlantic)

                for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < m and 0 <= nj < n and heights[ni][nj] <= heights[i][j]:
                        uf.union(get_id(i, j), get_id(ni, nj))

        return [[i, j] for i in range(m) for j in range(n)
                if uf.find(get_id(i, j)) == uf.find(pacific) and
                   uf.find(get_id(i, j)) == uf.find(atlantic)]
```

Time Complexity: O(m _ n _ α(m \* n)), where α is the inverse Ackermann function, which grows very slowly and is effectively constant for all practical values of m and n.

Space Complexity: O(m \* n) for the UnionFind data structure.

Key intuitions and invariants:

- Represent the grid as a graph where each cell is a node.
- Use two "super nodes" to represent Pacific and Atlantic oceans.
- Connect cells that can flow into each other.
- Cells connected to both ocean super nodes are the answer.

#### Rejected Approaches

1. Brute Force DFS/BFS from each cell:
   This approach would involve starting a DFS or BFS from every cell and checking if it can reach both oceans. While correct, it's highly inefficient with a time complexity of O(m^2 \* n^2) in the worst case. This solution is rejected because it doesn't leverage the problem's structure and performs many redundant computations.

2. Dynamic Programming:
   A DP approach might seem tempting given the grid structure, but it's not well-suited for this problem. The non-linear nature of water flow (it can go in any direction) makes it difficult to establish a clear recurrence relation. Additionally, the requirement to reach both oceans further complicates a potential DP solution. This approach is rejected due to its complexity and likely inefficiency compared to graph traversal methods.

#### Final Recommendations

The DFS approach (Neetcode solution) is recommended as the best solution to learn for several reasons:

1. Intuitive: It directly models the water flow problem by starting from the oceans and moving inward.
2. Efficient: It has optimal time and space complexity (O(m \* n)).
3. Easy to implement: The recursive nature of DFS makes the code concise and straightforward.
4. Flexible: It can be easily adapted to similar problems or variations of this problem.

While the BFS and Union-Find approaches are also valid and efficient, the DFS solution offers the best balance of simplicity, efficiency, and intuitiveness, making it an excellent choice for interview settings.

### Visualization(s)

To visualize the DFS approach, we can use a simple ASCII representation of the grid:

```
Step 1: Start DFS from Pacific edges (top and left)
P P P P P
P 1 2 2 3
P 3 2 3 4
P 2 4 5 3
P 6 7 1 4

Step 2: After Pacific DFS
P P P P P
P P P P 5
P P P 4 4
P 4 5 3 1
P 7 1 4 5

Step 3: Start DFS from Atlantic edges (bottom and right)
P P P P A
P P P P A
P 4 5 A A
P 7 1 A A
A A A A A

Step 4: Final result (cells reachable from both oceans)
P P P P *
P P P * *
P 4 * 3 1
* * 1 4 5
* 1 1 2 4

Legend:
P: Reachable from Pacific
A: Reachable from Atlantic
*: Reachable from both (final answer)
Numbers: Heights
```

This visualization helps to understand how the DFS progresses from the ocean edges inward, and how the final result is determined by finding cells reachable from both oceans.
