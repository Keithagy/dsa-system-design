## Explanation: Kth Largest Element in an Array

### Analysis of problem & input data

This problem asks us to find the kth largest element in an unsorted array. The key aspects to consider are:

1. The array is unsorted, which immediately suggests we need an efficient way to find the kth largest element without fully sorting the array.
2. We're looking for the kth largest, not the kth distinct largest. This means duplicate elements count in the ranking.
3. The problem explicitly asks if we can solve it without sorting, hinting at more optimal solutions than a naive sort-and-index approach.
4. The constraints show that the array can be quite large (up to 10^5 elements), emphasizing the need for an efficient solution.

The key principle that makes this question simple is the concept of partitioning used in quicksort. We can use this principle to find the kth largest element without fully sorting the array, which leads us to the QuickSelect algorithm.

### Test cases

1. Regular case: `nums = [3,2,1,5,6,4], k = 2` (Expected output: 5)
2. Array with duplicates: `nums = [3,2,3,1,2,4,5,5,6], k = 4` (Expected output: 4)
3. Edge case - k is 1 (largest element): `nums = [1,2,3,4,5], k = 1` (Expected output: 5)
4. Edge case - k is the length of the array (smallest element): `nums = [1,2,3,4,5], k = 5` (Expected output: 1)
5. Array with all identical elements: `nums = [1,1,1,1,1], k = 3` (Expected output: 1)
6. Large array: `nums = list(range(100000, 0, -1)), k = 50000` (Expected output: 50001)

Here's the Python code for these test cases:

```python
def find_kth_largest(nums: List[int], k: int) -> int:
    # Implementation goes here
    pass

# Test cases
test_cases = [
    ([3,2,1,5,6,4], 2, 5),
    ([3,2,3,1,2,4,5,5,6], 4, 4),
    ([1,2,3,4,5], 1, 5),
    ([1,2,3,4,5], 5, 1),
    ([1,1,1,1,1], 3, 1),
    (list(range(100000, 0, -1)), 50000, 50001)
]

for i, (nums, k, expected) in enumerate(test_cases, 1):
    result = find_kth_largest(nums, k)
    print(f"Test case {i}: {'Passed' if result == expected else 'Failed'}")
    if result != expected:
        print(f"  Expected {expected}, but got {result}")
```

### Solutions

#### Overview of solution approaches

##### Solutions worth learning

