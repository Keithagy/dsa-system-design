## Explanation: Valid Sudoku

### Analysis of problem & input data

This problem is fundamentally about validating a partially filled Sudoku board according to specific rules. The key aspects to consider are:

1. Data structure: The input is a 9x9 2D array (list of lists in Python) representing the Sudoku board.
2. Content: Each cell contains either a digit from '1' to '9' or a '.' representing an empty cell.
3. Validation rules: We need to check for uniqueness in rows, columns, and 3x3 sub-boxes.
4. Partial filling: We only need to validate the filled cells, not solve the Sudoku.

The core principle that makes this question simple is the use of hash sets for efficient uniqueness checking. By leveraging sets, we can quickly determine if a value has been seen before in a particular row, column, or 3x3 sub-box.

This problem falls into the category of matrix traversal and hash table usage. It's not about solving the Sudoku, but rather efficiently checking the validity of the current state. The challenge lies in how to efficiently check all three conditions (row, column, and sub-box) in a single pass through the board.

### Test cases

Here are some relevant test cases:

1. Valid complete Sudoku board
2. Valid partially filled Sudoku board (as given in Example 1)
3. Invalid board with duplicate in row (as given in Example 2)
4. Invalid board with duplicate in column
5. Invalid board with duplicate in 3x3 sub-box
6. Empty board (all '.')
7. Board with single filled cell
8. Board with all cells filled with the same valid digit

Here's the Python code for these test cases:

```python
def test_valid_sudoku(is_valid_sudoku_func):
    # Test case 1: Valid complete Sudoku board
    board1 = [
        ["5","3","4","6","7","8","9","1","2"],
        ["6","7","2","1","9","5","3","4","8"],
        ["1","9","8","3","4","2","5","6","7"],
        ["8","5","9","7","6","1","4","2","3"],
        ["4","2","6","8","5","3","7","9","1"],
        ["7","1","3","9","2","4","8","5","6"],
        ["9","6","1","5","3","7","2","8","4"],
        ["2","8","7","4","1","9","6","3","5"],
        ["3","4","5","2","8","6","1","7","9"]
    ]
    assert is_valid_sudoku_func(board1) == True

    # Test case 2: Valid partially filled Sudoku board (Example 1)
    board2 = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    assert is_valid_sudoku_func(board2) == True

    # Test case 3: Invalid board with duplicate in row (Example 2)
    board3 = [
        ["8","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    assert is_valid_sudoku_func(board3) == False

    # Test case 4: Invalid board with duplicate in column
    board4 = [
        ["5","3",".",".","7",".",".",".","."],
        ["5",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    assert is_valid_sudoku_func(board4) == False

    # Test case 5: Invalid board with duplicate in 3x3 sub-box
    board5 = [
        ["5","3",".",".","7",".",".",".","."],
        ["6","5",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    assert is_valid_sudoku_func(board5) == False

    # Test case 6: Empty board
    board6 = [["." for _ in range(9)] for _ in range(9)]
    assert is_valid_sudoku_func(board6) == True

    # Test case 7: Board with single filled cell
    board7 = [["." for _ in range(9)] for _ in range(9)]
    board7[0][0] = "5"
    assert is_valid_sudoku_func(board7) == True

    # Test case 8: Board with all cells filled with the same valid digit
    board8 = [["5" for _ in range(9)] for _ in range(9)]
    assert is_valid_sudoku_func(board8) == False

    print("All test cases passed!")

# Usage:
# test_valid_sudoku(your_is_valid_sudoku_function)
```

### Solutions

#### Overview of solution approaches

##### Solutions worth learning

1. Single-pass with hash sets (Neetcode solution)
2. Three separate passes (one for rows, one for columns, one for sub-boxes)
3. Bitmap solution
4. Array-based solution

Count: 4 solutions (1 Neetcode solution)

##### Rejected solutions

1. Brute force checking every possibility (O(n^4) time complexity)
2. Solving the Sudoku completely (unnecessarily complex for this problem)

#### Worthy Solutions

##### Single-pass with hash sets (Neetcode solution)

```python
from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == '.':
                    continue

                # Check row
                if val in rows[r]:
                    return False
                rows[r].add(val)

                # Check column
                if val in cols[c]:
                    return False
                cols[c].add(val)

                # Check 3x3 sub-box
                box_idx = (r // 3) * 3 + (c // 3)
                if val in boxes[box_idx]:
                    return False
                boxes[box_idx].add(val)

        return True
```

Time Complexity: O(1)
Space Complexity: O(1)

Explanation:

- Time Complexity: We iterate through each cell of the 9x9 board exactly once. Since the board size is fixed (9x9), this results in a constant number of operations (81 iterations). Therefore, the time complexity is O(1).
- Space Complexity: We use 27 sets (9 for rows, 9 for columns, 9 for boxes), each containing at most 9 elements. Since the space used is constant regardless of input size, the space complexity is O(1).

