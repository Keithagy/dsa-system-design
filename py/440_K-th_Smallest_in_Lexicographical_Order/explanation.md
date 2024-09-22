## Explanation: Kth Smallest Number in Lexicographical Order

### Analysis of problem & input data

This problem is about understanding lexicographical order and efficiently finding the kth element in this order within a given range. The key characteristics of the problem are:

1. Lexicographical order: Numbers are ordered as strings, not by their numeric value.
2. Large input range: n can be up to 10^9, making brute force approaches infeasible.
3. The order follows a pattern similar to a 10-ary tree (each node has up to 10 children).

The key principle that makes this question simple is recognizing that lexicographical order forms a tree-like structure. This allows us to use a tree traversal approach without actually building the tree.

Pattern matching: This problem maps to:

1. Tree traversal (specifically, preorder traversal of a 10-ary tree)
2. Counting nodes in a tree
3. Skip counting / Branch pruning

The optimal solution leverages the tree-like structure of lexicographical order to efficiently count and skip nodes, avoiding the need to generate all numbers explicitly.

### Test cases

1. Edge cases:

   - n = 1, k = 1 (minimum possible input)
   - n = 10^9, k = 1 (first element with maximum n)
   - n = 10^9, k = 10^9 (last element with maximum n and k)

2. Challenging inputs:

   - n = 100, k = 10 (crosses from single-digit to double-digit numbers)
   - n = 1000, k = 200 (requires skipping some branches)

3. Additional test cases:
   - n = 13, k = 2 (given example)
   - n = 100, k = 5 (includes skipping some single-digit numbers)

Here's the code for these test cases:

```python
def kth_lexicographical_number(n: int, k: int) -> int:
    # Implementation will be provided in the solutions section

# Test cases
test_cases = [
    (1, 1),
    (10**9, 1),
    (10**9, 10**9),
    (100, 10),
    (1000, 200),
    (13, 2),
    (100, 5)
]

for n, k in test_cases:
    result = kth_lexicographical_number(n, k)
    print(f"n = {n}, k = {k}: {result}")
```

### Solutions

#### Overview of solution approaches

##### Solutions worth learning

1. Tree traversal with counting (Neetcode solution)
2. Binary search on the lexicographical order
3. Math-based solution using digit-by-digit construction

Count: 3 solutions (1 Neetcode solution)

##### Rejected solutions

1. Brute force generation of all numbers and sorting
2. Recursive tree traversal without pruning

#### Worthy Solutions

##### Tree traversal with counting

```python
def findKthNumber(n: int, k: int) -> int:
    def count_numbers(prefix: int, n: int) -> int:
        count = 0
        current, next = prefix, prefix + 1
        while current <= n:
            count += min(n + 1, next) - current
            current *= 10
            next *= 10
        return count

    current = 1
    k -= 1  # We start from 1, so we need to find the (k-1)th number after 1

    while k > 0:
        count = count_numbers(current, n)
        if k >= count:
            k -= count
            current += 1
        else:
            k -= 1
            current *= 10

    return current
```

Time Complexity: O(log(n) \* log(n))

- The outer while loop runs at most log(n) times because in each iteration, we either move to the next sibling (incrementing by 1) or to the first child (multiplying by 10).
- The `count_numbers` function also takes O(log(n)) time because it's dealing with powers of 10 up to n.

Space Complexity: O(1)

- We only use a constant amount of extra space for variables.

Intuitions and invariants:

- The lexicographical order forms a 10-ary tree structure.
- We can count the number of nodes in a subtree without generating all numbers.
- By comparing the count with k, we can decide whether to go to the next sibling or dive deeper into the current subtree.
- The `count_numbers` function efficiently calculates the number of nodes in a subtree.
- We keep track of the current prefix and adjust k as we traverse the tree.

This solution is optimal because it avoids generating all numbers explicitly and uses the tree structure to efficiently navigate to the kth number.

##### Binary search on the lexicographical order

```python
def findKthNumber(n: int, k: int) -> int:
    def lexicographical_rank(x: int) -> int:
        rank = 0
        start, end = x, x + 1
        while start <= n:
            rank += min(n + 1, end) - start
            start *= 10
            end *= 10
        return rank

    left, right = 1, n
    while left < right:
        mid = (left + right) // 2
        if lexicographical_rank(mid) >= k:
            right = mid
        else:
            left = mid + 1
    return left
```

Time Complexity: O(log(n) \* log(n))

- The binary search takes O(log(n)) iterations.
- In each iteration, `lexicographical_rank` takes O(log(n)) time.

