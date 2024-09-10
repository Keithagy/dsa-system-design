## Explanation: Largest Number

### Analysis of problem & input data

This problem is essentially about sorting, but with a custom comparison rule. The key insight is that we need to compare numbers based on their contribution to the overall number when concatenated, not their individual values.

The problem's characteristics that enable pattern-matching to a particular solution strategy are:

1. We're dealing with non-negative integers, which can be easily converted to strings for comparison.
2. The order of numbers matters, suggesting a sorting approach.
3. The comparison rule is not straightforward, indicating we need a custom comparator.

The key principle that makes this question simple is understanding that for any two numbers a and b, we need to compare their concatenations "ab" and "ba" to determine their relative order. This is because the goal is to form the largest possible number, and the position of each number in the final result affects its contribution to the overall value.

For example, when comparing 3 and 30:

- "330" > "303", so 3 should come before 30 in our sorted result.

This problem falls into the category of "custom sorting" or "comparator-based sorting" problems, where the challenge lies in defining the correct comparison rule rather than in the sorting algorithm itself.

### Test cases

Here are some test cases to consider:

1. Basic case: `[10, 2]` -> "210"
2. Multiple digits: `[3, 30, 34, 5, 9]` -> "9534330"
3. All single digits: `[1, 2, 3, 4, 5]` -> "54321"
4. Repeated numbers: `[3, 30, 34, 3, 30]` -> "34330330"
5. All zeros: `[0, 0, 0]` -> "0"
6. Single number: `[42]` -> "42"
7. Large numbers: `[8247, 824]` -> "8248247"
8. Edge case with zeros: `[0, 0, 30]` -> "30"

Here's the Python code for these test cases:

```python
def largest_number(nums):
    # Implementation goes here
    pass

test_cases = [
    [10, 2],
    [3, 30, 34, 5, 9],
    [1, 2, 3, 4, 5],
    [3, 30, 34, 3, 30],
    [0, 0, 0],
    [42],
    [8247, 824],
    [0, 0, 30]
]

for i, case in enumerate(test_cases, 1):
    result = largest_number(case)
    print(f"Test case {i}: {case} -> {result}")
```

### Solutions

#### Overview of solution approaches

##### Solutions worth learning

1. Custom Sorting with String Comparison (Neetcode solution)
2. Custom Key Function Sorting
3. Bubble Sort with Custom Comparison

Count: 3 solutions (1 Neetcode solution)

##### Rejected solutions

1. Naive sorting of numbers: This doesn't work because the largest individual numbers don't necessarily form the largest combined number.
2. Greedy approach selecting the largest digit first: This fails for cases like [34, 3, 30].

#### Worthy Solutions

##### Custom Sorting with String Comparison

```python
from typing import List

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # Convert all numbers to strings for easier comparison
        nums = [str(num) for num in nums]

        def compare(n1: str, n2: str) -> int:
            # Compare concatenations in both orders
            if n1 + n2 > n2 + n1:
                return -1
            else:
                return 1

        # Sort using the custom comparison function
        nums.sort(key=functools.cmp_to_key(compare))

        # Join the sorted array and handle the all-zeros case
        return '0' if nums[0] == '0' else ''.join(nums)
```

Time Complexity: O(nlog(n)), where n is the number of elements in the input list.
Space Complexity: O(n) for creating a new list of string representations.

Explanation:

- The time complexity is dominated by the sorting operation, which uses Python's Timsort algorithm with O(nlog(n)) complexity.
- The space complexity is O(n) because we create a new list of string representations of the numbers.

Key intuitions and invariants:

- Converting numbers to strings allows for easy concatenation and comparison.
- The custom comparator ensures that numbers are sorted based on their contribution to the largest number when concatenated.
- The all-zeros case is handled separately to avoid returning a string with leading zeros.

##### Custom Key Function Sorting

