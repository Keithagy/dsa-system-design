## Explanation: Find K Closest Elements

### Analysis of problem & input data

This problem involves finding the k closest elements to a given value x in a sorted array. The key aspects to consider are:

1. The array is already sorted in ascending order.
2. We need to find k elements that are closest to x.
3. The closeness is determined by the absolute difference |a - x|.
4. In case of a tie (same absolute difference), the smaller element is considered closer.
5. The result should be sorted in ascending order.

The sorted nature of the input array is a crucial characteristic that enables efficient solutions. This problem can be approached in several ways, but the most optimal solutions leverage the sorted property of the array.

The key principle that makes this question simple is the realization that the k closest elements will always form a contiguous subarray in the original sorted array. This is because if we have found k-1 closest elements and are deciding between two elements for the kth position, we will always choose the one closer to the center of our current subarray.

### Test cases

1. Standard case:

   - Input: arr = [1,2,3,4,5], k = 4, x = 3
   - Expected Output: [1,2,3,4]

2. Target outside array (left):

   - Input: arr = [1,2,3,4,5], k = 4, x = -1
   - Expected Output: [1,2,3,4]

3. Target outside array (right):

   - Input: arr = [1,2,3,4,5], k = 4, x = 10
   - Expected Output: [2,3,4,5]

4. K equals array length:

   - Input: arr = [1,2,3,4,5], k = 5, x = 3
   - Expected Output: [1,2,3,4,5]

5. K equals 1:

   - Input: arr = [1,2,3,4,5], k = 1, x = 3
   - Expected Output: [3]

6. Array with duplicates:

   - Input: arr = [1,1,1,10,10,10], k = 1, x = 9
   - Expected Output: [10]

7. Large array:
   - Input: arr = list(range(1, 10001)), k = 100, x = 5000
   - Expected Output: list(range(4951, 5051))

Here's the Python code for these test cases:

```python
def test_find_closest_elements(find_closest_elements):
    assert find_closest_elements([1,2,3,4,5], 4, 3) == [1,2,3,4]
    assert find_closest_elements([1,2,3,4,5], 4, -1) == [1,2,3,4]
    assert find_closest_elements([1,2,3,4,5], 4, 10) == [2,3,4,5]
    assert find_closest_elements([1,2,3,4,5], 5, 3) == [1,2,3,4,5]
    assert find_closest_elements([1,2,3,4,5], 1, 3) == [3]
    assert find_closest_elements([1,1,1,10,10,10], 1, 9) == [10]
    assert find_closest_elements(list(range(1, 10001)), 100, 5000) == list(range(4951, 5051))
    print("All test cases passed!")

# You can run this test function with your implementation like this:
# test_find_closest_elements(find_closest_elements)
```

### Solutions

#### Overview of solution approaches

##### Solutions worth learning

1. Binary Search + Two Pointers (Neetcode solution)
2. Binary Search for Left Bound
3. Sorting with Custom Comparator
4. Heap-based approach

Count: 4 solutions (1 Neetcode solution)

##### Rejected solutions

1. Brute Force approach: Calculating the difference for all elements and sorting.
2. Sliding Window approach: While it might seem intuitive, it's not as efficient as the binary search approaches.

#### Worthy Solutions

##### Binary Search + Two Pointers (Neetcode solution)

```python
from typing import List

def find_closest_elements(arr: List[int], k: int, x: int) -> List[int]:
    left, right = 0, len(arr) - k

    while left < right:
        mid = (left + right) // 2
        # Compare the distance from x to the start and end of the k-sized window
        if x - arr[mid] > arr[mid + k] - x:
            left = mid + 1
        else:
            right = mid

    return arr[left:left + k]
```

Time Complexity: O(log(n-k) + k), where n is the length of the array. The binary search takes O(log(n-k)) time, and slicing the final result takes O(k) time.
Space Complexity: O(1) if we don't count the output array, O(k) if we do.

- This solution leverages the sorted nature of the array to perform a binary search.
- Instead of searching for x directly, it searches for the left bound of the k-element window.
- The key insight is comparing the distances from x to the start and end of the current k-sized window.
- If x - arr[mid] > arr[mid + k] - x, it means the window should move to the right.
- The binary search narrows down the left bound of the k-element window.
- Once the left bound is found, we can simply return the k elements starting from that index.