Space Complexity: O(1)

- We only use a constant amount of extra space for variables.

Intuitions and invariants:

- The lexicographical rank of a number is monotonically increasing.
- We can use binary search to find the number with rank k.
- The `lexicographical_rank` function efficiently calculates the rank of a number in the lexicographical order.
- We maintain the invariant that the kth number is always within the [left, right] range.

This solution is a different perspective on the problem, leveraging the monotonicity of lexicographical rank to perform a binary search.

##### Math-based solution using digit-by-digit construction

```python
def findKthNumber(n: int, k: int) -> int:
    def count_prefix(prefix: int, n: int) -> int:
        count = 0
        for i in range(10):
            if prefix * 10 + i > n:
                break
            count += 1
        return count

    result = 0
    remaining = k

    while remaining > 0:
        for digit in range(10):
            if result == 0 and digit == 0:
                continue
            count = count_prefix(result * 10 + digit, n)
            if remaining <= count:
                result = result * 10 + digit
                remaining -= 1
                break
            remaining -= count

    return result
```

Time Complexity: O(log(n) \* log(n))

- We construct the number digit by digit, taking at most log(n) iterations.
- In each iteration, `count_prefix` takes O(log(n)) time.

Space Complexity: O(1)

- We only use a constant amount of extra space for variables.

Intuitions and invariants:

- We can construct the kth number digit by digit.
- For each prefix, we count how many numbers with that prefix are within the range [1, n].
- We maintain the invariant that `remaining` represents the remaining rank we need to find within the current prefix.
- The `count_prefix` function efficiently calculates how many numbers with a given prefix are within the range [1, n].

This solution takes a more mathematical approach, directly constructing the kth number by making decisions digit by digit based on the count of valid numbers with each prefix.

#### Rejected Approaches

1. Brute force generation and sorting:

   - Generate all numbers from 1 to n, sort them lexicographically, and return the kth element.
   - Rejected because: Time and space complexity of O(n log n), which is infeasible for large n (up to 10^9).

2. Recursive tree traversal without pruning:

   - Perform a full recursive traversal of the lexicographical tree.
   - Rejected because: Time complexity of O(n), which is too slow for large inputs.

3. Dynamic Programming:
   - While DP can solve some lexicographical problems, it's not suitable here due to the large input range and the nature of the problem.
   - Rejected because: Would require O(n) space and time, which is infeasible for large n.

#### Final Recommendations

The tree traversal with counting approach (Neetcode solution) is the best to learn for this problem. It offers the optimal balance of:

1. Efficiency: O(log(n) \* log(n)) time complexity with O(1) space.
2. Intuitive understanding: It directly maps to the tree-like structure of lexicographical order.
3. Implementation simplicity: The code is relatively straightforward once you understand the concept.

This solution also demonstrates important problem-solving skills:

- Recognizing underlying data structures (tree-like structure in this case)
- Efficient counting and skipping techniques
- Leveraging problem constraints to optimize the solution

Understanding this approach will help with similar problems involving lexicographical order or tree-like structures with large input ranges.

### Visualization(s)

To visualize the tree traversal approach, we can represent the lexicographical order as a 10-ary tree:

```
       1        2        3    ...    9
    /  |  \
   10 11  12 ...  19
  /|\
100 101 102 ... 109
```

```tsx
import React from "react";

const TreeNode = ({ value, children }) => (
  <div className="flex flex-col items-center">
    <div className="border rounded-full w-10 h-10 flex items-center justify-center mb-2">
      {value}
    </div>
    {children && <div className="flex space-x-2">{children}</div>}
  </div>
);

const LexicographicalTree = () => (
  <div className="p-4">
    <h3 className="text-lg font-bold mb-4">Lexicographical Tree</h3>
    <div className="flex justify-center space-x-4">
      <TreeNode value={1}>
        <TreeNode value={10}>
          <TreeNode value={100} />
          <TreeNode value={101} />
          <TreeNode value={"..."} />
        </TreeNode>
        <TreeNode value={11} />
        <TreeNode value={"..."} />
      </TreeNode>
      <TreeNode value={2} />
      <TreeNode value={3} />
      <TreeNode value={"..."} />
      <TreeNode value={9} />
    </div>
  </div>
);

export default LexicographicalTree;
```

This visualization helps to understand how the tree traversal algorithm navigates the lexicographical order. The algorithm efficiently moves through this tree structure, counting nodes in subtrees to determine whether to move to the next sibling or dive deeper into the current subtree.
