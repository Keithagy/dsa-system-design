## Explanation: Linked List Cycle

### Analysis of problem & input data

This problem is a classic example of cycle detection in a linked list. The key characteristics of the problem are:

1. We're dealing with a singly linked list, where each node points to the next node.
2. The list may or may not contain a cycle.
3. If there's a cycle, it means that at some point, a node's 'next' pointer points back to a previously visited node.
4. The `pos` parameter is not directly given to us in the function; it's used internally to create the cycle in the test cases.

The key principle that makes this question simple is the "Floyd's Cycle-Finding Algorithm" (also known as the "Tortoise and Hare" algorithm). This algorithm uses two pointers moving at different speeds to detect a cycle. If there's a cycle, the faster pointer will eventually catch up to the slower pointer.

Pattern matching: This problem falls into the category of "Two Pointer" problems, specifically the "Fast and Slow Pointer" pattern. This pattern is often used in linked list problems, especially for cycle detection or finding the middle of a linked list.

### Test cases

1. Empty list: `head = nil`
2. Single node without cycle: `head = &ListNode{Val: 1, Next: nil}`
3. Two nodes with cycle: `head = &ListNode{Val: 1, Next: &ListNode{Val: 2, Next: head}}`
4. Multiple nodes without cycle: `head = &ListNode{Val: 1, Next: &ListNode{Val: 2, Next: &ListNode{Val: 3, Next: nil}}}`
5. Multiple nodes with cycle at the end: `head = &ListNode{Val: 3, Next: &ListNode{Val: 2, Next: &ListNode{Val: 0, Next: &ListNode{Val: -4, Next: head.Next}}}}`
6. Multiple nodes with cycle in the middle: `head = &ListNode{Val: 1, Next: &ListNode{Val: 2, Next: &ListNode{Val: 3, Next: &ListNode{Val: 4, Next: head.Next.Next}}}}`

Here's the Go code to set up these test cases:

```go
type ListNode struct {
    Val int
    Next *ListNode
}

func createLinkedList(values []int, pos int) *ListNode {
    if len(values) == 0 {
        return nil
    }

    head := &ListNode{Val: values[0]}
    current := head
    var cycleNode *ListNode

    for i := 1; i < len(values); i++ {
        current.Next = &ListNode{Val: values[i]}
        current = current.Next
        if i == pos {
            cycleNode = current
        }
    }

    if cycleNode != nil {
        current.Next = cycleNode
    }

    return head
}

func main() {
    testCases := []struct {
        values []int
        pos    int
    }{
        {[]int{}, -1},                  // Empty list
        {[]int{1}, -1},                 // Single node without cycle
        {[]int{1, 2}, 0},               // Two nodes with cycle
        {[]int{1, 2, 3}, -1},           // Multiple nodes without cycle
        {[]int{3, 2, 0, -4}, 1},        // Multiple nodes with cycle at the end
        {[]int{1, 2, 3, 4}, 1},         // Multiple nodes with cycle in the middle
    }

    for _, tc := range testCases {
        head := createLinkedList(tc.values, tc.pos)
        fmt.Printf("Has cycle: %v\n", hasCycle(head))
    }
}
```

### Solutions

#### Overview of solution approaches

##### Solutions worth learning

1. Floyd's Cycle-Finding Algorithm (Two Pointers: Fast and Slow) - Neetcode solution
2. Hash Set
3. Modifying the linked list structure (not recommended for interviews)

Count: 3 solutions (1 Neetcode solution)

##### Rejected solutions

1. Brute force with a counter: This approach would involve traversing the list with a counter and checking if we've exceeded the maximum possible length of the list. This is not optimal as it doesn't leverage the nature of the problem efficiently.

#### Worthy Solutions

##### Floyd's Cycle-Finding Algorithm (Two Pointers: Fast and Slow)

```go
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func hasCycle(head *ListNode) bool {
    // Edge case: empty list or single node
    if head == nil || head.Next == nil {
        return false
    }

    // Initialize two pointers
    slow, fast := head, head.Next

    // Move pointers until they meet or reach the end
    for fast != nil && fast.Next != nil {
        // If pointers meet, there's a cycle
        if slow == fast {
            return true
        }
        // Move slow pointer by one step
        slow = slow.Next
        // Move fast pointer by two steps
        fast = fast.Next.Next
    }

    // If we exit the loop, there's no cycle
    return false
}
```

Runtime complexity: O(n), where n is the number of nodes in the linked list.
Space complexity: O(1), as we only use two pointers regardless of the input size.