##### Binary Search for Left Bound

```python
from typing import List

def find_closest_elements(arr: List[int], k: int, x: int) -> List[int]:
    left, right = 0, len(arr) - k

    while left < right:
        mid = (left + right) // 2
        # If x is closer to arr[mid+k], move the window to the right
        if x - arr[mid] > arr[mid+k] - x:
            left = mid + 1
        else:
            right = mid

    return arr[left:left+k]
```

Time Complexity: O(log(n-k) + k), where n is the length of the array. The binary search takes O(log(n-k)) time, and slicing the final result takes O(k) time.
Space Complexity: O(1) if we don't count the output array, O(k) if we do.

- This solution is very similar to the Neetcode solution, but it's presented here to emphasize the binary search aspect.
- The key intuition is to find the left bound of the k-element window that contains the closest elements.
- The binary search compares the distance from x to the start and end of the current k-sized window.
- If x is closer to arr[mid+k] than to arr[mid], we move the window to the right.
- This approach efficiently narrows down the search space to find the optimal left bound.

##### Sorting with Custom Comparator

```python
from typing import List

def find_closest_elements(arr: List[int], k: int, x: int) -> List[int]:
    # Sort the array based on the custom comparator
    sorted_arr = sorted(arr, key=lambda num: (abs(num - x), num))

    # Return the first k elements, sorted in ascending order
    return sorted(sorted_arr[:k])
```

Time Complexity: O(n log n), where n is the length of the array, due to the sorting operations.
Space Complexity: O(n) for the sorted array.

- This solution uses Python's built-in sorting with a custom key function.
- The key function (abs(num - x), num) creates a tuple for each element.
- Sorting is first done based on the absolute difference from x, then by the element value itself.
- This approach directly implements the problem's definition of "closeness".
- While not as efficient as the binary search approaches, it's intuitive and demonstrates understanding of custom sorting.

##### Heap-based approach

```python
import heapq
from typing import List

def find_closest_elements(arr: List[int], k: int, x: int) -> List[int]:
    # Create a max heap of (abs difference, element) pairs
    heap = [(-abs(num - x), -num) for num in arr]
    heapq.heapify(heap)

    # Keep only k closest elements in the heap
    while len(heap) > k:
        heapq.heappop(heap)

    # Extract elements from the heap and sort them
    return sorted(-pair[1] for pair in heap)
```

Time Complexity: O(n + (n-k)log n + k log k), where n is the length of the array. Heapifying takes O(n), removing n-k elements takes O((n-k)log n), and sorting the final k elements takes O(k log k).
Space Complexity: O(n) for the heap.

- This solution uses a max heap to efficiently find the k closest elements.
- We negate the absolute difference and the element value to turn the min heap into a max heap.
- By keeping only k elements in the heap, we end up with the k closest elements.
- This approach demonstrates understanding of heap operations and their applications.

#### Rejected Approaches

1. Brute Force approach: While correct, it involves calculating the difference for all elements, sorting them, and then selecting the top k. This would have a time complexity of O(n log n) due to sorting, which is less efficient than our binary search solutions.

2. Sliding Window approach: This might seem intuitive given the contiguous nature of the result, but it's not as efficient as the binary search. It would involve sliding a window of size k over the array and comparing each window, resulting in O(n) time complexity.

#### Final Recommendations

The Binary Search + Two Pointers approach (Neetcode solution) is the best to learn for this problem. It's the most efficient in terms of time and space complexity, and it leverages the sorted nature of the input array. This solution demonstrates a deep understanding of binary search and how it can be applied to find a range rather than a single element. It's also the kind of elegant, efficient solution that interviewers love to see in coding interviews.

### Visualization(s)

For this problem, a visualization of the binary search process could be helpful. Here's a simple ASCII representation of how the binary search narrows down the left bound of the k-element window:

```
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], k = 4, x = 6

Initial state:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
 ^                 ^
left              right

Mid-point check:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        ^     ^
       mid   mid+k

Compare: |6-4| > |7-6|, so move left:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
           ^        ^
          left     right

Final state:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
           ^
          left
Result: [4, 5, 6, 7]
```

This visualization helps to understand how the binary search efficiently narrows down the search space to find the optimal left bound of the k-element window.