Key intuitions and invariants:

- Use separate sets for rows, columns, and 3x3 sub-boxes to check for duplicates efficiently.
- The box index formula `(r // 3) * 3 + (c // 3)` maps each cell to its corresponding 3x3 sub-box.
- Early return on finding any duplicate saves unnecessary iterations.
- Skipping '.' cells focuses only on filled cells, as per the problem statement.

##### Three separate passes

```python
from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def is_valid_unit(unit):
            # Filter out '.' and check for duplicates
            digits = [x for x in unit if x != '.']
            return len(digits) == len(set(digits))

        # Check rows
        for row in board:
            if not is_valid_unit(row):
                return False

        # Check columns
        for col in zip(*board):
            if not is_valid_unit(col):
                return False

        # Check 3x3 sub-boxes
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                sub_box = [board[x][y] for x in range(i, i+3) for y in range(j, j+3)]
                if not is_valid_unit(sub_box):
                    return False

        return True
```

Time Complexity: O(1)
Space Complexity: O(1)

Explanation:

- Time Complexity: We make three passes through the board, each examining all 81 cells. Since the board size is fixed, this results in a constant number of operations. Therefore, the time complexity is O(1).
- Space Complexity: We create temporary lists and sets for each unit (row, column, sub-box), but these are of constant size (at most 9 elements). Thus, the space complexity is O(1).

Key intuitions and invariants:

- Separate the validation of rows, columns, and sub-boxes for clarity.
- Use list comprehension and zip function for elegant column and sub-box extraction.
- The `is_valid_unit` function encapsulates the logic for checking uniqueness in any unit (row, column, or sub-box).
- Filtering out '.' before checking for duplicates adheres to the requirement of only validating filled cells.

##### Bitmap solution

```python
from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def is_valid_unit(unit):
            seen = 0
            for cell in unit:
                if cell != '.':
                    val = int(cell)
                    if seen & (1 << val):
                        return False
                    seen |= (1 << val)
            return True

        # Check rows
        for row in board:
            if not is_valid_unit(row):
                return False

        # Check columns
        for col in zip(*board):
            if not is_valid_unit(col):
                return False

        # Check 3x3 sub-boxes
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                sub_box = [board[x][y] for x in range(i, i+3) for y in range(j, j+3)]
                if not is_valid_unit(sub_box):
                    return False

        return True
```

Time Complexity: O(1)
Space Complexity: O(1)

Explanation:

- Time Complexity: Similar to the previous solution, we make three passes through the fixed-size board. Each operation within `is_valid_unit` is O(1) due to bitwise operations. Thus, the overall time complexity remains O(1).
- Space Complexity: We only use a single integer (`seen`) as a bitmap, which uses constant space regardless of input size. Therefore, the space complexity is O(1).

Key intuitions and invariants:

- Use a bitmap (integer) to represent seen digits, where each bit corresponds to a digit (1-9).
- Bitwise AND (&) operation checks if a digit has been seen before.
- Bitwise OR (|) operation marks a digit as seen.
- This approach is memory-efficient as it uses a single integer instead of a set or array.

##### Array-based solution

```python
from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [[0] * 9 for _ in range(9)]
        cols = [[0] * 9 for _ in range(9)]
        boxes = [[0] * 9 for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    num = int(board[i][j]) - 1
                    box_index = (i // 3) * 3 + j // 3

                    # Check and update row
                    if rows[i][num]:
                        return False
                    rows[i][num] = 1

                    # Check and update column
                    if cols[j][num]:
                        return False
                    cols[j][num] = 1

                    # Check and update box
                    if boxes[box_index][num]:
                        return False
                    boxes[box_index][num] = 1

        return True
```

Time Complexity: O(1)
Space Complexity: O(1)

Explanation:

- Time Complexity: We iterate through each cell of the 9x9 board once. Since the board size is fixed, this results in a constant number of operations (81 iterations). Therefore, the time complexity is O(1).
- Space Complexity: We use three 9x9 arrays (rows, cols, boxes) to keep track of seen digits. Since these arrays have a fixed size regardless of input, the space complexity is O(1).

Key intuitions and invariants:

- Use separate 2D arrays for rows, columns, and boxes to track seen digits.
- Each inner array represents the presence (1) or absence (0) of digits 1-9.
- The box index formula `(i // 3) * 3 + j // 3` maps each cell to its corresponding 3x3 sub-box.
- Early return on finding any duplicate saves unnecessary iterations.
- This approach can be more cache-friendly than using hash sets, potentially offering better performance for larger boards.

#### Rejected Approaches

