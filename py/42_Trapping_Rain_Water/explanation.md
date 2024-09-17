## Explanation: Trapping Rain Water

### Analysis of problem & input data

This problem is a classic example of a two-pointer technique application, with potential for dynamic programming and stack-based solutions. The key characteristics of this problem are:

1. We're dealing with an array of non-negative integers representing heights.
2. The width of each bar is 1 unit.
3. We need to calculate the total amount of water that can be trapped between the bars.

The critical insight for this problem is understanding that for any given bar, the amount of water it can trap is determined by the minimum of the maximum height to its left and the maximum height to its right, minus its own height (if this difference is positive).

The main principle that makes this question tractable is the realization that water can only be trapped between two higher bars. This allows us to think about the problem in terms of left and right boundaries for each position.

### Test cases

1. Regular case: `[0,1,0,2,1,0,1,3,2,1,2,1]` (Output: 6)
2. Descending heights: `[4,3,2,1,0]` (Output: 0)
3. Ascending heights: `[0,1,2,3,4]` (Output: 0)
4. Single peak: `[0,1,2,3,2,1,0]` (Output: 0)
5. Two peaks: `[3,0,2,0,4]` (Output: 7)
6. Flat surface: `[2,2,2,2,2]` (Output: 0)
7. Empty input: `[]` (Output: 0)
8. Single element: `[5]` (Output: 0)

```python
def test_trap():
    assert trap([0,1,0,2,1,0,1,3,2,1,2,1]) == 6
    assert trap([4,3,2,1,0]) == 0
    assert trap([0,1,2,3,4]) == 0
    assert trap([0,1,2,3,2,1,0]) == 0
    assert trap([3,0,2,0,4]) == 7
    assert trap([2,2,2,2,2]) == 0
    assert trap([]) == 0
    assert trap([5]) == 0
    print("All test cases passed!")

# The trap function will be implemented in the solutions section
```

### Solutions

#### Overview of solution approaches

##### Solutions worth learning

1. Two Pointer Approach (Neetcode solution)
2. Dynamic Programming
3. Stack-based Approach
4. Brute Force Approach

Count: 4 solutions (1 Neetcode solution)

##### Rejected solutions

1. Sorting-based approach: Sorting would destroy the positional information which is crucial for this problem.
2. Sliding window: While this might seem tempting due to the array nature of the problem, it doesn't effectively capture the "trapping" aspect which depends on both left and right boundaries.

#### Worthy Solutions

##### Two Pointer Approach

```python
def trap(height: List[int]) -> int:
    if not height:
        return 0

    left, right = 0, len(height) - 1
    left_max, right_max = 0, 0
    water = 0

    while left < right:
        if height[left] < height[right]:
            if height[left] >= left_max:
                left_max = height[left]
            else:
                water += left_max - height[left]
            left += 1
        else:
            if height[right] >= right_max:
                right_max = height[right]
            else:
                water += right_max - height[right]
            right -= 1

    return water
```

Time Complexity: O(n), where n is the length of the height array. We traverse the array once with two pointers.
Space Complexity: O(1), as we only use a constant amount of extra space.

Explanation of time and space complexity:

- Time: We iterate through the array once, with each element being visited by either the left or right pointer. This results in a linear time complexity of O(n).
- Space: We only use a fixed number of variables (left, right, left_max, right_max, water) regardless of the input size, hence O(1) space complexity.

Intuition and invariants:

- We maintain two pointers, left and right, starting from the ends of the array.
- We also keep track of the maximum height seen from the left (left_max) and right (right_max).
- The key invariant is that for any position, the amount of water it can trap is determined by the smaller of left_max and right_max.
- We always move the pointer pointing to the smaller height, ensuring that we have the correct boundary for calculating trapped water.
- This approach works because if we encounter a smaller height, we know for certain that it will trap water (bounded by the opposite max height).

##### Dynamic Programming Approach

```python
def trap(height: List[int]) -> int:
    if not height:
        return 0

    n = len(height)
    left_max = [0] * n
    right_max = [0] * n

    left_max[0] = height[0]
    for i in range(1, n):
        left_max[i] = max(height[i], left_max[i-1])

    right_max[n-1] = height[n-1]
    for i in range(n-2, -1, -1):
        right_max[i] = max(height[i], right_max[i+1])

    water = 0
    for i in range(n):
        water += min(left_max[i], right_max[i]) - height[i]

    return water
```

Time Complexity: O(n), where n is the length of the height array. We traverse the array three times.
Space Complexity: O(n), as we use two additional arrays of size n.

Explanation of time and space complexity:

- Time: We perform three passes through the array - one to compute left_max, one for right_max, and one to calculate the trapped water. Each pass is O(n), so the total is still O(n).
- Space: We use two additional arrays (left_max and right_max) each of size n, resulting in O(n) space complexity.

Intuition and invariants:

- We precompute the maximum height to the left and right of each position.
- The invariant is that for any position i, the water trapped at i is min(left_max[i], right_max[i]) - height[i].
- This approach trades space for time, avoiding the need to recalculate max heights repeatedly.

##### Stack-based Approach

```python
def trap(height: List[int]) -> int:
    stack = []
    water = 0

    for i, h in enumerate(height):
        while stack and h > height[stack[-1]]:
            top = stack.pop()

            if not stack:
                break

            distance = i - stack[-1] - 1
            bounded_height = min(h, height[stack[-1]]) - height[top]
            water += distance * bounded_height

        stack.append(i)

    return water
```

Time Complexity: O(n), where n is the length of the height array. Each element is pushed and popped at most once.
Space Complexity: O(n) in the worst case, when the heights are in descending order.

Explanation of time and space complexity:

- Time: Although we have a nested while loop, each element is pushed and popped at most once, resulting in amortized O(n) time complexity.
- Space: In the worst case (descending heights), we might push all elements onto the stack before processing, leading to O(n) space complexity.

Intuition and invariants:

- We use a stack to keep track of indices where height is decreasing.
- When we find a bar taller than the top of the stack, we know we can trap water at the top of the stack.
- The amount of water is determined by the distance between the current bar and the bar at the top of the stack, bounded by their heights.
- This approach effectively identifies "valleys" where water can be trapped.

##### Brute Force Approach

```python
def trap(height: List[int]) -> int:
    water = 0

    for i in range(len(height)):
        left_max = max(height[:i+1])
        right_max = max(height[i:])
        water += min(left_max, right_max) - height[i]

    return water
```

Time Complexity: O(n^2), where n is the length of the height array.
Space Complexity: O(1), as we only use a constant amount of extra space.

Explanation of time and space complexity:

- Time: For each element, we compute the maximum height to its left and right, which are both O(n) operations. Doing this for all n elements results in O(n^2) time complexity.
- Space: We only use a fixed number of variables regardless of the input size, hence O(1) space complexity.

Intuition and invariants:

- For each position, we find the maximum height to its left and right.
- The water trapped at each position is the minimum of these two maxima, minus the height at that position.
- This approach directly implements the problem statement but is inefficient for large inputs.

#### Rejected Approaches

1. Sorting-based approach: Sorting the heights would destroy the positional information, which is crucial for determining where water can be trapped. This approach is fundamentally flawed for this problem.

2. Sliding window approach: While sliding window is often useful for array problems, it doesn't effectively capture the "trapping" aspect of this problem, which depends on both left and right boundaries that can be far apart.

3. Greedy approach: A simple greedy approach (e.g., always moving towards the higher bar) doesn't work because it might miss some water-trapping opportunities.

#### Final Recommendations

The Two Pointer Approach is the best solution to learn for this problem. It offers the optimal balance of time and space complexity (O(n) time and O(1) space) while being relatively straightforward to understand and implement. It's also the approach favored by Neetcode.

The Dynamic Programming approach is also worth understanding as it clearly demonstrates the relationship between left and right maximum heights, which is the key to solving this problem. However, it uses more space than necessary.

The Stack-based approach, while clever, is less intuitive and might be harder to come up with in an interview setting. It's worth knowing about, but not as critical as the Two Pointer approach.

The Brute Force approach, while simple to understand, is too inefficient for larger inputs and is mainly useful as a starting point to develop more efficient solutions.

### Visualization(s)

For a visual representation of how the Two Pointer approach works, we can use ASCII art to show the process:

```
Height: [0,1,0,2,1,0,1,3,2,1,2,1]
Step 1:
L                                 R
0 1 0 2 1 0 1 3 2 1 2 1
^ Max from left: 0                 ^ Max from right: 1
Water at this step: 0

Step 2:
  L                               R
0 1 0 2 1 0 1 3 2 1 2 1
  ^ Max from left: 1               ^ Max from right: 1
Water at this step: 0

Step 3:
    L                             R
0 1 0 2 1 0 1 3 2 1 2 1
    ^ Max from left: 1             ^ Max from right: 1
Water at this step: 1 (Fill up to height 1)

...

Final state:
                  L R
0 1 0 2 1 0 1 3 2 1 2 1
                  ^ ^
Total water trapped: 6
```

This visualization helps to understand how the two pointers move towards each other, always considering the maximum height from each side and calculating the water that can be trapped at each step.