```python
from typing import List

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compare_key(x: int) -> str:
            # Create a key for comparison by repeating the number
            return str(x) * 10  # Repeat to handle numbers of different lengths

        # Sort the numbers using the custom key
        sorted_nums = sorted(nums, key=compare_key, reverse=True)

        # Join the sorted numbers and handle the all-zeros case
        result = ''.join(map(str, sorted_nums))
        return '0' if result[0] == '0' else result
```

Time Complexity: O(nlog(n)), where n is the number of elements in the input list.
Space Complexity: O(n) for creating the sorted list and the final string.

Explanation:

- The time complexity is O(nlog(n)) due to the sorting operation.
- The space complexity is O(n) for storing the sorted list and the final string result.

Key intuitions and invariants:

- By repeating each number (as a string) multiple times, we create a key that naturally sorts numbers based on their contribution to the largest number.
- This approach avoids the need for a custom comparison function, simplifying the implementation.

##### Bubble Sort with Custom Comparison

```python
from typing import List

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compare(n1: int, n2: int) -> bool:
            return str(n1) + str(n2) > str(n2) + str(n1)

        n = len(nums)
        for i in range(n):
            for j in range(n - 1 - i):
                if compare(nums[j+1], nums[j]):
                    nums[j], nums[j+1] = nums[j+1], nums[j]

        return '0' if nums[0] == 0 else ''.join(map(str, nums))
```

Time Complexity: O(n^2), where n is the number of elements in the input list.
Space Complexity: O(1) for in-place sorting (excluding the final string creation).

Explanation:

- The time complexity is O(n^2) due to the nested loops in the bubble sort algorithm.
- The space complexity is O(1) as we sort the list in-place, only using a constant amount of extra space.

Key intuitions and invariants:

- The custom comparison function ensures that numbers are sorted based on their contribution to the largest number when concatenated.
- Bubble sort is used here to demonstrate the concept, but it's not the most efficient sorting algorithm for large inputs.

#### Rejected Approaches

1. Sorting numbers directly: This approach fails because the largest individual numbers don't necessarily form the largest combined number. For example, sorting [3, 30, 34] would give [34, 30, 3], but the correct order is [34, 3, 30].

2. Greedy approach selecting the largest digit first: This fails for cases like [34, 3, 30]. It would choose 34 first, then 3, then 30, resulting in "34330" instead of the correct "34330".

3. Radix sort: While radix sort can be efficient for sorting integers, it doesn't directly solve our problem because we need to compare numbers based on their concatenated values, not their individual digit values.

#### Final Recommendations

The Custom Sorting with String Comparison (Neetcode solution) is the best to learn for several reasons:

1. It's the most intuitive solution that directly addresses the problem's core concept.
2. It has optimal time complexity (O(nlog(n))) and reasonable space complexity (O(n)).
3. It demonstrates how to use a custom comparator in Python's sorting function, which is a valuable skill for many algorithm problems.
4. It handles all edge cases, including the all-zeros case.

While the Custom Key Function Sorting is also efficient and elegant, the String Comparison method more clearly demonstrates the problem-solving thought process and is likely to be more generalizable to similar problems.

### Visualization(s)

For this problem, a visualization of the sorting process might be helpful. Here's a simple ASCII representation of how the custom sorting would work for the input [3, 30, 34, 5, 9]:

```
Initial: [3, 30, 34, 5, 9]

Compare:
3 vs 30:  330 > 303  ->  [3, 30, 34, 5, 9]
3 vs 34:  334 < 343  ->  [34, 3, 30, 5, 9]
34 vs 5:  345 > 534  ->  [5, 34, 3, 30, 9]
5 vs 9:   59 < 95    ->  [9, 5, 34, 3, 30]

Final: [9, 5, 34, 3, 30]

Result: "9534330"
```

This visualization shows how each pair of numbers is compared based on their concatenated values, and how this leads to the final sorted order that produces the largest number when concatenated.
