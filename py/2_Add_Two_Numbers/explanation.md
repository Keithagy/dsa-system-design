## Explanation: Add Two Numbers

### Analysis of problem & input data

This problem is a classic example of linked list manipulation and basic arithmetic operations. The key aspects to consider are:

1. **Linked List Structure**: The numbers are represented as linked lists, with each node containing a single digit.
2. **Reverse Order**: The digits are stored in reverse order, which actually simplifies the addition process as we can start from the least significant digit.
3. **Variable Length**: The two numbers can have different lengths, which we need to account for in our solution.
4. **Carry Over**: When adding digits, we need to handle carry-over to the next position.
5. **Result Formation**: The result should also be in the form of a linked list.

The key principle that makes this question simple is that the reverse order representation aligns perfectly with how we perform manual addition: starting from the least significant digit and moving towards the most significant digit, carrying over when necessary.

### Test cases

Here are some relevant test cases to consider:

1. **Equal length, no carry**:
   l1 = [2,4,3], l2 = [5,6,4] → [7,0,8]
2. **Equal length, with carry**:
   l1 = [9,9,9], l2 = [1,1,1] → [0,1,1,1]
3. **Different lengths**:
   l1 = [9,9,9,9], l2 = [1] → [0,0,0,0,1]
4. **One empty list**:
   l1 = [1,2,3], l2 = [] → [1,2,3]
5. **Both single-node lists**:
   l1 = [5], l2 = [5] → [0,1]
6. **Large carry over**:
   l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9] → [8,9,9,9,0,0,0,1]

Here's the Python code to set up these test cases:

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def create_linked_list(arr):
    dummy = ListNode(0)
    current = dummy
    for val in arr:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

def linked_list_to_array(head):
    arr = []
    while head:
        arr.append(head.val)
        head = head.next
    return arr

# Test cases
test_cases = [
    ([2,4,3], [5,6,4]),
    ([9,9,9], [1,1,1]),
    ([9,9,9,9], [1]),
    ([1,2,3], []),
    ([5], [5]),
    ([9,9,9,9,9,9,9], [9,9,9,9])
]

# Function to run tests
def run_tests(solution_func):
    for i, (l1, l2) in enumerate(test_cases):
        l1_node = create_linked_list(l1)
        l2_node = create_linked_list(l2)
        result = solution_func(l1_node, l2_node)
        print(f"Test case {i+1}: {linked_list_to_array(result)}")

# Usage: run_tests(add_two_numbers)
```

### Solutions

#### Overview of solution approaches

##### Solutions worth learning

1. Iterative approach (Neetcode solution)
2. Recursive approach
3. Dummy node approach

Count: 3 solutions (1 Neetcode solution)

##### Rejected solutions

1. Converting to integer, adding, and converting back to linked list: This approach fails for very large numbers due to integer overflow.
2. Using a stack: While this could work, it's unnecessarily complex for this problem and doesn't leverage the reverse order nature of the input.

#### Worthy Solutions

##### Iterative approach (Neetcode solution)

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)  # Dummy node to simplify edge cases
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            # Get values, use 0 if the list has ended
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            # New digit is sum of values plus carry
            val = v1 + v2 + carry
            carry = val // 10  # Integer division to get new carry
            val = val % 10     # Modulo to get the digit to add

            current.next = ListNode(val)
            current = current.next

            # Move to next nodes if they exist
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next  # Return the head of the result list
```

Time Complexity: O(max(N, M)), where N and M are the lengths of l1 and l2.
Space Complexity: O(max(N, M)) for the new linked list.

Explanation:

- We iterate through both lists simultaneously, creating a new list for the sum.
- The time complexity is linear with respect to the longer list, as we need to process all digits.
- The space complexity is also linear, as we create a new list to store the result.

Key intuitions and invariants:

- Using a dummy node simplifies handling the head of the result list.
- The carry is maintained throughout the iteration, ensuring correct addition.
- The loop continues while there are digits in either list or a carry exists, handling lists of different lengths.

