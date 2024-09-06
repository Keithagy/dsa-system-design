## Explanation: Asteroid Collision

### Analysis of problem & input data

This problem is fundamentally about simulating a series of collisions between asteroids moving in opposite directions. The key characteristics of the problem are:

1. Asteroids are represented by integers in an array.
2. The absolute value of each integer represents the asteroid's size.
3. The sign represents the direction (positive for right, negative for left).
4. Collisions only occur between asteroids moving in opposite directions.
5. In a collision, the smaller asteroid explodes; if equal, both explode.
6. Asteroids moving in the same direction never collide.

The problem can be categorized as a simulation problem with stack-like behavior. The key principle that makes this question simple is the realization that we only need to consider collisions for rightward-moving asteroids with leftward-moving asteroids that come after them in the array.

This problem is an excellent example of how Leetcode problems often require pattern matching to specific data structure usage. In this case, a stack is an ideal data structure because:

1. We process asteroids from left to right.
2. We need to keep track of asteroids that might collide with future asteroids.
3. We only need to consider the most recently added asteroid for potential collisions.

### Test cases

Here are some relevant test cases:

1. Basic collision: `[5, 10, -5]` → `[5, 10]`
2. All asteroids explode: `[8, -8]` → `[]`
3. Multiple collisions: `[10, 2, -5]` → `[10]`
4. No collisions: `[-2, -1, 1, 2]` → `[-2, -1, 1, 2]`
5. Left-moving asteroid survives multiple collisions: `[5, 10, -5]` → `[5, 10]`
6. Right-moving asteroids at the end: `[-2, -2, 1, 1]` → `[-2, -2, 1, 1]`
7. Left-moving asteroids at the beginning: `[-2, -1, 1, 2]` → `[-2, -1, 1, 2]`
8. Alternating directions: `[1, -1, 2, -2]` → `[]`
9. Large asteroid destroys multiple smaller ones: `[10, -5, 5, -10]` → `[-10]`

Here's the Python code for these test cases:

```python
def asteroid_collision(asteroids):
    # Implementation goes here
    pass

test_cases = [
    [5, 10, -5],
    [8, -8],
    [10, 2, -5],
    [-2, -1, 1, 2],
    [5, 10, -5],
    [-2, -2, 1, 1],
    [-2, -1, 1, 2],
    [1, -1, 2, -2],
    [10, -5, 5, -10]
]

for i, case in enumerate(test_cases):
    result = asteroid_collision(case)
    print(f"Test case {i + 1}: {case} → {result}")
```

### Solutions

#### Overview of solution approaches

##### Solutions worth learning

1. Stack-based approach (Neetcode solution)
2. Two-pointer approach
3. In-place modification

Count: 3 solutions (1 Neetcode solution)

##### Rejected solutions

1. Brute force simulation: Simulating all collisions by repeatedly scanning the array is inefficient.
2. Recursion: While possible, it's not as intuitive or efficient as the iterative approaches.

#### Worthy Solutions

##### Stack-based approach (Neetcode solution)

```python
def asteroid_collision(asteroids: List[int]) -> List[int]:
    stack = []

    for asteroid in asteroids:
        while stack and asteroid < 0 < stack[-1]:
            if stack[-1] < -asteroid:
                stack.pop()
                continue
            elif stack[-1] == -asteroid:
                stack.pop()
            break
        else:
            stack.append(asteroid)

    return stack
```

Time Complexity: O(n), where n is the number of asteroids. Each asteroid is pushed and popped at most once.
Space Complexity: O(n) in the worst case, where no collisions occur and all asteroids are stored in the stack.

Explanation:

- We iterate through each asteroid once, which gives us O(n) time complexity.
- In the worst case, we might need to store all asteroids in the stack, giving us O(n) space complexity.
- The while loop might seem to add extra time complexity, but each asteroid is popped at most once, so the total number of operations remains linear.

Key intuitions and invariants:

- The stack always represents the current state of surviving asteroids.
- Only the top of the stack needs to be considered for collisions with the current asteroid.
- Left-moving asteroids can only collide with right-moving asteroids already in the stack.
- The `else` clause in the `for` loop is executed when the `while` loop condition is initially false or when we `break` out of the `while` loop.

##### Two-pointer approach

```python
def asteroid_collision(asteroids: List[int]) -> List[int]:
    n = len(asteroids)
    write = 0  # Pointer for writing surviving asteroids

    for read in range(n):
        # If there's no collision, just write the asteroid
        if write == 0 or asteroids[read] > 0 or asteroids[write-1] < 0:
            asteroids[write] = asteroids[read]
            write += 1
        else:
            # Handle collision
            if abs(asteroids[write-1]) < abs(asteroids[read]):
                # Current asteroid destroys the previous one
                write -= 1
                continue
            elif abs(asteroids[write-1]) == abs(asteroids[read]):
                # Both asteroids destroy each other
                write -= 1
            # If current asteroid is destroyed, do nothing

    return asteroids[:write]
```

Time Complexity: O(n), where n is the number of asteroids. We iterate through the array once.
Space Complexity: O(1), as we modify the input array in-place.

Explanation:

- We use two pointers: 'read' to iterate through all asteroids, and 'write' to keep track of surviving asteroids.
- The time complexity is O(n) because we process each asteroid once, even though we might move the 'write' pointer backwards.
- The space complexity is O(1) because we modify the input array in-place without using any additional data structures.

Key intuitions and invariants:

- The 'write' pointer always points to the position where the next surviving asteroid should be placed.
- Asteroids before the 'write' pointer are guaranteed to survive.
- We only need to consider collisions between the current asteroid and the last surviving asteroid.

##### In-place modification

```python
def asteroid_collision(asteroids: List[int]) -> List[int]:
    i = 0  # Pointer for the current position

    for asteroid in asteroids:
        while i > 0 and asteroids[i-1] > 0 > asteroid:
            if asteroids[i-1] < -asteroid:
                i -= 1
                continue
            elif asteroids[i-1] == -asteroid:
                i -= 1
            break
        else:
            asteroids[i] = asteroid
            i += 1

    return asteroids[:i]
```

Time Complexity: O(n), where n is the number of asteroids. Each asteroid is processed at most twice (once when it's added, and once if it's destroyed).
Space Complexity: O(1), as we modify the input array in-place.

Explanation:

- Similar to the stack approach, but we use the input array itself as the stack.
- The time complexity is O(n) because each asteroid is processed at most twice.
- The space complexity is O(1) because we modify the input array in-place.

Key intuitions and invariants:

- The array up to index i always represents the current state of surviving asteroids.
- We only need to consider collisions between the current asteroid and the previously surviving asteroids.
- The `else` clause in the `for` loop is executed when the `while` loop condition is initially false or when we `break` out of the `while` loop.

#### Rejected Approaches

1. Brute force simulation: This approach would involve repeatedly scanning the array and simulating collisions until no more collisions occur. This is inefficient with a time complexity of O(n^2) in the worst case.

2. Recursion: While it's possible to solve this problem recursively by handling one collision at a time and recursing on the remaining asteroids, this approach is less intuitive and could lead to stack overflow for large inputs. It also doesn't provide any benefits over the iterative approaches in terms of time or space complexity.

#### Final Recommendations

The stack-based approach (Neetcode solution) is the best to learn for several reasons:

1. It's intuitive and closely models the problem description.
2. It has optimal time and space complexity.
3. It's concise and easy to implement.
4. It demonstrates effective use of a stack data structure, which is a common pattern in many problems.

The two-pointer and in-place modification approaches are also worth understanding as they showcase techniques for optimizing space usage, which can be crucial in certain interview scenarios or when dealing with large datasets.

### Visualization(s)

For this problem, a simple visualization of the stack operations would be helpful. Here's a text-based representation of how the stack changes for the input `[5, 10, -5]`:

```
Step 1: [5]
Step 2: [5, 10]
Step 3: [5, 10] (-5 collides with 10 and is destroyed)
Final: [5, 10]
```

For a more complex example, let's visualize `[5, 10, -5, -10, 15, -15]`:

```
Step 1: [5]
Step 2: [5, 10]
Step 3: [5, 10] (-5 collides with 10 and is destroyed)
Step 4: [5] (-10 collides with 10, destroying 10, then collides with 5, destroying 5)
Step 5: [5, 15]
Step 6: [] (-15 collides with 15, destroying both)
Final: []
```

These visualizations help to understand how the stack-based approach processes each asteroid and handles collisions.

two-pointer approach:

```
Initial array: [5, 10, -5, -10, 15, -15]

Step 1: read = 0, write = 0
[5, 10, -5, -10, 15, -15]
 ^
 read/write

Step 2: read = 1, write = 1
[5, 10, -5, -10, 15, -15]
    ^
    read/write

Step 3: read = 2, write = 2
[5, 10, -5, -10, 15, -15]
       ^
       read/write
Collision detected: 10 > |-5|, -5 is destroyed

Step 4: read = 3, write = 2
[5, 10, -10, -10, 15, -15]
       ^    ^
     write  read
Collision detected: 10 = |-10|, both are destroyed

Step 5: read = 3, write = 1
[5, -10, -10, -10, 15, -15]
    ^    ^
  write  read
Collision detected: 5 < |-10|, 5 is destroyed

Step 6: read = 4, write = 0
[-10, -10, -10, -10, 15, -15]
 ^                   ^
write               read

Step 7: read = 5, write = 1
[-10, 15, -10, -10, 15, -15]
      ^                   ^
    write               read
Collision detected: 15 > |-15|, -15 is destroyed

Final array: [-10, 15]
               ^
              write
```

Explanation of the visualization:

1. We start with both `read` and `write` pointers at the beginning of the array.
2. We move through the array with the `read` pointer, processing each asteroid.
3. The `write` pointer keeps track of where we should place the next surviving asteroid.
4. When a collision occurs, we handle it by either destroying the current asteroid (not advancing `write`), destroying the previous asteroid (decrementing `write`), or destroying both (decrementing `write` and not writing the current asteroid).
5. After processing all asteroids, we return the slice of the array from the beginning up to the `write` pointer.

This visualization demonstrates how the two-pointer approach efficiently handles collisions while modifying the array in-place, resulting in a space-efficient solution.
