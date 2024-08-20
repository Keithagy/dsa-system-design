## Explanation: Word Search

### Analysis of problem & input data

This problem is a classic example of a grid-based search problem, which is commonly solved using depth-first search (DFS) with backtracking. The key characteristics of this problem are:

1. Grid structure: The input is a 2D grid of characters, which suggests a need for traversal in multiple directions.
2. Sequential search: We need to find a sequence of adjacent cells that match the given word.
3. Revisiting restriction: Each cell can only be used once in the word, which implies we need to keep track of visited cells.
4. Directional movement: We can move horizontally or vertically, but not diagonally.
5. Bounded search space: The grid size is relatively small (up to 6x6), which makes exhaustive search feasible.

The key principle that makes this question simple is the combination of DFS and backtracking. DFS allows us to explore paths deeply, while backtracking enables us to undo choices and explore alternative paths efficiently.

Pattern matching for this problem:

- Grid-based search → DFS or BFS
- Need to explore all possibilities → Backtracking
- Sequence matching → Path-finding algorithms

### Test cases

1. Edge cases:

   - Empty board
   - Single character board
   - Word longer than the total number of cells in the board
   - Word with repeated characters
   - Word that zigzags through the board

2. Challenging inputs:
   - Word that exists but requires backtracking
   - Word that doesn't exist but shares a prefix with an existing path
   - Word that uses all cells in the board

Here's the Python code for test cases:

```python
def test_word_search(word_search_function):
    test_cases = [
        # Basic cases
        ([["A"]], "A", True),
        ([["A"]], "B", False),
        ([["A","B"],["C","D"]], "ABDC", True),

        # Edge cases
        ([], "A", False),
        ([[]], "A", False),
        ([["A","B"],["C","D"]], "ABCDA", False),

        # Challenging inputs
        ([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED", True),
        ([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE", True),
        ([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB", False),
        ([["A","A","A","A"],["A","A","A","A"],["A","A","A","A"]], "AAAAAAAAAAAAA", True),
    ]

    for i, (board, word, expected) in enumerate(test_cases):
        result = word_search_function(board, word)
        assert result == expected, f"Test case {i+1} failed. Expected {expected}, got {result}"
    print("All test cases passed!")

# Usage:
# test_word_search(your_word_search_function)
```

### Solutions

#### Overview of solution approaches

##### Solutions worth learning

1. DFS with Backtracking: The most intuitive and efficient solution for this problem.
2. Trie-based DFS: An optimization for multiple word searches on the same board.

Count: 2 solutions

##### Rejected solutions

1. Brute Force: Checking all possible paths in the grid (extremely inefficient).
2. BFS: While possible, it's less efficient than DFS for this particular problem.

#### Worthy Solutions

##### DFS with Backtracking

```python
from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not board[0]:
            return False

        m, n = len(board), len(board[0])

        def dfs(i: int, j: int, k: int) -> bool:
            # Base case: we've matched all characters in the word
            if k == len(word):
                return True

            # Check if current position is out of bounds or doesn't match the current character
            if (i < 0 or i >= m or j < 0 or j >= n or board[i][j] != word[k]):
                return False

            # Mark the current cell as visited
            temp, board[i][j] = board[i][j], '#'

            # Recursive calls in all four directions
            result = (dfs(i+1, j, k+1) or
                      dfs(i-1, j, k+1) or
                      dfs(i, j+1, k+1) or
                      dfs(i, j-1, k+1))

            # Backtrack: restore the cell's original value
            board[i][j] = temp

            return result

        # Try starting the search from each cell in the grid
        return any(dfs(i, j, 0) for i in range(m) for j in range(n))
```

Time Complexity: O(m \* n \* 4^L), where m and n are the dimensions of the board, and L is the length of the word.
Space Complexity: O(L) for the recursion stack.

Key intuitions and invariants:

- We use DFS to explore paths in the grid, trying to match the word character by character.
- Backtracking allows us to mark cells as visited during exploration and unmark them when backtracking.
- The base case of the recursion is when we've matched all characters in the word.
- We prune the search by immediately returning false if we go out of bounds or encounter a non-matching character.
- The use of a temporary variable to mark visited cells ensures we don't revisit the same cell in a single path.

##### Trie-based DFS

