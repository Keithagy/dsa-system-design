# Explanation: Evaluate Reverse Polish Notation

## Analysis of problem & input data

This problem involves evaluating an arithmetic expression in Reverse Polish Notation (RPN), also known as postfix notation. The key characteristics and insights of this problem are:

1. RPN eliminates the need for parentheses by using a stack-based approach.
2. Operands come before operators in RPN.
3. When an operator is encountered, it applies to the two most recent operands.
4. The problem involves basic arithmetic operations: addition, subtraction, multiplication, and division.
5. Division between integers always truncates toward zero.
6. The input is guaranteed to be a valid RPN expression.
7. All calculations can be represented in a 32-bit integer, which simplifies our approach.
8. The input is an array of strings, where each string is either an operator or an integer.

The key principle that makes this question simple is the natural fit between RPN and stack data structures. As we process the tokens from left to right, we can push operands onto a stack and perform operations when we encounter operators, which perfectly mimics the evaluation process of RPN.

### Test cases

Here are some test cases to cover various scenarios:

1. Basic operations:

   - Input: ["2", "1", "+", "3", "*"]
   - Expected Output: 9

2. Division with truncation:

   - Input: ["4", "13", "5", "/", "+"]
   - Expected Output: 6

3. Complex expression with negative numbers:

   - Input: ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
   - Expected Output: 22

4. Single number:

   - Input: ["42"]
   - Expected Output: 42

5. Negative result:

   - Input: ["5", "3", "-"]
   - Expected Output: 2

6. Zero division (not actually possible according to constraints, but good to consider):
   - Input: ["1", "0", "/"]
   - Expected Output: Error or undefined behavior

Here's the Python code to implement these test cases:

```python
def evaluate_rpn(tokens):
    # Implementation goes here
    pass

# Test cases
test_cases = [
    (["2", "1", "+", "3", "*"], 9),
    (["4", "13", "5", "/", "+"], 6),
    (["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"], 22),
    (["42"], 42),
    (["5", "3", "-"], 2),
    # Uncomment the following line to test division by zero (not actually possible in this problem)
    # (["1", "0", "/"], "Error"),
]

for i, (input_tokens, expected_output) in enumerate(test_cases):
    result = evaluate_rpn(input_tokens)
    print(f"Test case {i + 1}: {'Passed' if result == expected_output else 'Failed'}")
    print(f"Input: {input_tokens}")
    print(f"Expected: {expected_output}")
    print(f"Got: {result}\n")
```

## Solutions

### Overview of solution approaches

#### Solutions worth learning

1. Stack-based approach
2. Stack-based approach with lambda functions

Count: 2 solutions

#### Rejected solutions

1. Building a binary expression tree
2. Recursive approach
3. Using eval() function (insecure and not suitable for interviews)

### Worthy Solutions

#### 1. Stack-based approach

```python
from typing import List

def evalRPN(tokens: List[str]) -> int:
    stack = []
    operators = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: int(a / b)  # Use int() for truncation towards zero
    }

    for token in tokens:
        if token in operators:
            # Pop the two most recent operands
            b, a = stack.pop(), stack.pop()
            # Apply the operator and push the result back to the stack
            stack.append(operators[token](a, b))
        else:
            # If it's not an operator, it's an operand. Push it to the stack
            stack.append(int(token))

    # The final result will be the only item left in the stack
    return stack[0]
```

Time Complexity: O(n), where n is the number of tokens
Space Complexity: O(n) in the worst case, where the expression consists only of numbers

Intuition and invariants:

- We use a stack to keep track of operands
- When we encounter an operator, we know it applies to the two most recent operands
- The stack always contains intermediate results or operands waiting to be used
- After processing all tokens, the stack will contain only the final result

#### 2. Stack-based approach with lambda functions

```python
from typing import List

def evalRPN(tokens: List[str]) -> int:
    stack = []
    operators = {
        '+': lambda: stack.append(stack.pop(-2) + stack.pop()),
        '-': lambda: stack.append(stack.pop(-2) - stack.pop()),
        '*': lambda: stack.append(stack.pop(-2) * stack.pop()),
        '/': lambda: stack.append(int(stack.pop(-2) / stack.pop()))
    }

    for token in tokens:
        if token in operators:
            operators[token]()
        else:
            stack.append(int(token))

    return stack[0]
```

