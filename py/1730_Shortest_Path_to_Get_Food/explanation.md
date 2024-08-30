## Question: Shortest Path to Get Food

You are starving and you want to eat food as quickly as possible. You want to find the shortest path to arrive at any food cell.

You are given an `m x n` character matrix, `grid`, of these different types of cells:

- `'*'` is your location. There is exactly one `'*'` cell.
- `'#'` is a food cell. There may be multiple food cells.
- `'O'` is free space, and you can travel through these cells.
- `'X'` is an obstacle, and you cannot travel through these cells.

You can travel to any adjacent cell north, east, south, or west of your current location if there is not an obstacle.

Return the length of the shortest path for you to reach any food cell. If there is no path for you to reach food, return -1.

## Explanation: Shortest Path to Get Food

### Analysis of problem & input data

This problem is a classic example of a shortest path problem in a 2D grid. The key characteristics that help us pattern-match to a solution are:

1. We're working with a 2D grid (matrix) with different types of cells.
2. We need to find the shortest path from a starting point to any of potentially multiple endpoints.
3. Movement is restricted to adjacent cells (up, down, left, right).
4. There are obstacles that we can't pass through.

These characteristics strongly suggest using a breadth-first search (BFS) algorithm. BFS is optimal for this problem because:

1. It explores all possible paths simultaneously, level by level.
2. In an unweighted graph (which our grid effectively is), BFS always finds the shortest path first.
3. It can easily handle multiple possible end points (food cells).

The key principle that makes this question simple is that BFS always explores nodes in order of their distance from the start. This means that the first food cell we encounter during our BFS is guaranteed to be the closest one.

### Test cases

Here are some relevant test cases:

1. Basic case with a clear path:

   ```
   [['*', 'O', 'O', '#'],
    ['O', 'X', 'O', 'O'],
    ['O', 'O', 'O', 'O']]
   ```

   Expected output: 3

2. No path to food:

   ```
   [['*', 'X', 'O', 'O'],
    ['O', 'X', '#', 'O'],
    ['O', 'X', 'O', 'O']]
   ```

   Expected output: -1

3. Multiple food sources:

   ```
   [['*', 'O', 'O', '#'],
    ['#', 'O', 'X', 'O'],
    ['O', 'O', 'O', '#']]
   ```

   Expected output: 2

4. Food right next to start:

   ```
   [['*', '#'],
    ['O', 'O']]
   ```

   Expected output: 1

5. Large grid with winding path:
   ```
   [['*', 'X', 'O', 'O', 'O'],
    ['O', 'X', 'X', 'X', 'O'],
    ['O', 'O', 'O', 'X', 'O'],
    ['X', 'X', 'O', 'X', 'O'],
    ['#', 'O', 'O', 'O', 'O']]
   ```
   Expected output: 12

Here's the Python code to set up these test cases:

```python
def test_get_food():
    test_cases = [
        [['*', 'O', 'O', '#'], ['O', 'X', 'O', 'O'], ['O', 'O', 'O', 'O']],
        [['*', 'X', 'O', 'O'], ['O', 'X', '#', 'O'], ['O', 'X', 'O', 'O']],
        [['*', 'O', 'O', '#'], ['#', 'O', 'X', 'O'], ['O', 'O', 'O', '#']],
        [['*', '#'], ['O', 'O']],
        [['*', 'X', 'O', 'O', 'O'], ['O', 'X', 'X', 'X', 'O'],
         ['O', 'O', 'O', 'X', 'O'], ['X', 'X', 'O', 'X', 'O'],
         ['#', 'O', 'O', 'O', 'O']]
    ]
    expected_outputs = [3, -1, 2, 1, 12]

    for i, (grid, expected) in enumerate(zip(test_cases, expected_outputs)):
        result = get_food(grid)
        print(f"Test case {i+1}: {'Passed' if result == expected else 'Failed'}")
        print(f"Expected: {expected}, Got: {result}")
        print()

# The get_food function will be implemented in the Solutions section
```

### Solutions

#### Overview of solution approaches

##### Solutions worth learning

1. Breadth-First Search (BFS) with Queue (Neetcode solution)
2. A\* Search
3. Depth-First Search (DFS) with pruning