1. Brute force checking every possibility:

   - This approach would involve checking each cell against every other cell in its row, column, and 3x3 sub-box.
   - Time complexity would be O(n^4) for an nxn board, which is inefficient even for a 9x9 board.
   - Rejected because it's unnecessarily complex and slow compared to the hash set or bitmap solutions.

2. Solving the Sudoku completely:
   - This approach would involve implementing a full Sudoku solver algorithm (e.g., backtracking).
   - It's rejected because it's overkill for this problem. We only need to validate the current state, not solve the entire puzzle.
   - Solving is much more computationally expensive and complex than simple validation.

#### Final Recommendations

The single-pass hash set solution (Neetcode solution) is recommended as the best to learn for several reasons:

1. Efficiency: It solves the problem in a single pass through the board, minimizing the number of iterations.
2. Clarity: The solution is straightforward to understand and implement.

Space optimization: It uses hash sets, which provide O(1) lookup time and also help in maintaining uniqueness of elements. Here's a more detailed breakdown:

1. Memory usage:

   - We use 3 lists of sets: one for rows, one for columns, and one for 3x3 sub-boxes.
   - Each set can contain at most 9 elements (digits 1-9).
   - There are 9 rows, 9 columns, and 9 sub-boxes.
   - So, the total space used by these sets is 9 _9_ 3 = 243 elements in the worst case.

2. Constant space:

   - Regardless of the input size (which is always 9x9 for this problem), we always use the same amount of additional space.
   - This makes the space complexity O(1) or constant space.

3. Efficiency trade-off:

   - We're trading a small amount of extra space for significant time efficiency.
   - The alternative would be to check for duplicates by scanning the entire row/column/sub-box each time, which would be much slower.

4. Hash set benefits:

   - Hash sets in Python (implemented as dictionaries with dummy values) offer average-case O(1) time complexity for add and lookup operations.
   - This is crucial for maintaining the overall O(n^2) time complexity of the solution.

5. Alternative to sets:

   - We could use boolean arrays of size 9 instead of sets, which would use slightly less memory.
   - However, sets provide a more intuitive and Pythonic solution, and the space difference is negligible for this problem size.

6. Memory layout:

   - The `rows`, `cols`, and `squares` lists are essentially acting as a form of 2D hash table.
   - This layout allows us to quickly access the relevant set for any given cell using simple index calculations.

7. Flexibility: This approach can be easily adapted to different board sizes or additional validation rules.
8. Interview readiness: It demonstrates knowledge of hash sets and efficient algorithm design, which are valuable skills in coding interviews.
   By using this space-efficient data structure, we're able to validate the Sudoku board in a single pass, checking each cell exactly once. This approach strikes an excellent balance between time and space efficiency, making it an optimal solution for the Valid Sudoku problem.

While the bitmap and array-based solutions are also efficient and worth understanding, the hash set solution strikes an excellent balance between readability, efficiency, and demonstrating important concepts. It's a solution that you can quickly implement and explain in an interview setting, making it the most practical choice to learn thoroughly.

### Visualization(s)

To help visualize the single-pass hash set solution, let's create a simple ASCII representation of how the algorithm checks a Sudoku board:

```
5 3 . | . 7 . | . . .    R0: {5,3,7}
6 . . | 1 9 5 | . . .    R1: {6,1,9,5}
. 9 8 | . . . | . 6 .    R2: {9,8,6}
------+-------+------
8 . . | . 6 . | . . 3    R3: {8,6,3}
4 . . | 8 . 3 | . . 1    R4: {4,8,3,1}
7 . . | . 2 . | . . 6    R5: {7,2,6}
------+-------+------
. 6 . | . . . | 2 8 .    R6: {6,2,8}
. . . | 4 1 9 | . . 5    R7: {4,1,9,5}
. . . | . 8 . | . 7 9    R8: {8,7,9}

C0:{5,6,8,4,7}
C1:{3,9,6}
C2:{8}
C3:{1,8,4}
C4:{7,9,6,2,1,8}
C5:{5,3,9}
C6:{2}
C7:{6,8,7}
C8:{3,1,6,5,9}

B0:{5,3,6,9,8}    B1:{7,1,9,5}     B2:{6}
B3:{8,4,7}        B4:{6,8,2,3}     B5:{3,1,6}
B6:{6,2,8}        B7:{4,1,9,8}     B8:{5,7,9}
```

This visualization shows:

1. The Sudoku board
2. The contents of each row set (R0-R8)
3. The contents of each column set (C0-C8)
4. The contents of each 3x3 box set (B0-B8)

As the algorithm progresses through the board, it updates these sets and checks for duplicates. This visual representation helps understand how the algorithm keeps track of seen digits in each row, column, and 3x3 sub-box.
