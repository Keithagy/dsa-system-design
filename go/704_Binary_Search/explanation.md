## Explanation: Binary Search

### Analysis of problem & input data

This problem is a classic example of binary search, which is an efficient algorithm for searching a sorted array. The key characteristics that make binary search applicable here are:

1. The input array `nums` is sorted in ascending order.
2. We're searching for a specific `target` value.
3. The requirement for O(log n) runtime complexity.

The sorted nature of the array allows us to eliminate half of the remaining search space in each step, leading to the logarithmic time complexity. This is the key principle that makes the question simple: in a sorted array, we can always determine which half of the array our target is in, allowing us to discard the other half.

Binary search is optimal for this problem because:

- It meets the O(log n) runtime requirement.
- It takes advantage of the sorted property of the input array.
- It's space-efficient, using only a constant amount of extra space.

Pattern matching: Whenever you see a problem involving searching in a sorted array with a requirement for logarithmic time complexity, binary search should be your go-to algorithm.

### Test cases

1. Normal case: `nums = [-1,0,3,5,9,12], target = 9` (Expected output: 4)
2. Target not in array: `nums = [-1,0,3,5,9,12], target = 2` (Expected output: -1)
3. Target at the beginning: `nums = [-1,0,3,5,9,12], target = -1` (Expected output: 0)
4. Target at the end: `nums = [-1,0,3,5,9,12], target = 12` (Expected output: 5)
5. Single element array, target present: `nums = [5], target = 5` (Expected output: 0)
6. Single element array, target not present: `nums = [5], target = 3` (Expected output: -1)
7. Two element array: `nums = [1,3], target = 3` (Expected output: 1)
8. Large array: `nums = [-10000, ..., 10000], target = 9999` (Expected output: corresponding index)

Here's the Go code to set up these test cases:

```go
func runTestCases(search func([]int, int) int) {
    testCases := []struct {
        nums   []int
        target int
        want   int
    }{
        {[]int{-1, 0, 3, 5, 9, 12}, 9, 4},
        {[]int{-1, 0, 3, 5, 9, 12}, 2, -1},
        {[]int{-1, 0, 3, 5, 9, 12}, -1, 0},
        {[]int{-1, 0, 3, 5, 9, 12}, 12, 5},
        {[]int{5}, 5, 0},
        {[]int{5}, 3, -1},
        {[]int{1, 3}, 3, 1},
    }

    for i, tc := range testCases {
        got := search(tc.nums, tc.target)
        if got != tc.want {
            fmt.Printf("Test case %d failed. Got: %d, Want: %d\n", i, got, tc.want)
        } else {
            fmt.Printf("Test case %d passed.\n", i)
        }
    }
}
```

### Solutions

#### Overview of solution approaches

##### Solutions worth learning

1. Iterative Binary Search (Neetcode solution)
2. Recursive Binary Search
3. Two-pointer Binary Search

Count: 3 solutions (1 Neetcode solution)

##### Rejected solutions

1. Linear search: O(n) time complexity, doesn't meet the O(log n) requirement.
2. Built-in search functions: While Go's `sort.SearchInts` could be used, it's important to understand the underlying algorithm for interview purposes.

#### Worthy Solutions

##### Iterative Binary Search (Neetcode solution)

```go
func search(nums []int, target int) int {
    left, right := 0, len(nums)-1

    for left <= right {
        mid := left + (right-left)/2 // Avoid potential integer overflow
        if nums[mid] == target {
            return mid
        } else if nums[mid] < target {
            left = mid + 1 // Target is in the right half
        } else {
            right = mid - 1 // Target is in the left half
        }
    }

    return -1 // Target not found
}
```

Time Complexity: O(log n)

- The search space is halved in each iteration, leading to a logarithmic number of steps.
- In the worst case, we make log₂(n) comparisons before either finding the target or concluding it's not in the array.

Space Complexity: O(1)

- We only use a constant amount of extra space (variables `left`, `right`, and `mid`), regardless of the input size.

Key intuitions and invariants:

- The `left` and `right` pointers always maintain the current search range.
- The `mid` element splits the current search range into two halves.
- After each comparison, we can eliminate half of the remaining search space.
- The loop continues as long as there's a valid search range (`left <= right`).
- If the loop ends without finding the target, it means the target is not in the array.

