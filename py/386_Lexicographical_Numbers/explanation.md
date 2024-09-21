## Explanation: Lexicographical Numbers

### Analysis of problem & input data

This problem asks us to generate numbers from 1 to n in lexicographical order, which is the order words would appear in a dictionary. The key insight here is understanding how lexicographical order works for numbers:

1. Numbers are compared digit by digit from left to right.
2. Shorter numbers come before longer numbers that start with the same digits.
3. The order is: 1, 10, 100, 1000, ..., 11, 110, 1100, ..., 12, 120, 1200, ..., 2, 20, 200, ...

The constraint of O(n) time and O(1) space complexity is crucial. It rules out sorting-based approaches and requires us to generate the numbers in the correct order directly.

The key principle that makes this question simple is that lexicographical order for numbers follows a depth-first search (DFS) pattern on a decimal tree. This insight allows us to generate the numbers in order without actually building or storing the tree.

### Test cases

1. n = 1 (minimum input)
2. n = 13 (as given in the example)
3. n = 100 (to test three-digit numbers)
4. n = 5 \* 10^4 (maximum input)
5. n = 20 (to test the transition from 19 to 2)

Here's the code to run these test cases:

```python
def lexicalOrder(n: int) -> List[int]:
    # Implementation will be added here

# Test cases
test_cases = [1, 13, 100, 50000, 20]
for case in test_cases:
    print(f"n = {case}:")
    print(lexicalOrder(case))
    print()
```

### Solutions

#### Overview of solution approaches

##### Solutions worth learning

1. Iterative DFS (Neetcode solution) - Most intuitive and efficient
2. Recursive DFS - Elegant but potentially prone to stack overflow for large n
3. Preorder traversal simulation - Alternative perspective on the problem

Count: 3 solutions (1 Neetcode solution)

##### Rejected solutions

1. Sorting-based approach - Violates the O(n) time complexity requirement
2. Generation and conversion to strings - Violates the O(1) space complexity requirement

#### Worthy Solutions

##### Iterative DFS (Neetcode solution)

```python
def lexicalOrder(n: int) -> List[int]:
    result = []
    current = 1
    for _ in range(n):
        result.append(current)
        if current * 10 <= n:
            current *= 10
        else:
            if current >= n:
                current //= 10
            current += 1
            while current % 10 == 0:
                current //= 10
    return result
```

Time Complexity: O(n)

- We iterate exactly n times, performing O(1) operations in each iteration.

Space Complexity: O(1) (excluding the output array)

- We only use a constant amount of extra space (the `current` variable).

Intuition and invariants:

- We simulate DFS traversal on a decimal tree without actually building the tree.
- `current` represents the current number we're considering.
- Multiplying by 10 simulates going deeper into the tree (e.g., from 1 to 10).
- When we can't go deeper, we increment and handle carry-over (e.g., from 19 to 2).
- The algorithm maintains the invariant that `current` is always the next lexicographical number.

##### Recursive DFS

```python
def lexicalOrder(n: int) -> List[int]:
    def dfs(current: int, limit: int, result: List[int]) -> None:
        if current > limit:
            return
        result.append(current)
        for i in range(10):
            dfs(current * 10 + i, limit, result)

    result = []
    for i in range(1, 10):
        dfs(i, n, result)
    return result
```

Time Complexity: O(n)

- We visit each number exactly once, performing O(1) operations for each.

Space Complexity: O(log n) due to the recursion stack

- The maximum depth of recursion is log_10(n), as we add one digit at a time.

Intuition and invariants:

- We explicitly perform a DFS on the decimal tree.
- The recursive calls maintain the lexicographical order naturally.
- We start with digits 1-9 and recursively explore their children.
- The base case is when the current number exceeds n.

##### Preorder traversal simulation

```python
def lexicalOrder(n: int) -> List[int]:
    result = []
    stack = []
    num = 1

    while len(result) < n:
        result.append(num)
        if num * 10 <= n:
            stack.append(num)
            num *= 10
        else:
            while num % 10 == 9 or num + 1 > n:
                if not stack:
                    return result
                num = stack.pop()
            num += 1

    return result
```

Time Complexity: O(n)

- We generate exactly n numbers, performing O(1) operations for each.

Space Complexity: O(log n)

- The stack can grow up to log_10(n) elements in the worst case.

Intuition and invariants:

- We simulate a preorder traversal of the decimal tree.
- The stack keeps track of parent nodes (numbers) we need to return to.
- We always try to go deeper (multiply by 10) if possible.
- When we can't go deeper, we backtrack and increment, simulating moving to the next sibling in the tree.

#### Rejected Approaches

1. Sorting-based approach:
   Generating all numbers and then sorting them lexicographically would take O(n log n) time, violating the time complexity requirement.

2. Generation and conversion to strings:
   Converting numbers to strings for comparison would require O(n log n) space, violating the space complexity requirement.

3. Using built-in sorting with a custom comparator:
   This would also violate both time and space complexity requirements.

#### Final Recommendations

The iterative DFS approach (Neetcode solution) is the best to learn for this problem. It's the most efficient in terms of both time and space complexity, meeting the problem's requirements exactly. It's also more intuitive once you understand the decimal tree concept, and it avoids the potential stack overflow issues of the recursive approach for large n values.

### Visualization(s)

To visualize the decimal tree and the DFS traversal, we can use a simple ASCII representation:

```
       1
    /  |  \
   10 11  12 ...
  /
100
```

This tree structure helps understand how the iterative DFS algorithm works:

1. Start at 1
2. Go deep (1 -> 10 -> 100) until we exceed n
3. Backtrack and increment (100 -> 101, or if > n, 10 -> 11)
4. Repeat until all numbers up to n are generated

This visualization can be helpful in understanding the pattern of lexicographical order and how the algorithm traverses the implicit decimal tree structure.