Time Complexity: O(n), where n is the number of tokens
Space Complexity: O(n) in the worst case, where the expression consists only of numbers

Intuition and invariants:

- Similar to the first approach, but uses lambda functions to encapsulate the operation logic
- The lambda functions directly manipulate the stack, reducing the need for explicit pop and push operations
- This approach is more concise but might be slightly less readable for some

### Rejected Approaches

1. Building a binary expression tree:

   - While this approach would work, it's overly complex for this problem
   - It would require more time and space than necessary
   - RPN already gives us the order of operations, so a tree structure is redundant

2. Recursive approach:

   - Could work by recursively evaluating sub-expressions
   - However, it would be less efficient and more complex than the stack-based approach
   - Might lead to stack overflow for very large expressions

3. Using eval() function:
   - While tempting for its simplicity, it's considered unsafe as it can execute arbitrary code
   - It doesn't demonstrate understanding of the problem or data structures
   - Not suitable for coding interviews or production code

### Final Recommendations

The stack-based approach (Solution 1) is the best one to learn and implement. It's efficient, straightforward, and directly mimics the evaluation process of Reverse Polish Notation. It demonstrates a good understanding of both the problem and the use of appropriate data structures.

The stack-based approach with lambda functions (Solution 2) is a more concise variation but might be slightly less readable. It's worth knowing but perhaps not as the primary solution.

Avoid approaches that seem to overcomplicate the problem, like building expression trees or using recursion. These might seem tempting given the arithmetic nature of the problem, but they don't leverage the simplicity that RPN provides.

Remember that while using eval() might seem like a quick solution, it's generally frowned upon in coding interviews and real-world applications due to security concerns and because it doesn't demonstrate problem-solving skills.

## Visualization(s)

To visualize how the stack-based approach works, let's create a simple step-by-step visualization for the example: ["2", "1", "+", "3", "*"]

```tsx
import React, { useState } from "react";
import { Card, CardContent, CardHeader } from "@/components/ui/card";
import { Button } from "@/components/ui/button";

const RPNVisualization = () => {
  const [step, setStep] = useState(0);
  const tokens = ["2", "1", "+", "3", "*"];
  const steps = [
    { stack: [], current: "2" },
    { stack: ["2"], current: "1" },
    { stack: ["2", "1"], current: "+" },
    { stack: ["3"], current: "3" },
    { stack: ["3", "3"], current: "*" },
    { stack: ["9"], current: "Done" },
  ];

  const nextStep = () =>
    setStep((prev) => Math.min(prev + 1, steps.length - 1));
  const prevStep = () => setStep((prev) => Math.max(prev - 1, 0));

  return (
    <div className="flex flex-col items-center space-y-4">
      <Card className="w-full max-w-md">
        <CardHeader>RPN Evaluation: {tokens.join(" ")}</CardHeader>
        <CardContent>
          <div className="flex justify-between items-center mb-4">
            <Button onClick={prevStep} disabled={step === 0}>
              Previous
            </Button>
            <span>
              Step {step + 1} of {steps.length}
            </span>
            <Button onClick={nextStep} disabled={step === steps.length - 1}>
              Next
            </Button>
          </div>
          <div className="flex justify-between items-center">
            <div className="border p-2 w-1/2">
              <h3 className="text-lg font-bold mb-2">Stack</h3>
              {steps[step].stack.map((item, index) => (
                <div key={index} className="bg-gray-100 p-1 mb-1">
                  {item}
                </div>
              ))}
            </div>
            <div className="border p-2 w-1/3">
              <h3 className="text-lg font-bold mb-2">Current Token</h3>
              <div className="bg-blue-100 p-1">{steps[step].current}</div>
            </div>
          </div>
        </CardContent>
      </Card>
    </div>
  );
};

export default RPNVisualization;
```

This visualization shows how the stack changes as we process each token in the RPN expression. You can step through the evaluation process to see how numbers are pushed onto the stack and how operators consume numbers from the stack to produce results.