1. QuickSelect algorithm (Hoare's selection algorithm) [Neetcode solution]
2. Heap-based approach (using a min-heap) [Neetcode solution]
3. Sorting approach (though not optimal, it's simple and worth knowing)

Count: 3 solutions (2 Neetcode solutions)

##### Rejected solutions

1. Naive approach: Sorting the entire array and returning the kth element from the end (rejected because it's not optimal for large arrays and doesn't meet the "without sorting" challenge)
2. Using a max-heap (rejected because a min-heap is more efficient for this problem)

#### Worthy Solutions

##### QuickSelect Algorithm

```python
import random

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quickSelect(left: int, right: int, k: int) -> int:
            pivot = random.randint(left, right)
            pivot_value = nums[pivot]

            # Move pivot to the end
            nums[pivot], nums[right] = nums[right], nums[pivot]

            # Partition
            store_index = left
            for i in range(left, right):
                if nums[i] < pivot_value:
                    nums[store_index], nums[i] = nums[i], nums[store_index]
                    store_index += 1

            # Move pivot to its final place
            nums[right], nums[store_index] = nums[store_index], nums[right]

            # The pivot is in its final sorted position
            if len(nums) - store_index == k:
                return nums[store_index]
            elif len(nums) - store_index < k:
                # The kth largest is in the left partition
                return quickSelect(left, store_index - 1, k)
            else:
                # The kth largest is in the right partition
                return quickSelect(store_index + 1, right, k)

        return quickSelect(0, len(nums) - 1, k)
```

Time Complexity: O(n) average case, O(n^2) worst case
Space Complexity: O(1)

Explanation of time complexity:

- Average case O(n): On average, the partition reduces the problem size by half in each recursive call. This leads to T(n) = T(n/2) + O(n), which resolves to O(n).
- Worst case O(n^2): If we consistently choose the smallest or largest element as the pivot, we may need to make n recursive calls, each doing O(n) work.

Space complexity is O(1) because we're modifying the array in-place and using only a constant amount of extra space.

Intuition and invariants:

- The QuickSelect algorithm is based on the partitioning step of QuickSort.
- We choose a pivot and partition the array such that elements smaller than the pivot are on the left, and larger elements are on the right.
- After partitioning, the pivot is in its final sorted position.
- We can then determine which partition contains the kth largest element and recursively apply the algorithm to that partition.
- The key invariant is that after each partition, we know exactly how many elements are larger than the pivot.

##### Heap-based Approach

```python
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Create a min-heap of size k
        min_heap = []
        for num in nums:
            if len(min_heap) < k:
                heapq.heappush(min_heap, num)
            elif num > min_heap[0]:
                # If the current number is larger than the smallest in the heap,
                # remove the smallest and add the current number
                heapq.heappop(min_heap)
                heapq.heappush(min_heap, num)

        # The root of the heap is the kth largest element
        return min_heap[0]
```

Time Complexity: O(n log k)
Space Complexity: O(k)

Explanation of time complexity:

- We iterate through all n elements in the list.
- For each element, we might perform a heap operation (push or pop).
- Heap operations are O(log k) where k is the size of the heap.
- Therefore, the total time complexity is O(n log k).

Space complexity is O(k) because we maintain a heap of size k.

Intuition and invariants:

- We use a min-heap of size k to keep track of the k largest elements.
- The smallest element in this heap is the kth largest element overall.
- We only need to keep k elements in the heap at any time.
- If we encounter an element larger than the smallest in our heap, we replace the smallest with this new element.
- At the end, the root of the heap (smallest element in the heap) is our answer.

##### Sorting Approach

```python
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Sort the array in descending order
        nums.sort(reverse=True)
        # Return the kth element (0-indexed)
        return nums[k-1]
```

Time Complexity: O(n log n)
Space Complexity: O(1) or O(n), depending on the sorting algorithm

Explanation of time complexity:

- Sorting the array takes O(n log n) time.
- Accessing the kth element is O(1).
- Therefore, the overall time complexity is dominated by the sorting step: O(n log n).

Space complexity can vary:

- If an in-place sorting algorithm is used (like Heapsort), it's O(1).
- If a non-in-place algorithm is used (like Mergesort), it can be O(n).

Intuition and invariants:

- By sorting the array in descending order, we ensure that the kth element from the start is the kth largest.
- This approach is simple and works for all cases, but it's not the most efficient for large arrays or when k is small compared to n.

#### Rejected Approaches

1. Naive sorting approach: While we included a sorting approach in our solutions, it's worth noting that it doesn't meet the challenge of solving the problem "without sorting". It's included because it's simple and worth knowing, but it's not the most efficient solution, especially for large arrays.

2. Max-heap approach: While using a heap is a good strategy, a max-heap is less efficient than a min-heap for this problem. With a max-heap, we'd need to heapify the entire array (O(n)) and then pop k times (O(k log n)). This is less efficient than the min-heap approach when k is small compared to n.

3. Using a balanced binary search tree: While this would work (inserting all elements and then finding the kth largest), it's overly complex for this problem and doesn't offer any advantages over the heap-based solution.

#### Final Recommendations

The QuickSelect algorithm is the best solution to learn for this problem. It offers the best average-case time complexity (O(n)) and constant space complexity. It's also an excellent example of how partitioning (a fundamental concept in sorting algorithms) can be used to solve selection problems efficiently.

The heap-based approach is also worth learning as it offers a good balance of simplicity and efficiency, especially when k is small compared to n. It's also a great example of how to use a heap data structure effectively.

The sorting approach, while not optimal, is worth knowing for its simplicity and as a baseline solution. It's often a good starting point in an interview before optimizing to more efficient solutions.

### Visualization(s)

For the QuickSelect algorithm, a visual representation of the partitioning process would be helpful. Here's a simple ASCII representation:

```
Initial array: [3, 2, 1, 5, 6, 4]  (k = 2)

Choose pivot (e.g., 4):
[3, 2, 1, 4, 6, 5]
         ^
         pivot

After partitioning:
[3, 2, 1, 4, 6, 5]
      |  |
  < pivot  >= pivot

The pivot (4) is now in its final sorted position.
We need the 2nd largest element, which is in the right partition.

Recurse on right partition:
[6, 5]

Choose pivot (e.g., 5):
[6, 5]
    ^
    pivot

After partitioning:
[6, 5]
 |  |
>= pivot  < pivot

The 2nd largest element (5) is now in its final position.
This is our answer.
```

This visualization helps to understand how the QuickSelect algorithm narrows down the search space in each iteration, focusing only on the partition that contains the kth largest element.
