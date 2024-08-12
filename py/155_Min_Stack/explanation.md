# Explanation: Min Stack

## Analysis of problem & input data

This problem requires designing a stack data structure with additional functionality to retrieve the minimum element in constant time. The key aspects of this problem are:

1. Stack operations: The basic stack operations (push, pop, top) need to be implemented.
2. Minimum element retrieval: The getMin operation needs to return the minimum element in O(1) time.
3. Constant time complexity: All operations must be performed in O(1) time.

The main challenge here is maintaining the minimum element information efficiently while performing stack operations. The key principle that makes this question simple is that we can track the minimum element at each step of stack modification, rather than calculating it on demand.

Input data characteristics:

- The stack can contain both positive and negative integers.
- The range of values is between -2^31 and 2^31 - 1, which fits within a 32-bit integer.
- The stack will never be empty when pop, top, or getMin are called.
- There can be up to 3 \* 10^4 calls to the stack methods.

### Test cases

1. Basic operations:

   - Push elements: -2, 0, -3
   - Get minimum (should return -3)
   - Pop
   - Get top (should return 0)
   - Get minimum (should return -2)

2. Duplicate minimum:

   - Push elements: 1, 1, 1
   - Get minimum (should return 1)
   - Pop
   - Get minimum (should still return 1)

3. Ascending order:

   - Push elements: 1, 2, 3, 4, 5
   - Get minimum (should return 1)
   - Pop multiple times
   - Get minimum (should still return 1)

4. Descending order:

   - Push elements: 5, 4, 3, 2, 1
   - Get minimum (should return 1)
   - Pop
   - Get minimum (should return 2)

5. Mixed order with negative numbers:
   - Push elements: -1, 5, -2, 4, -3, 3
   - Get minimum (should return -3)
   - Pop twice
   - Get minimum (should return -2)

Here's the executable Python code for these tests:

```python
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        if self.stack:
            if self.stack[-1] == self.min_stack[-1]:
                self.min_stack.pop()
            self.stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]

    def getMin(self) -> int:
        if self.min_stack:
            return self.min_stack[-1]

# Test cases
def run_tests():
    # Test case 1: Basic operations
    ms1 = MinStack()
    ms1.push(-2)
    ms1.push(0)
    ms1.push(-3)
    assert ms1.getMin() == -3, "Test case 1 failed: getMin"
    ms1.pop()
    assert ms1.top() == 0, "Test case 1 failed: top"
    assert ms1.getMin() == -2, "Test case 1 failed: getMin after pop"

    # Test case 2: Duplicate minimum
    ms2 = MinStack()
    ms2.push(1)
    ms2.push(1)
    ms2.push(1)
    assert ms2.getMin() == 1, "Test case 2 failed: getMin"
    ms2.pop()
    assert ms2.getMin() == 1, "Test case 2 failed: getMin after pop"

    # Test case 3: Ascending order
    ms3 = MinStack()
    for i in range(1, 6):
        ms3.push(i)
    assert ms3.getMin() == 1, "Test case 3 failed: getMin"
    for _ in range(3):
        ms3.pop()
    assert ms3.getMin() == 1, "Test case 3 failed: getMin after multiple pops"

    # Test case 4: Descending order
    ms4 = MinStack()
    for i in range(5, 0, -1):
        ms4.push(i)
    assert ms4.getMin() == 1, "Test case 4 failed: getMin"
    ms4.pop()
    assert ms4.getMin() == 2, "Test case 4 failed: getMin after pop"

    # Test case 5: Mixed order with negative numbers
    ms5 = MinStack()
    for val in [-1, 5, -2, 4, -3, 3]:
        ms5.push(val)
    assert ms5.getMin() == -3, "Test case 5 failed: getMin"
    ms5.pop()
    ms5.pop()
    assert ms5.getMin() == -2, "Test case 5 failed: getMin after two pops"

    print("All test cases passed!")

run_tests()
```

## Solutions

### Overview of solution approaches

#### Solutions worth learning

1. Two-stack approach: Use one stack for elements and another for minimum values
2. Single stack with pairs: Store each element with the current minimum
3. Linked list with minimum tracking: Use a linked list to implement the stack, storing the minimum with each node

Count: 3 solutions

#### Rejected solutions

1. Sorting the stack: This would violate the O(1) time complexity requirement for getMin
2. Heap-based approach: While a min-heap could maintain the minimum element, it would complicate push and pop operations
3. Single stack without additional information: This would require iterating through the stack to find the minimum, violating the O(1) time complexity requirement

