# Explanation: Valid Parentheses

## Analysis of problem & input data

This problem is a classic example of string parsing and stack usage. The key characteristics of this problem are:

1. We're dealing with a string input containing only parentheses characters.
2. The problem requires matching opening and closing brackets in the correct order.
3. The input has a reasonable length constraint (1 to 10^4^), allowing for efficient solutions.

The key principle that makes this question simple is the Last-In-First-Out (LIFO) nature of parentheses matching. The last opening bracket encountered should match the next closing bracket. This naturally suggests a stack-based solution.

### Test cases

Here are some test cases to consider:

1. Valid cases:

   - `"()"`
   - `"()[]{}"`
   - `"({[]})"`
   - `""`

2. Invalid cases:

   - `"(]"`
   - `"([)]"`
   - `"]"`
   - `"("`
   - `"(("`

3. Edge cases:
   - Empty string
   - String with only opening brackets
   - String with only closing brackets
   - Very long string of valid parentheses

Here's the Python code for these test cases:

```python
def test_valid_parentheses(func):
    test_cases = [
        ("()", True),
        ("()[]{}", True),
        ("({[]})", True),
        ("", True),
        ("(]", False),
        ("([)]", False),
        ("]", False),
        ("(", False),
        ("((", False),
        ("" * 10000, True),
        ("(" * 5000 + ")" * 5000, True),
        (")" * 5000 + "(" * 5000, False)
    ]

    for i, (s, expected) in enumerate(test_cases):
        result = func(s)
        print(f"Test case {i+1}: {'Passed' if result == expected else 'Failed'}")
        if result != expected:
            print(f"  Input: {s}")
            print(f"  Expected: {expected}")
            print(f"  Got: {result}")

# Usage:
# test_valid_parentheses(is_valid)
```

## Solutions

### Overview of solution approaches

#### Solutions worth learning

1. Stack-based approach
2. Counter-based approach

Count: 2 solutions

#### Rejected solutions

1. Recursive approach: While possible, it's less efficient and more complex than iterative solutions for this problem.
2. Regular expression: While it can work for simple cases, it becomes complex for nested parentheses and is generally less efficient.

### Worthy Solutions

#### 1. Stack-based approach

```python
from typing import List

def is_valid(s: str) -> bool:
    # Dictionary to map closing brackets to their corresponding opening brackets
    bracket_map = {")": "(", "]": "[", "}": "{"}

    # Stack to keep track of opening brackets
    stack: List[str] = []

    for char in s:
        if char not in bracket_map:
            # If it's an opening bracket, push onto the stack
            stack.append(char)
        elif not stack or stack[-1] != bracket_map[char]:
            # If it's a closing bracket and either the stack is empty
            # or the last opening bracket doesn't match, it's invalid
            return False
        else:
            # If it's a closing bracket and matches the last opening bracket,
            # pop the opening bracket from the stack
            stack.pop()

    # The string is valid if all brackets have been matched and closed
    return len(stack) == 0
```

Time Complexity: O(n), where n is the length of the string.
Space Complexity: O(n) in the worst case, where all characters are opening brackets.

Key intuitions and invariants:

- The stack always contains only opening brackets.
- The top of the stack always represents the most recently encountered unclosed opening bracket.
- If we encounter a closing bracket, it must match the most recent opening bracket (top of the stack).
- After processing all characters, a valid string will have an empty stack.

#### 2. Counter-based approach

```python
def is_valid(s: str) -> bool:
    # Initialize counters for each type of bracket
    round_brackets = square_brackets = curly_brackets = 0

    for char in s:
        if char == '(':
            round_brackets += 1
        elif char == ')':
            round_brackets -= 1
        elif char == '[':
            square_brackets += 1
        elif char == ']':
            square_brackets -= 1
        elif char == '{':
            curly_brackets += 1
        elif char == '}':
            curly_brackets -= 1

        # If any counter becomes negative, we've encountered a closing bracket
        # without a corresponding opening bracket
        if round_brackets < 0 or square_brackets < 0 or curly_brackets < 0:
            return False

    # All counters should be zero for a valid string
    return round_brackets == 0 and square_brackets == 0 and curly_brackets == 0
```

Time Complexity: O(n), where n is the length of the string.
Space Complexity: O(1), as we use a constant number of counters.

Key intuitions and invariants:

- Each type of bracket is tracked independently.
- The count for each bracket type should never go negative.
- At the end, all counts should be zero for a valid string.
- This approach doesn't check for proper nesting order, only overall balance.

### Rejected Approaches

1. Recursive approach: While it's possible to solve this problem recursively by checking if the first and last characters match and then recursively checking the substring between them, this approach is less efficient (O(n^2) time complexity in the worst case) and more complex than the iterative solutions.

2. Regular expression: A regex like `^(\()?\[?\{?(?(1)\))?(?(2)])?)?)(?(3)})?$` could potentially solve simple cases, but it becomes extremely complex for nested parentheses and is generally less efficient and harder to understand and maintain than the algorithmic solutions.

### Final Recommendations

The stack-based approach is the best solution to learn for this problem. It efficiently handles all cases, including nested parentheses, and clearly demonstrates understanding of both the problem and data structures.

The counter-based approach, while simple and efficient, doesn't check for proper nesting order (e.g., it would incorrectly validate "([)]"). It's worth understanding but not as robust as the stack-based solution.

The recursive and regex approaches, while theoretically possible, are overly complex for this problem and not recommended in an interview setting.

## Visualization(s)

Here's a simple visualization of how the stack-based approach works:

```
Input: "{[]}"

Step 1: {       Step 2: {[      Step 3: {[]     Step 4: {[      Step 5: {       Step 6: (empty)
        |               | |             | |             |               |
        V               V V             V V             V               V
       ['{']           ['{','[']       ['{','[']      ['{']           []              []

Stack:  {                {[              {[             {                (empty)        (empty)
```

This visualization shows how opening brackets are pushed onto the stack, and closing brackets cause matching opening brackets to be popped off. A valid string results in an empty stack at the end.