Explanation:

- Time complexity: In the worst case (no cycle), we traverse the entire list once. If there is a cycle, we'll detect it before completing a full cycle, which is still O(n).
- Space complexity: We only use two pointers (slow and fast), which occupy constant space regardless of the input size.

Intuitions and invariants:

- If there's a cycle, the fast pointer will eventually catch up to the slow pointer.
- The fast pointer moves twice as fast as the slow pointer, ensuring they will meet if there's a cycle.
- If there's no cycle, the fast pointer will reach the end of the list.
- The algorithm maintains the invariant that the distance between the pointers increases by 1 in each iteration if there's no cycle.

##### Hash Set

```go
func hasCycle(head *ListNode) bool {
    // Create a hash set to store visited nodes
    visited := make(map[*ListNode]bool)

    // Traverse the linked list
    for head != nil {
        // If we've seen this node before, there's a cycle
        if visited[head] {
            return true
        }
        // Mark the current node as visited
        visited[head] = true
        // Move to the next node
        head = head.Next
    }

    // If we reach here, there's no cycle
    return false
}
```

Runtime complexity: O(n), where n is the number of nodes in the linked list.
Space complexity: O(n), as in the worst case, we store all nodes in the hash set.

Explanation:

- Time complexity: We traverse the list once, performing constant-time operations (hash set insertion and lookup) for each node.
- Space complexity: In the worst case (no cycle), we store all nodes in the hash set.

Intuitions and invariants:

- Each node is unique, so if we encounter a node we've seen before, there must be a cycle.
- The hash set allows for constant-time lookups and insertions.
- This approach trades space for simplicity and potentially faster execution in practice.

##### Modifying the linked list structure

```go
func hasCycle(head *ListNode) bool {
    for head != nil {
        // If we've marked this node, we've found a cycle
        if head.Val == math.MinInt32 {
            return true
        }
        // Mark this node as visited
        head.Val = math.MinInt32
        head = head.Next
    }
    return false
}
```

Runtime complexity: O(n), where n is the number of nodes in the linked list.
Space complexity: O(1), as we modify the existing structure without using extra space.

Explanation:

- Time complexity: We traverse the list once, performing constant-time operations for each node.
- Space complexity: We modify the existing structure in-place, using no extra space.

Intuitions and invariants:

- We use a special value (math.MinInt32) to mark visited nodes.
- If we encounter a marked node, we've found a cycle.
- This approach assumes we can modify the original list structure, which may not always be allowed.

#### Rejected Approaches

1. Brute force with a counter: This approach would involve traversing the list with a counter and checking if we've exceeded the maximum possible length of the list (10^4 in this case). While this would work, it's not efficient for large lists and doesn't leverage the problem's nature effectively.

2. Recursive approach: A recursive solution could be implemented, but it would potentially lead to stack overflow for very long lists, especially if there's a cycle. It also doesn't provide any advantages over the iterative approaches.

#### Final Recommendations

The Floyd's Cycle-Finding Algorithm (Two Pointers: Fast and Slow) is the best solution to learn for this problem. It's efficient in both time and space complexity, doesn't modify the original list structure, and demonstrates a clever algorithmic technique that's applicable to various other problems. This method is often asked about in interviews and is considered the standard solution for cycle detection in linked lists.

The Hash Set approach is also worth knowing as it's intuitive and can be quickly implemented if you're more comfortable with hash-based solutions. However, it's less space-efficient than the two-pointer method.

The approach that modifies the linked list structure, while efficient, is generally not recommended for interviews as it alters the input data, which is often considered bad practice unless explicitly allowed.

### Visualization(s)

For this problem, a visual representation of the Floyd's Cycle-Finding Algorithm would be helpful. Here's a simple ASCII art visualization:

```
Step 1: Initial state
3 -> 2 -> 0 -> -4 -+
     ^             |
     |             |
     +-------------+

S
F

Step 2: After first iteration
3 -> 2 -> 0 -> -4 -+
     ^             |
     |             |
     +-------------+

     S
          F

Step 3: After second iteration
3 -> 2 -> 0 -> -4 -+
     ^             |
     |             |
     +-------------+

          S
                    F

Step 4: After third iteration (cycle detected)
3 -> 2 -> 0 -> -4 -+
     ^             |
     |             |
     +-------------+

               S
               F

S: Slow pointer
F: Fast pointer
```

This visualization shows how the slow and fast pointers move through the linked list until they meet, indicating a cycle.