### Worthy Solutions

#### 1. Two-stack approach

```python
class MinStack:
    def __init__(self):
        self.stack = []  # Main stack to store all elements
        self.min_stack = []  # Auxiliary stack to store minimum values

    def push(self, val: int) -> None:
        self.stack.append(val)
        # If min_stack is empty or val is smaller than or equal to the current minimum,
        # push val onto min_stack
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        if self.stack:
            # If the popped element is the current minimum, remove it from min_stack as well
            if self.stack[-1] == self.min_stack[-1]:
                self.min_stack.pop()
            self.stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]

    def getMin(self) -> int:
        if self.min_stack:
            return self.min_stack[-1]
```

Time complexity: O(1) for all operations
Space complexity: O(n), where n is the number of elements in the stack

Intuition and invariants:

- The main stack stores all elements, while the min_stack stores only the minimum elements encountered so far.
- The top of min_stack always contains the current minimum element of the entire stack.
- We only push to min_stack when a new minimum is encountered or an equal minimum is pushed.
- We only pop from min_stack when the main stack's popped element is equal to the current minimum.

#### 2. Single stack with pairs

```python
class MinStack:
    def __init__(self):
        self.stack = []  # Stack to store (value, current_min) pairs

    def push(self, val: int) -> None:
        # If stack is empty, val is the new minimum
        # Otherwise, compare val with the current minimum
        current_min = min(val, self.stack[-1][1]) if self.stack else val
        self.stack.append((val, current_min))

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1][0]

    def getMin(self) -> int:
        if self.stack:
            return self.stack[-1][1]
```

Time complexity: O(1) for all operations
Space complexity: O(n), where n is the number of elements in the stack

Intuition and invariants:

- Each element in the stack is stored as a pair: (value, current_minimum).
- The current_minimum is calculated at push time by comparing the new value with the previous minimum.
- This approach saves space compared to the two-stack solution when there are many duplicate minimums.
- The trade-off is slightly more complex push operation and potentially more memory usage per element.

#### 3. Linked list with minimum tracking

```python
class Node:
    def __init__(self, val: int, min_val: int, next_node: 'Node' = None):
        self.val = val
        self.min_val = min_val
        self.next = next_node

class MinStack:
    def __init__(self):
        self.head = None

    def push(self, val: int) -> None:
        if not self.head:
            self.head = Node(val, val)
        else:
            # New node's min_val is the minimum of val and the current minimum
            self.head = Node(val, min(val, self.head.min_val), self.head)

    def pop(self) -> None:
        if self.head:
            self.head = self.head.next

    def top(self) -> int:
        if self.head:
            return self.head.val

    def getMin(self) -> int:
        if self.head:
            return self.head.min_val
```

Time complexity: O(1) for all operations
Space complexity: O(n), where n is the number of elements in the stack

Intuition and invariants:

- Each node in the linked list stores its value, the minimum value up to that point, and a reference to the next node.
- The head of the linked list always contains the current minimum value for the entire stack.
- This approach can be more memory-efficient than array-based implementations for very large stacks, as it doesn't require contiguous memory.
- It also provides a natural way to maintain the minimum value at each step of the stack's history.

### Rejected Approaches

1. Sorting the stack: While sorting would make finding the minimum easy, it would violate the O(1) time complexity requirement for push and pop operations. Sorting would take O(n log n) time, which is unacceptable.

2. Heap-based approach: A min-heap could maintain the minimum element efficiently, but it would complicate push and pop operations. Removing arbitrary elements (necessary for pop) from a heap is not an O(1) operation.

3. Single stack without additional information: Simply using a regular stack without any additional structures or information would require iterating through the entire stack to find the minimum, violating the O(1) time complexity requirement for getMin.

4. Using a separate variable to track the minimum: While this would work for getMin, it would fail when the minimum element is popped from the stack. Updating the minimum would require scanning the entire stack, violating the O(1) time complexity requirement.

### Final Recommendations

The two-stack approach (Solution 1) is the best one to learn and implement for this problem. Here's why:

1. Simplicity: It's straightforward to understand and implement, making it easier to explain in an interview setting.
2. Efficiency: It achieves O(1) time complexity for all operations while maintaining a clear separation of concerns between the main stack and the minimum tracking.
3. Space efficiency: While it uses an auxiliary stack, it only stores necessary information (the historical minimums), which is often more space-efficient than storing a minimum with every element.
4. Flexibility: This approach can be easily extended to support other operations or modified to track other properties (e.g., maximum element) without significant changes to the core logic.

