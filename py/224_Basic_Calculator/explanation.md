## Explanation: Basic Calculator

### Analysis of problem & input data

This problem is a classic example of expression evaluation, specifically dealing with arithmetic expressions involving addition, subtraction, and parentheses. The key characteristics of this problem are:

1. The input is a string representing a valid mathematical expression.
2. The expression can contain digits, '+', '-', '(', ')', and spaces.
3. The expression can have nested parentheses.
4. We need to handle both binary (e.g., "1+2") and unary (e.g., "-1") operations.
5. The evaluation should follow the standard order of operations (PEMDAS), where parentheses have the highest precedence.

The primary challenge in this problem is handling the parentheses, which can be nested to arbitrary depths. This naturally suggests a stack-based approach or a recursive approach, both of which are well-suited for handling nested structures.

The key principle that makes this question solvable is the concept of operator precedence and the use of a stack to manage nested expressions. By using a stack, we can effectively "pause" the evaluation of an outer expression while we evaluate an inner expression enclosed in parentheses.

### Test cases

Here are some relevant test cases:

1. Basic addition and subtraction: "1 + 1" (Output: 2)
2. Expression with spaces: " 2-1 + 2 " (Output: 3)
3. Nested parentheses: "(1+(4+5+2)-3)+(6+8)" (Output: 23)
4. Unary minus: "-1 + (2 + 3)" (Output: 4)
5. Multiple unary minuses: "- - 1" (Output: 1)
6. Expression starting with parentheses: "(1)" (Output: 1)
7. Complex nested expression: "2-4-(8+2-6+(8+4-(1)+8-10))" (Output: -15)

Here's the code to run these test cases:

```python
def calculate(s: str) -> int:
    # Implementation will be provided in the solution section

# Test cases
test_cases = [
    "1 + 1",
    " 2-1 + 2 ",
    "(1+(4+5+2)-3)+(6+8)",
    "-1 + (2 + 3)",
    "- - 1",
    "(1)",
    "2-4-(8+2-6+(8+4-(1)+8-10))"
]

for case in test_cases:
    print(f"Input: {case}")
    print(f"Output: {calculate(case)}")
    print()
```

### Solutions

#### Overview of solution approaches

##### Solutions worth learning

1. Stack-based approach (Neetcode solution)
2. Recursive approach
3. Two-stack approach

Count: 3 solutions (1 Neetcode solution)

##### Rejected solutions

1. Using eval() function: This is explicitly forbidden by the problem statement.
2. Building a full abstract syntax tree (AST): While this would work, it's overly complex for this problem and not time-efficient for an interview setting.
3. Shunting yard algorithm: While this is a classic algorithm for expression parsing, it's more complex than necessary for this problem, which doesn't involve operator precedence beyond parentheses.

#### Worthy Solutions

##### Stack-based approach (Neetcode solution)

```python
def calculate(s: str) -> int:
    stack = []
    num = 0
    sign = 1
    result = 0

    for char in s:
        if char.isdigit():
            num = num * 10 + int(char)
        elif char in ['+', '-']:
            result += sign * num
            num = 0
            sign = 1 if char == '+' else -1
        elif char == '(':
            stack.append(result)
            stack.append(sign)
            result = 0
            sign = 1
        elif char == ')':
            result += sign * num
            result *= stack.pop()
            result += stack.pop()
            num = 0

    return result + sign * num
```

Time Complexity: O(n), where n is the length of the input string. We iterate through each character in the string once.
Space Complexity: O(n) in the worst case, where the expression is deeply nested with parentheses. In the average case, it's much less.

Explanation:

- We use a single stack to keep track of intermediate results and signs when encountering nested parentheses.
- We maintain a running `result` and a `sign` to handle the current operation.
- For digits, we build up the number (`num`) digit by digit.
- When we encounter '+' or '-', we update the result with the previous number and reset for the next number.
- When we encounter '(', we push the current result and sign onto the stack and reset both.
- When we encounter ')', we finalize the current result, multiply it by the sign from the stack, and add it to the result from the stack.

This approach is elegant because it handles nested parentheses without explicit recursion, using the stack to "remember" the outer context when diving into nested expressions.

##### Recursive approach

```python
def calculate(s: str) -> int:
    def eval_expr(index: int) -> tuple[int, int]:
        result = 0
        num = 0
        sign = 1

        while index < len(s):
            char = s[index]
            if char.isdigit():
                num = num * 10 + int(char)
            elif char in ['+', '-']:
                result += sign * num
                num = 0
                sign = 1 if char == '+' else -1
            elif char == '(':
                num, index = eval_expr(index + 1)
            elif char == ')':
                break
            index += 1

        return result + sign * num, index

    return eval_expr(0)[0]
```

Time Complexity: O(n), where n is the length of the input string. We process each character once.
Space Complexity: O(n) in the worst case due to the call stack for deeply nested expressions.

Explanation:

- We use a recursive approach where each call to `eval_expr` evaluates an expression until it encounters a closing parenthesis or the end of the string.
- The function returns both the result of the expression and the index where it stopped processing.
- We handle numbers, signs, and opening parentheses similarly to the stack-based approach.
- When we encounter an opening parenthesis, we make a recursive call to evaluate the nested expression.
- The base case is when we encounter a closing parenthesis or reach the end of the string.

This approach is intuitive because it directly mirrors the nested structure of the expression. Each recursive call corresponds to evaluating a nested subexpression.

##### Two-stack approach

```python
from collections import deque

def calculate(s: str) -> int:
    nums = deque()
    ops = deque()
    num = 0

    def apply_op():
        right = nums.pop()
        left = nums.pop()
        op = ops.pop()
        if op == '+':
            nums.append(left + right)
        else:  # op == '-'
            nums.append(left - right)

    for i, char in enumerate(s):
        if char.isdigit():
            num = num * 10 + int(char)
        elif char in ['+', '-']:
            nums.append(num)
            num = 0
            while ops and ops[-1] != '(':
                apply_op()
            ops.append(char)
        elif char == '(':
            ops.append(char)
        elif char == ')':
            nums.append(num)
            num = 0
            while ops[-1] != '(':
                apply_op()
            ops.pop()  # Remove '('

    nums.append(num)
    while ops:
        apply_op()

    return nums[0]
```

Time Complexity: O(n), where n is the length of the input string. We process each character once.
Space Complexity: O(n) for the stacks in the worst case of deeply nested expressions.

Explanation:

- We use two stacks: one for numbers and one for operators.
- We process the expression left to right, building up numbers digit by digit.
- When we encounter an operator or closing parenthesis, we evaluate all pending operations of equal or higher precedence.
- The `apply_op` function applies the top operation to the top two numbers on the stack.
- Parentheses are handled by treating '(' as an operator with lowest precedence, and evaluating all operations when we encounter ')' until we find the matching '('.

This approach is more general and can be extended to handle more operators with different precedences. It's a simplified version of the shunting yard algorithm.

#### Rejected Approaches

1. Using eval() function: This is explicitly forbidden by the problem statement. While it would provide a quick solution, it doesn't demonstrate understanding of expression evaluation algorithms and can be dangerous if used on untrusted input.

2. Building a full abstract syntax tree (AST): While this would work and is a common approach in compiler design, it's overly complex for this problem. It would involve creating node classes for different expression types, building the tree, and then evaluating it. This is time-consuming in an interview setting and doesn't provide significant benefits over the stack-based or recursive approaches for this specific problem.

3. Shunting yard algorithm: This algorithm is typically used for expressions with multiple operators of different precedences. While it would work for this problem, it's more complex than necessary since we only need to handle addition, subtraction, and parentheses. The stack-based and recursive approaches are simpler and equally effective for this specific case.

#### Final Recommendations

For this problem, I would recommend learning the stack-based approach (the Neetcode solution) as the primary solution. It's elegant, efficient, and demonstrates a good understanding of how to use a stack to handle nested structures. It's also relatively easy to explain and implement in an interview setting.

The recursive approach is also worth understanding as it provides a different perspective on the problem and can be more intuitive for some people. It directly mirrors the structure of the expression, which can make it easier to reason about.

The two-stack approach, while valid, is more complex than necessary for this specific problem. However, it's worth knowing about if you're interested in how to handle more complex expressions with multiple operator precedences.

### Visualization(s)

To visualize the stack-based approach, we can use a simple ASCII art representation of the stack as we process the expression "(1+(4+5+2)-3)+(6+8)":

```
Expression: (1+(4+5+2)-3)+(6+8)
Step | Char | Stack    | Result | Num | Sign
-----+------+----------+--------+-----+-----
0    | (    | [0, 1]   | 0      | 0   | 1
1    | 1    | [0, 1]   | 0      | 1   | 1
2    | +    | [0, 1]   | 1      | 0   | 1
3    | (    | [0, 1, 1, 1] | 0  | 0   | 1
4    | 4    | [0, 1, 1, 1] | 0  | 4   | 1
5    | +    | [0, 1, 1, 1] | 4  | 0   | 1
6    | 5    | [0, 1, 1, 1] | 4  | 5   | 1
7    | +    | [0, 1, 1, 1] | 9  | 0   | 1
8    | 2    | [0, 1, 1, 1] | 9  | 2   | 1
9    | )    | [0, 1]   | 12     | 0   | 1
10   | -    | [0, 1]   | 12     | 0   | -1
11   | 3    | [0, 1]   | 12     | 3   | -1
12   | )    | []       | 9      | 0   | 1
13   | +    | []       | 9      | 0   | 1
14   | (    | [9, 1]   | 0      | 0   | 1
15   | 6    | [9, 1]   | 0      | 6   | 1
16   | +    | [9, 1]   | 6      | 0   | 1
17   | 8    | [9, 1]   | 6      | 8   | 1
18   | )    | []       | 23     | 0   | 1

Final Result: 23
```

This visualization shows how the stack, result, current number, and sign change as we process each character of the expression. It helps illustrate how the stack is used to handle nested parentheses and how the running result is updated at each step.