##### Recursive approach

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def add_recursive(n1, n2, carry=0):
            if not n1 and not n2 and carry == 0:
                return None

            # Sum the current digits and carry
            value = carry
            if n1:
                value += n1.val
                n1 = n1.next
            if n2:
                value += n2.val
                n2 = n2.next

            # Create new node with current digit
            node = ListNode(value % 10)

            # Recursively process next digits
            node.next = add_recursive(n1, n2, value // 10)

            return node

        return add_recursive(l1, l2)
```

Time Complexity: O(max(N, M)), where N and M are the lengths of l1 and l2.
Space Complexity: O(max(N, M)) for the call stack and new linked list.

Explanation:

- The time complexity is linear as we process each node once.
- The space complexity is linear due to the recursive call stack and the new list we're creating.

Key intuitions and invariants:

- The base case is when both lists are exhausted and there's no carry.
- Each recursive call processes one digit and passes the carry to the next call.
- The recursion naturally handles lists of different lengths.

##### Dummy node approach

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        current = dummy
        carry = 0

        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0

            sum = carry + x + y
            carry = sum // 10
            current.next = ListNode(sum % 10)

            current = current.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        if carry > 0:
            current.next = ListNode(carry)

        return dummy.next
```

Time Complexity: O(max(N, M)), where N and M are the lengths of l1 and l2.
Space Complexity: O(max(N, M)) for the new linked list.

Explanation:

- This approach is similar to the iterative one but handles the carry slightly differently.
- The time and space complexities are the same as the iterative approach.

Key intuitions and invariants:

- The dummy node simplifies handling the head of the result list.
- We process both lists simultaneously, handling different lengths naturally.
- The final carry check ensures we don't miss an additional digit if there's a carry at the end.

#### Rejected Approaches

1. **Converting to integer, adding, and converting back**: This approach seems intuitive but fails for very large numbers due to integer overflow. It also doesn't leverage the linked list structure effectively.

2. **Using a stack**: While this could work by pushing all elements onto stacks, reversing the order, and then performing addition, it's unnecessarily complex. The problem already gives us the numbers in reverse order, so we can add directly without any reversal.

#### Final Recommendations

The iterative approach (Neetcode solution) is the best to learn for several reasons:

1. It's intuitive and mirrors how we would add numbers manually.
2. It has optimal time and space complexity.
3. It handles different list lengths and carry-over elegantly.
4. It's iterative, which is often preferred in interviews for its simplicity and lower space complexity compared to recursive solutions.

The recursive approach is also worth understanding as it demonstrates a different problem-solving paradigm, but it's generally less preferred in interviews due to the potential stack overflow for very long lists.

### Visualization(s)

Here's a simple visualization of how the iterative addition works:

```
  2 -> 4 -> 3
  5 -> 6 -> 4
  -------------
  7 -> 0 -> 8

Step 1: 2 + 5 = 7, carry = 0
Step 2: 4 + 6 = 10, write 0, carry = 1
Step 3: 3 + 4 + 1 (carry) = 8, carry = 0
```

This visualization helps to understand how we process the linked lists digit by digit, handling carry as we go along.

```tsx
import React, { useState, useEffect } from "react";
import { Card, CardContent, CardHeader } from "@/components/ui/card";

const LinkedListNode = ({ value, isCarry }) => (
  <div
    className={`inline-flex items-center justify-center w-10 h-10 rounded-full border-2 ${isCarry ? "border-red-500 text-red-500" : "border-blue-500 text-blue-500"} mr-2`}
  >
    {value}
  </div>
);

const Arrow = () => <div className="inline-block mx-2">→</div>;

const LinkedList = ({ values, isCarry }) => (
  <div className="flex items-center mb-4">
    {values.map((value, index) => (
      <React.Fragment key={index}>
        <LinkedListNode value={value} isCarry={isCarry} />
        {index < values.length - 1 && <Arrow />}
      </React.Fragment>
    ))}
  </div>
);

const LinkedListAddition = () => {
  const [list1, setList1] = useState([2, 4, 3]);
  const [list2, setList2] = useState([5, 6, 4]);
  const [result, setResult] = useState([]);
  const [carry, setCarry] = useState(0);
  const [step, setStep] = useState(0);

  useEffect(() => {
    if (step < Math.max(list1.length, list2.length)) {
      const timer = setTimeout(() => {
        const val1 = step < list1.length ? list1[step] : 0;
        const val2 = step < list2.length ? list2[step] : 0;
        const sum = val1 + val2 + carry;
        setResult((prev) => [...prev, sum % 10]);
        setCarry(Math.floor(sum / 10));
        setStep((prev) => prev + 1);
      }, 1000);
      return () => clearTimeout(timer);
    } else if (carry > 0) {
      setResult((prev) => [...prev, carry]);
      setCarry(0);
    }
  }, [step, carry, list1, list2]);

  return (
    <Card className="w-full max-w-2xl mx-auto">
      <CardHeader>Linked List Addition Visualization</CardHeader>
      <CardContent>
        <LinkedList values={list1} />
        <LinkedList values={list2} />
        <div className="border-t-2 border-gray-300 my-4"></div>
        <LinkedList values={result} />
        {carry > 0 && <LinkedList values={[carry]} isCarry />}
      </CardContent>
    </Card>
  );
};

export default LinkedListAddition;
```

This React component provides an interactive visualization of the linked list addition process. It demonstrates how the digits are added step by step, including the carry-over process. The visualization updates every second to show each step of the addition.
