```python
def floyd_cycle_finding(f, x0):
    # The tortoise and hare start at the beginning of the sequence
    tortoise = f(x0)
    hare = f(f(x0))

    # Phase 1: Detect cycle
    while tortoise != hare:
        tortoise = f(tortoise)
        hare = f(f(hare))

    # Phase 2: Find the start of the cycle
    tortoise = x0
    while tortoise != hare:
        tortoise = f(tortoise)
        hare = f(hare)

    return tortoise  # This is the start of the cycle

# Example usage:
def sequence_function(x):
    # This function defines the sequence.
    # For this example, we'll use a simple sequence that cycles.
    return (x * 2 + 1) % 10

# Find the cycle in the sequence
start_of_cycle = floyd_cycle_finding(sequence_function, 0)
print(f"The cycle starts at: {start_of_cycle}")

# Demonstrate the cycle
print("Cycle elements:")
current = start_of_cycle
for _ in range(10):
    print(current, end=" ")
    current = sequence_function(current)
    if current == start_of_cycle:
        break
print()
```

duplicate number:

```python
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        def f(x):
            return nums[x]

        # Phase 1: Detect cycle
        tortoise = f(0)
        hare = f(f(0))
        while tortoise != hare:
            tortoise = f(tortoise)
            hare = f(f(hare))

        # Phase 2: Find the start of the cycle
        tortoise = 0
        while tortoise != hare:
            tortoise = f(tortoise)
            hare = f(hare)

        return tortoise  # This is the duplicate number

# Example usage:
solution = Solution()

# Test cases
print(solution.findDuplicate([1,3,4,2,2]))  # Expected output: 2
print(solution.findDuplicate([3,1,3,4,2]))  # Expected output: 3
print(solution.findDuplicate([3,3,3,3,3]))  # Expected output: 3
```
