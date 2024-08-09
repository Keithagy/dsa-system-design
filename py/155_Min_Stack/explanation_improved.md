# Explanation: Min Stack

## Analysis of problem & input data

This problem requires us to implement a stack with additional functionality to retrieve the minimum element in constant time. The key aspects to consider are:

1. Stack operations: The basic stack operations (push, pop, top) must be implemented.
2. Minimum element retrieval: We need to keep track of the minimum element at all times.
3. Time complexity: All operations, including getMin, must be O(1).
4. Space complexity: While not explicitly stated, an efficient solution in terms of space is desirable.
5. Input range: The values can be any 32-bit integer, which means we need to handle a wide range of numbers.
6. Non-empty guarantee: We're assured that pop, top, and getMin will only be called on non-empty stacks.
7. Number of operations: The stack should handle up to 3 \* 10^4 operations efficiently.

The key principle that makes this question solvable in O(1) time for all operations is the realization that we can maintain a separate stack of minimums alongside our main stack. This auxiliary stack will always have its top element as the current minimum of the main stack.

## Solutions

### Solution 1: Two-Stack Approach

This solution uses two stacks: one for the actual values and another for tracking minimums.

```python
from typing import List

class MinStack:
    def __init__(self):
        self.stack: List[int] = []  # Main stack to store all elements
        self.min_stack: List[int] = []  # Auxiliary stack to track minimums

    def push(self, val: int) -> None:
        self.stack.append(val)
        # If min_stack is empty or val is smaller than or equal to the current minimum,
        # push it to min_stack
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        # If the popped element is the current minimum, remove it from min_stack too
        if self.stack[-1] == self.min_stack[-1]:
            self.min_stack.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
```

Time Complexity: O(1) for all operations
Space Complexity: O(n), where n is the number of elements in the stack

### Solution 2: Single Stack with Pairs

This solution uses a single stack, but each element is stored as a pair (value, current_min).

```python
from typing import List, Tuple

class MinStack:
    def __init__(self):
        self.stack: List[Tuple[int, int]] = []  # Stack of (value, current_min) pairs

    def push(self, val: int) -> None:
        # If stack is empty, val is the new minimum
        # Otherwise, compare val with the current minimum
        current_min = min(val, self.stack[-1][1]) if self.stack else val
        self.stack.append((val, current_min))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
```

Time Complexity: O(1) for all operations
Space Complexity: O(n), where n is the number of elements in the stack

## Recommendation

I recommend learning and implementing Solution 1: Two-Stack Approach. Here's why:

1. Clarity: It clearly separates the concerns of storing all elements and tracking minimums.
2. Flexibility: It's easier to extend or modify if additional functionalities are needed.
3. Memory efficiency: In scenarios where many elements are pushed but few are minimums, it uses less memory than Solution 2.
4. Intuitive: The concept of an auxiliary stack for minimums is a common pattern in stack problems and is valuable to understand.

While Solution 2 is also valid and efficient, it combines two pieces of information in each stack element, which can be less intuitive and potentially more prone to errors when implementing or modifying the code.

## Test cases

```python
# Test case 1: Basic operations
minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
assert minStack.getMin() == -3
minStack.pop()
assert minStack.top() == 0
assert minStack.getMin() == -2

# Test case 2: Duplicate minimums
minStack = MinStack()
minStack.push(1)
minStack.push(2)
minStack.push(1)
assert minStack.getMin() == 1
minStack.pop()
assert minStack.getMin() == 1

# Test case 3: Large numbers
minStack = MinStack()
minStack.push(2**31 - 1)
minStack.push(-2**31)
assert minStack.getMin() == -2**31
minStack.pop()
assert minStack.getMin() == 2**31 - 1

# Test case 4: Many operations
minStack = MinStack()
for i in range(3 * 10**4):
    minStack.push(i)
    assert minStack.getMin() == 0
for i in range(3 * 10**4):
    assert minStack.top() == 3 * 10**4 - 1 - i
    minStack.pop()
```

## Overview of rejected approaches

1. Naive approach: Keeping a single variable for the minimum

   - Why it doesn't work: While this would work for getMin(), it fails when we need to update the minimum after popping elements. We wouldn't know what the new minimum is without scanning the entire stack, which would be O(n).

2. Sorting the stack

   - Why it's not worth learning: While this would allow us to retrieve the minimum easily, it would make push and pop operations O(n log n), violating the O(1) time complexity requirement for all operations.

3. Using a heap alongside the stack

   - Why it's not worth learning: While a heap would allow us to retrieve the minimum in O(1) time, removing elements other than the minimum would be O(log n), violating the O(1) requirement for pop operations.

4. Keeping a sorted list of all elements
   - Why it's not worth learning: This would allow O(1) access to the minimum, but insertions and deletions would be O(n), violating the time complexity requirements.

## Visualization(s)

To visualize the Two-Stack Approach, we can create a simple React component that demonstrates the state of both stacks after each operation:

```tsx
import React, { useState } from "react";
import { Button, Input } from "@/components/ui/button";

const MinStackVisualizer = () => {
  const [mainStack, setMainStack] = useState([]);
  const [minStack, setMinStack] = useState([]);
  const [inputValue, setInputValue] = useState("");

  const push = (val) => {
    const newVal = parseInt(val);
    setMainStack([...mainStack, newVal]);
    if (minStack.length === 0 || newVal <= minStack[minStack.length - 1]) {
      setMinStack([...minStack, newVal]);
    }
    setInputValue("");
  };

  const pop = () => {
    if (mainStack.length > 0) {
      const poppedValue = mainStack[mainStack.length - 1];
      setMainStack(mainStack.slice(0, -1));
      if (poppedValue === minStack[minStack.length - 1]) {
        setMinStack(minStack.slice(0, -1));
      }
    }
  };

  return (
    <div className="p-4 max-w-md mx-auto">
      <h2 className="text-2xl font-bold mb-4">Min Stack Visualizer</h2>
      <div className="flex mb-4">
        <Input
          type="number"
          value={inputValue}
          onChange={(e) => setInputValue(e.target.value)}
          placeholder="Enter a number"
          className="mr-2"
        />
        <Button onClick={() => push(inputValue)} disabled={!inputValue}>
          Push
        </Button>
        <Button
          onClick={pop}
          className="ml-2"
          disabled={mainStack.length === 0}
        >
          Pop
        </Button>
      </div>
      <div className="flex justify-between">
        <div className="w-1/2 pr-2">
          <h3 className="font-bold mb-2">Main Stack</h3>
          <div className="border p-2 h-40 overflow-y-auto">
            {mainStack.map((val, index) => (
              <div key={index} className="mb-1">
                {val}
              </div>
            ))}
          </div>
        </div>
        <div className="w-1/2 pl-2">
          <h3 className="font-bold mb-2">Min Stack</h3>
          <div className="border p-2 h-40 overflow-y-auto">
            {minStack.map((val, index) => (
              <div key={index} className="mb-1">
                {val}
              </div>
            ))}
          </div>
        </div>
      </div>
      <div className="mt-4">
        <p>
          <strong>Top:</strong>{" "}
          {mainStack.length > 0 ? mainStack[mainStack.length - 1] : "N/A"}
        </p>
        <p>
          <strong>Min:</strong>{" "}
          {minStack.length > 0 ? minStack[minStack.length - 1] : "N/A"}
        </p>
      </div>
    </div>
  );
};

export default MinStackVisualizer;
```

This visualization allows you to interact with a Min Stack implementation, pushing and popping values to see how both the main stack and the min stack change. It helps illustrate how the min stack always keeps track of the current minimum value, even as elements are added and removed from the main stack.