Count: 3 solutions (1 Neetcode solution)

##### Rejected solutions

1. Dijkstra's Algorithm: While it would work, it's overkill for an unweighted graph and less efficient than BFS.
2. Floyd-Warshall Algorithm: This is for all-pairs shortest paths and would be extremely inefficient for this problem.
3. Simple DFS without pruning: This could potentially explore all paths before finding the shortest one, making it inefficient.

#### Worthy Solutions

##### Breadth-First Search (BFS) with Queue (Neetcode solution)

```python
from collections import deque
from typing import List

def get_food(grid: List[List[str]]) -> int:
    if not grid or not grid[0]:
        return -1

    m, n = len(grid), len(grid[0])
    queue = deque()
    visited = set()

    # Find the starting position
    for i in range(m):
        for j in range(n):
            if grid[i][j] == '*':
                queue.append((i, j, 0))  # (row, col, distance)
                visited.add((i, j))
                break
        if queue:
            break

    # Directions: up, right, down, left
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    while queue:
        row, col, dist = queue.popleft()

        # Check if we've reached food
        if grid[row][col] == '#':
            return dist

        # Explore neighbors
        for dx, dy in directions:
            new_row, new_col = row + dx, col + dy

            # Check if the new position is valid and not visited
            if (0 <= new_row < m and 0 <= new_col < n and
                grid[new_row][new_col] != 'X' and
                (new_row, new_col) not in visited):
                queue.append((new_row, new_col, dist + 1))
                visited.add((new_row, new_col))

    # If we've explored all reachable cells and haven't found food
    return -1
```

Time Complexity: O(m \* n), where m is the number of rows and n is the number of columns in the grid.
Space Complexity: O(m \* n) in the worst case, where we might need to store all cells in the queue and visited set.

Explanation:

- We iterate through each cell once in the worst case, hence the time complexity is O(m \* n).
- In the worst case, we might need to store all cells in the queue and visited set before finding food or exhausting all possibilities, leading to a space complexity of O(m \* n).

Key intuitions and invariants:

- BFS explores cells in order of their distance from the start, ensuring we find the shortest path.
- The queue stores cells to explore, with their distances from the start.
- The visited set prevents revisiting cells, avoiding cycles and redundant work.
- By checking for food at each step, we ensure we stop as soon as we find the closest food.

##### A\* Search

```python
import heapq
from typing import List, Tuple

def get_food(grid: List[List[str]]) -> int:
    if not grid or not grid[0]:
        return -1

    m, n = len(grid), len(grid[0])

    # Find the starting position and food positions
    start = None
    food = []
    for i in range(m):
        for j in range(n):
            if grid[i][j] == '*':
                start = (i, j)
            elif grid[i][j] == '#':
                food.append((i, j))

    if not start or not food:
        return -1

    # Heuristic function: Manhattan distance to the nearest food
    def h(pos: Tuple[int, int]) -> int:
        return min(abs(pos[0] - f[0]) + abs(pos[1] - f[1]) for f in food)

    # A* search
    heap = [(h(start), 0, start)]  # (f, g, position)
    visited = set()

    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    while heap:
        _, g, (row, col) = heapq.heappop(heap)

        if (row, col) in visited:
            continue
        visited.add((row, col))

        if grid[row][col] == '#':
            return g

        for dx, dy in directions:
            new_row, new_col = row + dx, col + dy
            if (0 <= new_row < m and 0 <= new_col < n and
                grid[new_row][new_col] != 'X' and
                (new_row, new_col) not in visited):
                new_pos = (new_row, new_col)
                new_g = g + 1
                new_f = new_g + h(new_pos)
                heapq.heappush(heap, (new_f, new_g, new_pos))

    return -1
```

Time Complexity: O(m \* n \* log(m \* n)), where m is the number of rows and n is the number of columns in the grid.
Space Complexity: O(m \* n)

Explanation:

- In the worst case, we might explore all cells, each operation on the heap takes O(log(m\*n)) time, hence the time complexity.
- We store all cells in the heap and visited set in the worst case, leading to O(m \* n) space complexity.

Key intuitions and invariants:

- A\* uses a heuristic function to guide the search towards the goal, potentially finding the solution faster than BFS in some cases.
- The heuristic (Manhattan distance to nearest food) is admissible and consistent, ensuring optimality.
- The priority queue (heap) always expands the most promising node first.

##### Depth-First Search (DFS) with pruning

```python
from typing import List, Tuple

def get_food(grid: List[List[str]]) -> int:
    if not grid or not grid[0]:
        return -1

    m, n = len(grid), len(grid[0])
    start = None
    for i in range(m):
        for j in range(n):
            if grid[i][j] == '*':
                start = (i, j)
                break
        if start:
            break

    if not start:
        return -1

    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    min_dist = float('inf')

    def dfs(row: int, col: int, dist: int, visited: set) -> None:
        nonlocal min_dist

        if dist >= min_dist:
            return  # Prune: we've already found a shorter path

        if grid[row][col] == '#':
            min_dist = min(min_dist, dist)
            return

        for dx, dy in directions:
            new_row, new_col = row + dx, col + dy
            if (0 <= new_row < m and 0 <= new_col < n and
                grid[new_row][new_col] != 'X' and
                (new_row, new_col) not in visited):
                visited.add((new_row, new_col))
                dfs(new_row, new_col, dist + 1, visited)
                visited.remove((new_row, new_col))

    dfs(start[0], start[1], 0, {start})

    return min_dist if min_dist != float('inf') else -1
```

Time Complexity: O(4^(m\*n)) in the worst case, but typically much better due to pruning.
Space Complexity: O(m \* n) for the recursion stack in the worst case.

Explanation:

- In the worst case, we might explore all possible paths, leading to a time complexity of O(4^(m\*n)).
- The space complexity is O(m \* n) due to the recursion stack and visited set.
- However, pruning significantly reduces the actual runtime in practice.

Key intuitions and invariants:

- DFS explores paths deeply before backtracking.
- Pruning eliminates exploration of paths longer than the current best solution.
- The visited set prevents revisiting cells and getting stuck in cycles.

#### Rejected Approaches

1. Dijkstra's Algorithm: While this would work, it's unnecessary for an unweighted graph. BFS achieves the same result more efficiently in this context.

2. Floyd-Warshall Algorithm: This algorithm finds the shortest paths between all pairs of vertices. It's overkill for this problem and would have a time complexity of O(n^3), where n is the total number of cells.

3. Simple DFS without pruning: This could potentially explore all paths before finding the shortest one. In the worst case, it could have a time complexity of O(4^(m\*n)), making it inefficient for larger grids.

#### Final Recommendations

The Breadth-First Search (BFS) solution is the most recommended approach for this problem. Here's why:

1. Optimal Time Complexity: BFS guarantees finding the shortest path in O(m \* n) time, which is optimal for this problem.
2. Simplicity: The BFS solution is straightforward to implement and understand.
3. Memory Efficiency: While it uses O(m \* n) space in the worst case, it's generally more memory-efficient than A\* for this specific problem.
4. Guaranteed Optimality: BFS always finds the shortest path in unweighted graphs.

While A\* and DFS with pruning are interesting alternatives, they don't offer significant advantages for this specific problem:

- A\* could potentially be faster in some cases, but its implementation is more complex, and the overhead of maintaining a priority queue might not be justified for this unweighted graph problem.
- DFS with pruning, while an interesting approach, doesn't guarantee finding the shortest path first and could be less efficient on average.

Therefore, mastering the BFS approach for this type of problem is most beneficial for coding interviews and similar problem-solving scenarios.

### Visualization(s)

To visualize the BFS algorithm for this problem, we can use a simple ASCII representation of the grid and show how the algorithm explores cells level by level. Here's a basic visualization:

```python
def visualize_bfs(grid):
    m, n = len(grid), len(grid[0])
    visited = set()
    queue = deque()

    # Find start
    for i in range(m):
        for j in range(n):
            if grid[i][j] == '*':
                queue.append((i, j, 0))
                visited.add((i, j))
                break
        if queue:
            break

    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    step = 0
    while queue:
        level_size = len(queue)
        print(f"\nStep {step}:")

        for i in range(m):
            for j in range(n):
                if (i, j) in visited:
                    print("V", end=" ")
                elif grid[i][j] == 'X':
                    print("X", end=" ")
                elif grid[i][j] == '#':
                    print("#", end=" ")
                else:
                    print(".", end=" ")
            print()

        for _ in range(level_size):
            row, col, dist = queue.popleft()

            if grid[row][col] == '#':
                print(f"\nFood found at distance {dist}")
                return

            for dx, dy in directions:
                new_row, new_col = row + dx, col + dy
                if (0 <= new_row < m and 0 <= new_col < n and
                    grid[new_row][new_col] != 'X' and
                    (new_row, new_col) not in visited):
                    queue.append((new_row, new_col, dist + 1))
                    visited.add((new_row, new_col))

        step += 1

    print("\nNo food found")

# Example usage
grid = [
    ['*', 'O', 'O', '#'],
    ['O', 'X', 'O', 'O'],
    ['O', 'O', 'O', 'O']
]

visualize_bfs(grid)
```

This visualization function will show how the BFS algorithm explores the grid step by step. Here's what each symbol represents:

- `V`: Visited cell
- `X`: Obstacle
- `#`: Food
- `.`: Unvisited free space

When we run this visualization on our example grid, it will produce output like this:

```
Step 0:
V . . #
. X . .
. . . .

Step 1:
V V V #
V X . .
. . . .

Step 2:
V V V #
V X V .
V V . .

Step 3:
V V V #
V X V V
V V V .

Food found at distance 3
```

This visualization helps to understand how BFS explores the grid level by level, always finding the shortest path to the food.

Let's also create a simple visualization for the A\* algorithm to compare:

```python
import heapq

def visualize_astar(grid):
    m, n = len(grid), len(grid[0])
    start = None
    food = []
    for i in range(m):
        for j in range(n):
            if grid[i][j] == '*':
                start = (i, j)
            elif grid[i][j] == '#':
                food.append((i, j))

    def h(pos):
        return min(abs(pos[0] - f[0]) + abs(pos[1] - f[1]) for f in food)

    heap = [(h(start), 0, start)]
    visited = set()
    step = 0

    while heap:
        print(f"\nStep {step}:")
        for i in range(m):
            for j in range(n):
                if (i, j) in visited:
                    print("V", end=" ")
                elif grid[i][j] == 'X':
                    print("X", end=" ")
                elif grid[i][j] == '#':
                    print("#", end=" ")
                else:
                    print(".", end=" ")
            print()

        _, g, (row, col) = heapq.heappop(heap)

        if (row, col) in visited:
            continue
        visited.add((row, col))

        if grid[row][col] == '#':
            print(f"\nFood found at distance {g}")
            return

        for dx, dy in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            new_row, new_col = row + dx, col + dy
            if (0 <= new_row < m and 0 <= new_col < n and
                grid[new_row][new_col] != 'X' and
                (new_row, new_col) not in visited):
                new_pos = (new_row, new_col)
                new_g = g + 1
                new_f = new_g + h(new_pos)
                heapq.heappush(heap, (new_f, new_g, new_pos))

        step += 1

    print("\nNo food found")

# Example usage
grid = [
    ['*', 'O', 'O', '#'],
    ['O', 'X', 'O', 'O'],
    ['O', 'O', 'O', 'O']
]

visualize_astar(grid)
```

When we run this A\* visualization on the same grid, it might produce output like:

```
Step 0:
V . . #
. X . .
. . . .

Step 1:
V V . #
V X . .
. . . .

Step 2:
V V V #
V X . .
. . . .

Food found at distance 3
```

Notice how A\* might explore fewer cells than BFS before reaching the food, as it's guided by the heuristic function. However, for this simple grid, the difference is minimal.

These visualizations help to illustrate the key differences between BFS and A\*:

1. BFS explores uniformly in all directions, while A\* is guided towards the goal by its heuristic function.
2. BFS guarantees finding the shortest path by exploring level by level, while A\* aims to find the shortest path more efficiently by prioritizing promising directions.
3. In simple grids like this example, both algorithms perform similarly. However, in larger, more complex grids with multiple food sources, A\* might show more significant efficiency gains.

Understanding these visualizations can help reinforce the concepts behind these algorithms and provide intuition about their behavior in different scenarios.

```

```
