## Explanation: Next Permutation

### Analysis of problem & input data

This problem is about finding the next lexicographically greater permutation of a given array of integers. The key principle that makes this question simple is understanding the pattern of lexicographical ordering and how to manipulate the array to find the next permutation efficiently.

Important characteristics of the problem:

1. We're dealing with permutations, which are arrangements of elements.
2. The goal is to find the next greater permutation, not just any greater permutation.
3. If no greater permutation exists, we need to return the smallest permutation (sorted in ascending order).
4. The solution must be in-place and use constant extra memory.

The pattern-matching here is to recognize that this problem is about finding a specific rearrangement of elements. The optimal solution leverages the properties of lexicographical ordering to efficiently find the next permutation without generating all possible permutations.

Explainer of intuition: [YouTube video](https://www.youtube.com/watch?v=quAS1iydq7U)

### Test cases

1. Normal case: `[1,2,3]` → `[1,3,2]`
2. Descending order (no next permutation): `[3,2,1]` → `[1,2,3]`
3. Duplicate elements: `[1,1,5]` → `[1,5,1]`
4. Larger array: `[1,3,5,4,2]` → `[1,4,2,3,5]`
5. All elements same: `[1,1,1]` → `[1,1,1]`
6. Two elements: `[1,2]` → `[2,1]`
7. Single element: `[1]` → `[1]`

Here's the Python code for these test cases:

```python
def next_permutation(nums):
    # Implementation will go here
    pass

# Test cases
test_cases = [
    [1,2,3],
    [3,2,1],
    [1,1,5],
    [1,3,5,4,2],
    [1,1,1],
    [1,2],
    [1]
]

for case in test_cases:
    original = case.copy()
    next_permutation(case)
    print(f"Input: {original}, Output: {case}")
```

### Solutions

#### Overview of solution approaches

##### Solutions worth learning

1. Two-pointers approach with reverse (Neetcode solution)
2. Single-pass approach

Count: 2 solutions (1 Neetcode solution)

##### Rejected solutions

1. Generating all permutations and sorting them
2. Recursive backtracking to generate next permutation

#### Worthy Solutions

##### Two-pointers approach with reverse (Neetcode solution)

```python
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Find the first pair from the right where nums[i] < nums[i+1]
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        if i >= 0:
            # Find the smallest number on the right side of nums[i] that is greater than nums[i]
            j = len(nums) - 1
            while j > i and nums[j] <= nums[i]:
                j -= 1
            # Swap nums[i] and nums[j]
            nums[i], nums[j] = nums[j], nums[i]

        # Reverse the subarray to the right of i
        left, right = i + 1, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
```

Time Complexity: O(n), where n is the length of the input array. We traverse the array at most twice.
Space Complexity: O(1), as we only use a constant amount of extra space.

Explanation of time and space complexity:

- Time: We traverse the array once from right to left to find the first pair where nums[i] < nums[i+1]. In the worst case, this takes O(n) time. Then, we might traverse again to find the smallest number greater than nums[i], which is another O(n) operation. Finally, we reverse a portion of the array, which is also O(n). So, the total time complexity is O(n).
- Space: We only use a few additional variables (i, j, left, right) regardless of the input size, so the space complexity is O(1).

Intuitions and invariants:

- The subarray to the right of the found index i is always in descending order before the swap.
- Swapping with the smallest number greater than nums[i] ensures we get the next lexicographically greater permutation.
- Reversing the subarray after the swap transforms it into ascending order, which is the smallest possible arrangement for that subarray.

##### Single-pass approach

```python
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = n - 2

        # Find the first pair from the right where nums[i] < nums[i+1]
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        if i >= 0:
            j = n - 1
            # Find the smallest number on the right side of nums[i] that is greater than nums[i]
            # and swap in a single pass
            while j > i:
                if nums[j] > nums[i]:
                    nums[i], nums[j] = nums[j], nums[i]
                    break
                j -= 1

        # Reverse the subarray to the right of i
        left, right = i + 1, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
```

Time Complexity: O(n), where n is the length of the input array. We traverse the array at most twice.
Space Complexity: O(1), as we only use a constant amount of extra space.

Explanation of time and space complexity:

- Time: We traverse the array once from right to left to find the first pair where nums[i] < nums[i+1], which takes O(n) time in the worst case. Then, we traverse again from right to left to find the smallest number greater than nums[i] and perform the swap, which is another O(n) operation. Finally, we reverse a portion of the array, which is also O(n). So, the total time complexity is O(n).
- Space: We only use a few additional variables (i, j, left, right, n) regardless of the input size, so the space complexity is O(1).

Intuitions and invariants:

- The subarray to the right of the found index i is always in descending order before the swap.
- By traversing from right to left, we ensure that we find the smallest number greater than nums[i] in a single pass.
- Reversing the subarray after the swap transforms it into ascending order, which is the smallest possible arrangement for that subarray.

#### Rejected Approaches

1. Generating all permutations and sorting them:

   - This approach would involve generating all possible permutations of the input array, sorting them lexicographically, and then finding the next permutation after the given one.
   - Rejected because: The time complexity would be O(n! \* n log n) for generating and sorting all permutations, which is extremely inefficient for large inputs. It also uses much more than constant extra memory.

2. Recursive backtracking to generate next permutation:
   - This approach would involve using recursive backtracking to generate permutations one by one until we find the one that comes next after the given permutation.
   - Rejected because: While this could work, it's unnecessarily complex and potentially inefficient. The time complexity could be O(n!) in the worst case, which is much worse than the O(n) solution we have.

#### Final Recommendations

The two-pointers approach with reverse (Neetcode solution) is the best solution to learn for this problem. It's efficient, intuitive, and demonstrates a good understanding of array manipulation and permutation properties. The single-pass approach is a slight optimization but may be harder to understand and implement correctly in an interview setting.

### Visualization(s)

To visualize the algorithm, let's consider the example [1,3,5,4,2]:

1. Find the first pair from right where nums[i] < nums[i+1]:
   [1,3,5,**4**,2] (i = 2)
2. Find the smallest number on the right side of nums[i] that is greater than nums[i]:
   [1,3,5,4,**2**] (j = 4)
3. Swap nums[i] and nums[j]:
   [1,3,**2**,4,**5**]
4. Reverse the subarray to the right of i:
   [1,3,2,**5,4**]

Final result: [1,3,2,5,4]

This visualization helps to understand how the algorithm transforms the array step by step to find the next permutation.