```python
from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class Solution:
    def buildTrie(self, word: str) -> TrieNode:
        root = TrieNode()
        node = root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_word = True
        return root

    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not board[0] or not word:
            return False

        root = self.buildTrie(word)
        m, n = len(board), len(board[0])

        def dfs(i: int, j: int, node: TrieNode) -> bool:
            if node.is_word:
                return True

            if i < 0 or i >= m or j < 0 or j >= n:
                return False

            char = board[i][j]
            if char not in node.children:
                return False

            # Mark as visited
            board[i][j] = '#'

            # Recursive calls
            result = (dfs(i+1, j, node.children[char]) or
                      dfs(i-1, j, node.children[char]) or
                      dfs(i, j+1, node.children[char]) or
                      dfs(i, j-1, node.children[char]))

            # Backtrack
            board[i][j] = char

            return result

        return any(dfs(i, j, root) for i in range(m) for j in range(n))
```

Time Complexity: O(m \* n \* 4^L), where m and n are the dimensions of the board, and L is the length of the word.
Space Complexity: O(L) for the Trie and recursion stack.

Key intuitions and invariants:

- We build a Trie from the word, which allows for efficient prefix matching.
- The DFS traversal follows the Trie structure, pruning paths that don't match any prefix in the word.
- This approach is particularly efficient when searching for multiple words in the same board.
- The Trie structure acts as an implicit visited set, preventing revisiting of cells in a single path.

#### Rejected Approaches

1. Brute Force: Generating all possible paths in the grid and checking if any match the word. This approach has a time complexity of O(m \* n \* 8^L), which is extremely inefficient.

2. BFS: While BFS could solve this problem, it's less efficient than DFS for this particular task. BFS would explore all possible paths of length 1, then length 2, and so on, which is unnecessary when we're looking for a specific word.

#### Final Recommendations

The DFS with Backtracking solution is the best to learn for this problem. It's intuitive, efficient, and demonstrates key concepts like depth-first search and backtracking. The Trie-based solution is an excellent optimization for scenarios where you need to search for multiple words in the same board, but it's more complex and might be overkill for a single word search.

### Analysis of the provided solution

The solution you provided uses DFS with backtracking and includes some optimizations like memoization. While it's a good attempt, there are a few issues that need to be addressed:

1. Memoization implementation:

   - The current memoization strategy is flawed. In a word search, the validity of a path depends on the entire path taken, not just the current position and word index.
   - Memoizing `(row, col, word_idx)` can lead to incorrect results because it doesn't consider the path taken to reach that state.

2. Path tracking:

   - The `path` set is correctly used to avoid revisiting cells in the current path.
   - However, it's not reset between different starting positions, which could lead to incorrect results.

3. Early return condition:

   - The base case `if word_idx == len(word) - 1` is correct, but it should be checked before accessing `board[row][col]` to avoid index out of range errors.

4. Unnecessary complexity:

   - The use of a dictionary for directions adds unnecessary overhead. A list of tuples would be more efficient.

5. Type hinting:
   - The type hint for `directions` should be `Set[Tuple[int, int]]` instead of just `Set`.

### Corrected Solution

Here's a corrected version of your solution that addresses these issues:

```python
from typing import List, Set, Tuple

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if len(word) > len(board) * len(board[0]):
            return False

        directions: List[Tuple[int, int]] = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def explore(row: int, col: int, word_idx: int, path: Set[Tuple[int, int]]) -> bool:
            if word_idx == len(word):
                return True

            if (row < 0 or row >= len(board) or
                col < 0 or col >= len(board[0]) or
                (row, col) in path or
                board[row][col] != word[word_idx]):
                return False

            path.add((row, col))

            for row_diff, col_diff in directions:
                nr, nc = row + row_diff, col + col_diff
                if explore(nr, nc, word_idx + 1, path):
                    return True

            path.remove((row, col))
            return False

        for row in range(len(board)):
            for col in range(len(board[0])):
                if explore(row, col, 0, set()):
                    return True

        return False
```

### Key changes and explanations

1. Removed memoization: The memoization was causing incorrect results due to not considering the full path.

2. Simplified the `explore` function:

   - Moved all boundary and validity checks to the beginning of the function.
   - Removed the early return for the last character, as it's handled by the base case.

3. Path handling:

   - Now passing the `path` set as an argument to `explore`, ensuring a fresh set for each starting position.

4. Changed `directions` to a list of tuples for better performance.

5. Moved the base case check (`word_idx == len(word)`) to the beginning of `explore` for clarity and to avoid potential index out of range errors.

6. Removed unnecessary variables and simplified the loop in the main function.

This corrected version maintains the efficiency of your original approach while fixing the issues that could lead to incorrect results. The time complexity remains O(m \* n \* 4^L), where m and n are the dimensions of the board, and L is the length of the word. The space complexity is O(L) for the recursion stack and the path set.