##### Recursive Binary Search

```go
func search(nums []int, target int) int {
    return binarySearch(nums, target, 0, len(nums)-1)
}

func binarySearch(nums []int, target, left, right int) int {
    if left > right {
        return -1 // Base case: target not found
    }

    mid := left + (right-left)/2
    if nums[mid] == target {
        return mid
    } else if nums[mid] < target {
        return binarySearch(nums, target, mid+1, right) // Search right half
    } else {
        return binarySearch(nums, target, left, mid-1) // Search left half
    }
}
```

Time Complexity: O(log n)

- Each recursive call reduces the search space by half, resulting in a logarithmic number of calls.
- The recursion depth is log₂(n) in the worst case.

Space Complexity: O(log n)

- The space complexity is O(log n) due to the recursive call stack.
- Each recursive call adds a new frame to the stack, and there are at most log₂(n) frames.

Key intuitions and invariants:

- The recursive approach maintains the same invariants as the iterative version.
- The base case (`left > right`) handles the situation when the target is not found.
- Each recursive call narrows down the search range by choosing either the left or right half.
- The recursion naturally maintains the search range without explicit `left` and `right` variables in a loop.

##### Two-pointer Binary Search

```go
func search(nums []int, target int) int {
    left, right := 0, len(nums)-1

    for left < right {
        mid := left + (right-left)/2
        if nums[mid] < target {
            left = mid + 1
        } else {
            right = mid
        }
    }

    if nums[left] == target {
        return left
    }
    return -1
}
```

Time Complexity: O(log n)

- Similar to the standard binary search, we halve the search space in each iteration.
- The loop runs log₂(n) times in the worst case.

Space Complexity: O(1)

- We only use a constant amount of extra space, regardless of the input size.

Key intuitions and invariants:

- This approach maintains the invariant that the target, if it exists, is always in the range [left, right].
- The loop continues until `left` and `right` converge to a single index.
- After the loop, we only need to check if the element at `left` is the target.
- This method is particularly useful when you need to find the leftmost occurrence of the target in case of duplicates (though not applicable in this specific problem due to the uniqueness constraint).

#### Rejected Approaches

1. Linear Search (O(n)):

   ```go
   func linearSearch(nums []int, target int) int {
       for i, num := range nums {
           if num == target {
               return i
           }
       }
       return -1
   }
   ```

   This approach is rejected because it doesn't meet the O(log n) runtime complexity requirement. It checks each element sequentially, leading to O(n) time complexity in the worst case.

2. Using built-in `sort.SearchInts`:

   ```go
   import "sort"

   func builtInSearch(nums []int, target int) int {
       i := sort.SearchInts(nums, target)
       if i < len(nums) && nums[i] == target {
           return i
       }
       return -1
   }
   ```

   While this approach uses binary search internally and meets the time complexity requirement, it's not recommended for interview settings. It's important to demonstrate understanding of the algorithm rather than relying on built-in functions.

#### Final Recommendations

For this problem, I recommend learning and implementing the Iterative Binary Search solution (Neetcode solution). Here's why:

1. It's the most straightforward and commonly used implementation of binary search.
2. It has optimal time complexity (O(log n)) and space complexity (O(1)).
3. It's easier to reason about and debug compared to the recursive version.
4. It avoids the potential stack overflow issues that could occur with the recursive approach for very large inputs.
5. It's more memory-efficient than the recursive approach, which uses O(log n) space due to the call stack.

The two-pointer approach, while interesting, doesn't provide significant advantages for this specific problem and may be slightly less intuitive.

Understanding the iterative binary search thoroughly will serve you well in coding interviews and provides a solid foundation for more complex binary search variations.

### Visualization(s)

To visualize the binary search algorithm, we can use a simple ASCII representation:

```
Initial array: [-1, 0, 3, 5, 9, 12]
Target: 9

Step 1:  [-1, 0, 3, 5, 9, 12]
          ^        ^        ^
         left     mid     right

Step 2:  [-1, 0, 3, 5, 9, 12]
                    ^  ^  ^
                   left mid right

Step 3:  [-1, 0, 3, 5, 9, 12]
                       ^
                    left
                     mid
                    right

Target found at index 4
```

This visualization shows how the `left`, `mid`, and `right` pointers move during the search process, narrowing down the search range until the target is found.
