# Backtracking Solutions Guide

[Youtube Video](https://www.youtube.com/watch?v=gBC_Fd8EE8A)

## Notable LeetCode Problems with Backtracking Solutions

1. **N-Queens (LeetCode 51)**
2. **Sudoku Solver (LeetCode 37)**
3. **Combination Sum (LeetCode 39)**
4. **Permutations (LeetCode 46)**
5. **Palindrome Partitioning (LeetCode 131)**

Let's examine the backtracking solutions for these problems:

### 1. N-Queens (LeetCode 51)

```python
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def is_safe(board, row, col):
            # Check column
            for i in range(row):
                if board[i][col] == 'Q':
                    return False

            # Check upper left diagonal
            for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
                if board[i][j] == 'Q':
                    return False

            # Check upper right diagonal
            for i, j in zip(range(row, -1, -1), range(col, n)):
                if board[i][j] == 'Q':
                    return False

            return True

        def backtrack(row):
            if row == n:
                result.append([''.join(row) for row in board])
                return

            for col in range(n):
                if is_safe(board, row, col):
                    board[row][col] = 'Q'
                    backtrack(row + 1)
                    board[row][col] = '.'

        board = [['.' for _ in range(n)] for _ in range(n)]
        result = []
        backtrack(0)
        return result
```

### 2. Sudoku Solver (LeetCode 37)

```python
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        def is_valid(num, pos):
            # Check row
            for col in range(9):
                if board[pos[0]][col] == num and pos[1] != col:
                    return False

            # Check column
            for row in range(9):
                if board[row][pos[1]] == num and pos[0] != row:
                    return False

            # Check 3x3 box
            box_x, box_y = pos[1] // 3, pos[0] // 3
            for i in range(box_y * 3, box_y * 3 + 3):
                for j in range(box_x * 3, box_x * 3 + 3):
                    if board[i][j] == num and (i, j) != pos:
                        return False

            return True

        def solve():
            for i in range(9):
                for j in range(9):
                    if board[i][j] == '.':
                        for num in map(str, range(1, 10)):
                            if is_valid(num, (i, j)):
                                board[i][j] = num
                                if solve():
                                    return True
                                board[i][j] = '.'
                        return False
            return True

        solve()
```

### 3. Combination Sum (LeetCode 39)

```python
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(start, target, path):
            if target == 0:
                result.append(path[:])
                return

            for i in range(start, len(candidates)):
                if candidates[i] > target:
                    continue
                path.append(candidates[i])
                backtrack(i, target - candidates[i], path)
                path.pop()

        result = []
        candidates.sort()
        backtrack(0, target, [])
        return result
```

### 4. Permutations (LeetCode 46)

```python
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(path):
            if len(path) == len(nums):
                result.append(path[:])
                return

            for num in nums:
                if num not in path:
                    path.append(num)
                    backtrack(path)
                    path.pop()

        result = []
        backtrack([])
        return result
```

### 5. Palindrome Partitioning (LeetCode 131)

```python
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_palindrome(start, end):
            while start < end:
                if s[start] != s[end]:
                    return False
                start += 1
                end -= 1
            return True

        def backtrack(start, path):
            if start == len(s):
                result.append(path[:])
                return

            for end in range(start, len(s)):
                if is_palindrome(start, end):
                    path.append(s[start:end+1])
                    backtrack(end + 1, path)
                    path.pop()

        result = []
        backtrack(0, [])
        return result
```

## Generalized Step-by-Step Approach to Writing Backtracking Solutions

1. **Identify the Problem Structure**

   - Determine if the problem requires finding all possible solutions or configurations.
   - Check if the problem involves making choices at each step that affect subsequent choices.
   - Verify if the problem can be solved by building a solution incrementally.

2. **Define the Solution Space**

   - Identify the set of all possible candidates for the solution.
   - Determine the constraints that a valid solution must satisfy.

3. **Design the Backtracking Function**

   - Define the parameters:
     - Current state of the solution
     - Remaining choices or options
     - Any additional problem-specific parameters
   - Implement the base case(s):
     - Recognize when a valid solution is found
     - Add the solution to the result set or perform required actions

4. **Implement the Choice-Making Logic**

   - For each possible choice:
     - Check if the choice is valid given the current state and constraints
     - If valid, make the choice (update the current state)
     - Recursively call the backtracking function with the updated state
     - Undo the choice (backtrack) to explore other possibilities

5. **Optimize the Solution (if necessary)**

   - Implement pruning techniques to avoid exploring unnecessary paths
   - Use data structures to efficiently check constraints or validity

6. **Handle the Result**

   - Decide how to store or return the found solutions (e.g., list of lists, modifying input directly)

7. **Initialize and Call the Backtracking Function**
   - Set up any necessary data structures or variables
   - Call the backtracking function with initial state and parameters

Here's a template that encapsulates this approach:

```python
def backtrack(state, choices, ...):
    if is_solution(state):
        add_to_result(state)
        return

    for choice in choices:
        if is_valid(state, choice):
            apply(state, choice)
            backtrack(state, remaining_choices(choices, choice), ...)
            undo(state, choice)

def solve_problem(input):
    result = []
    initial_state = initialize_state(input)
    initial_choices = generate_initial_choices(input)
    backtrack(initial_state, initial_choices, ...)
    return result
```

### Visualization

To better understand the backtracking process, consider this tree representation:

```
                 Root
               /  |  \
              /   |   \
             /    |    \
         Choice1 Choice2 Choice3
          / \     |     / \
         /   \    |    /   \
      C1,1 C1,2  C2,1 C3,1 C3,2
       |     |    |    |     |
      ...   ...  ...  ...   ...
```

Each level represents a decision point, and each branch represents a choice. The backtracking algorithm explores this tree depth-first, pruning branches that violate constraints and backtracking when it reaches a dead end or finds a solution.

### Key Properties of Backtracking Problems

1. **Incremental Solution Building**: Solutions are constructed step by step.
2. **Constraint Satisfaction**: Each step must satisfy problem-specific constraints.
3. **Depth-First Search**: The algorithm explores as far as possible along each branch before backtracking.
4. **State Management**: The current state must be manageable and easily modifiable.
5. **Pruning**: Early detection of invalid paths to avoid unnecessary exploration.

By following this generalized approach and understanding these key properties, you can tackle a wide range of backtracking problems efficiently.