The single stack with pairs (Solution 2) is also correct and achieves the required time complexity, but it's slightly less elegant due to the need to store pairs of values. It might be worth mentioning as an alternative approach, especially if asked about space optimization for cases with many duplicate minimums.

The linked list approach (Solution 3) is correct but might be overkill for this specific problem. It's worth knowing but probably not the first solution you'd want to present in an interview unless specifically asked about alternative data structures or memory management.

Regarding approaches that might seem correct but aren't:

1. Using a single variable to track the minimum seems tempting but fails when you need to update the minimum after popping the current minimum element.
2. Using a built-in min() function on the entire stack for getMin() would work correctly but violate the O(1) time complexity requirement.

Remember, in an interview setting, it's crucial to discuss the trade-offs between these approaches, particularly in terms of time complexity, space complexity, and ease of implementation. Always clarify the requirements and constraints with your interviewer before diving into a solution.

## Visualization(s)

To visualize the two-stack approach, which is our recommended solution, let's create a simple diagram showing how the main stack and min stack evolve as we perform operations:

```tsx
import React, { useState } from "react";

const MinStackVisualization = () => {
  const [mainStack, setMainStack] = useState([]);
  const [minStack, setMinStack] = useState([]);
  const [inputValue, setInputValue] = useState("");

  const push = (val) => {
    setMainStack([...mainStack, val]);
    if (minStack.length === 0 || val <= minStack[minStack.length - 1]) {
      setMinStack([...minStack, val]);
    }
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

  const handlePush = () => {
    const val = parseInt(inputValue);
    if (!isNaN(val)) {
      push(val);
      setInputValue("");
    }
  };

  return (
    <div className="p-4">
      <h2 className="text-xl font-bold mb-4">Min Stack Visualization</h2>
      <div className="flex mb-4">
        <input
          type="number"
          value={inputValue}
          onChange={(e) => setInputValue(e.target.value)}
          className="border p-2 mr-2"
          placeholder="Enter a number"
        />
        <button
          onClick={handlePush}
          className="bg-blue-500 text-white px-4 py-2 rounded"
        >
          Push
        </button>
        <button
          onClick={pop}
          className="bg-red-500 text-white px-4 py-2 rounded ml-2"
        >
          Pop
        </button>
      </div>
      <div className="flex">
        <div className="mr-8">
          <h3 className="font-bold mb-2">Main Stack</h3>
          <div className="border p-2" style={{ minHeight: "200px" }}>
            {mainStack.map((val, index) => (
              <div key={index} className="bg-gray-200 p-2 mb-1">
                {val}
              </div>
            ))}
          </div>
        </div>
        <div>
          <h3 className="font-bold mb-2">Min Stack</h3>
          <div className="border p-2" style={{ minHeight: "200px" }}>
            {minStack.map((val, index) => (
              <div key={index} className="bg-green-200 p-2 mb-1">
                {val}
              </div>
            ))}
          </div>
        </div>
      </div>
      <div className="mt-4">
        <p>
          Current Minimum:{" "}
          {minStack.length > 0 ? minStack[minStack.length - 1] : "N/A"}
        </p>
      </div>
    </div>
  );
};
export default MinStackVisualization;
```

This visualization demonstrates how the two-stack approach works:

The main stack (on the left) shows all elements that have been pushed.
The min stack (on the right) shows the minimum elements at each state of the stack.
You can push new elements using the input field and "Push" button.
The "Pop" button removes the top element from the main stack and updates the min stack if necessary.
The current minimum is always displayed at the bottom.

This interactive visualization helps to understand:

How elements are added to both stacks
How the min stack only updates when a new minimum is encountered
How popping affects both stacks
How the current minimum is always accessible in O(1) time

You can experiment with this visualization by:

Pushing a series of decreasing numbers (e.g., 5, 4, 3, 2, 1) to see how both stacks grow equally.
Pushing a series of increasing numbers (e.g., 1, 2, 3, 4, 5) to see how the min stack stays constant.
Pushing and popping alternately to see how the stacks change.
Pushing duplicate minimums to see how they're handled.

This visual representation makes it easier to grasp the concept and could be very helpful in explaining the solution during an interview. It demonstrates your understanding of the problem and your ability to communicate complex ideas clearly.
