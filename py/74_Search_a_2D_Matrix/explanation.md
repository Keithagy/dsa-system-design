## Explanation: Search a 2D Matrix

### Analysis of problem & input data

This problem presents us with a 2D matrix with specific properties and asks us to search for a target value efficiently. The key characteristics of the input that guide our solution are:

1. Each row is sorted in non-decreasing order.
2. The first integer of each row is greater than the last integer of the previous row.
3. We need to achieve O(log(m \* n)) time complexity.

These properties effectively make the entire 2D matrix a sorted 1D array when read row by row. This insight is crucial because it allows us to apply binary search, which is the go-to algorithm for searching in sorted arrays with logarithmic time complexity.

The key principle that makes this question simple is recognizing that we can treat the 2D matrix as a 1D sorted array and perform a single binary search, rather than searching each row individually. This approach satisfies the O(log(m \* n)) time complexity requirement.

### Test cases

1. Standard case (target present):

   ```python
   matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
   target = 3
   # Expected output: True
   ```

2. Standard case (target not present):

   ```python
   matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
   target = 13
   # Expected output: False
   ```

3. Edge case (single element matrix):

   ```python
   matrix = [[1]]
   target = 1
   # Expected output: True
   ```

4. Edge case (target smaller than smallest element):

   ```python
   matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
   target = 0
   # Expected output: False
   ```

5. Edge case (target larger than largest element):

   ```python
   matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
   target = 61
   # Expected output: False
   ```

6. Edge case (target at the beginning of a row):

   ```python
   matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
   target = 10
   # Expected output: True
   ```

7. Edge case (target at the end of a row):
   ```python
   matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
   target = 20
   # Expected output: True
   ```

Here's the executable Python code for these test cases:

```python
def search_matrix(matrix: List[List[int]], target: int) -> bool:
    # Implementation will go here
    pass

# Test cases
test_cases = [
    ([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3, True),
    ([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13, False),
    ([[1]], 1, True),
    ([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 0, False),
    ([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 61, False),
    ([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 10, True),
    ([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 20, True),
]

for i, (matrix, target, expected) in enumerate(test_cases):
    result = search_matrix(matrix, target)
    print(f"Test case {i+1}: {'Passed' if result == expected else 'Failed'}")
    if result != expected:
        print(f"  Expected: {expected}, Got: {result}")
```

### Solutions

#### Overview of solution approaches

##### Solutions worth learning

1. Single Binary Search (Neetcode solution)
2. Two Binary Searches

Count: 2 solutions (1 Neetcode solution)

##### Rejected solutions

1. Linear Search: While correct, it doesn't meet the time complexity requirement.
2. Binary Search on Each Row: Although this would work, it's not as efficient as treating the entire matrix as a single sorted array.

#### Worthy Solutions

##### Single Binary Search

```python
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        rows, cols = len(matrix), len(matrix[0])
        left, right = 0, rows * cols - 1

        while left <= right:
            mid = (left + right) // 2
            # Convert 1D index to 2D coordinates
            row, col = divmod(mid, cols)
            value = matrix[row][col]

            if value == target:
                return True
            elif value < target:
                left = mid + 1
            else:
                right = mid - 1

        return False
```

Time Complexity: O(log(m \* n)), where m is the number of rows and n is the number of columns.
Space Complexity: O(1)

Explanation of time complexity:

- We perform a single binary search on the entire matrix, treating it as a 1D sorted array of length m \* n.
- Each iteration of the binary search reduces the search space by half.
- The number of iterations is logarithmic in the total number of elements, hence log(m \* n).

Explanation of space complexity:

- We only use a constant amount of extra space for variables (left, right, mid, row, col), regardless of the input size.

Key intuitions and invariants:

- The matrix can be treated as a single sorted array due to its properties.
- We can convert between 1D index and 2D coordinates using division and modulo operations.
- The binary search invariant is maintained: the target, if it exists, is always within the current search range.

##### Two Binary Searches

```python
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        # Binary search to find the potential row
        top, bottom = 0, len(matrix) - 1
        while top <= bottom:
            mid_row = (top + bottom) // 2
            if matrix[mid_row][0] <= target <= matrix[mid_row][-1]:
                # Target might be in this row, perform binary search on the row
                return self.binary_search_row(matrix[mid_row], target)
            elif target < matrix[mid_row][0]:
                bottom = mid_row - 1
            else:
                top = mid_row + 1

        return False

    def binary_search_row(self, row: List[int], target: int) -> bool:
        left, right = 0, len(row) - 1
        while left <= right:
            mid = (left + right) // 2
            if row[mid] == target:
                return True
            elif row[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False
```

Time Complexity: O(log m + log n), where m is the number of rows and n is the number of columns.
Space Complexity: O(1)

Explanation of time complexity:

- We perform two binary searches:
  1. First on the rows to find the potential row containing the target: O(log m)
  2. Then on the selected row to find the target: O(log n)
- The total time complexity is the sum of these: O(log m + log n)
- Note that O(log m + log n) = O(log(m \* n)), satisfying the problem's requirement

Explanation of space complexity:

- We only use a constant amount of extra space for variables, regardless of the input size.

Key intuitions and invariants:

- We can eliminate rows quickly by comparing the target with the first and last elements of each row.
- Once we've found a potential row, we can perform a standard binary search on that row.
- This approach leverages both properties of the matrix: sorted rows and increasing first elements across rows.

#### Rejected Approaches

1. Linear Search (O(m \* n) time complexity):

   ```python
   def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
       for row in matrix:
           for element in row:
               if element == target:
                   return True
       return False
   ```

   This approach is rejected because it doesn't meet the O(log(m \* n)) time complexity requirement. It's inefficient for large matrices and doesn't utilize the sorted nature of the input.

2. Binary Search on Each Row (O(m \* log n) time complexity):
   ```python
   def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
       for row in matrix:
           if self.binary_search_row(row, target):
               return True
       return False
   ```
   While this approach is better than linear search, it's still not optimal. It doesn't fully utilize the property that the first element of each row is greater than the last element of the previous row, leading to unnecessary searches in some cases.

#### Final Recommendations

The Single Binary Search approach (Neetcode solution) is recommended as the best solution to learn for this problem. Here's why:

1. It fully utilizes both properties of the matrix, treating it as a single sorted array.
2. It achieves the required O(log(m \* n)) time complexity in the most straightforward manner.
3. It's more space-efficient and conceptually simpler than the Two Binary Searches approach.
4. It demonstrates a clever technique of treating a 2D structure as 1D, which can be applicable in other problems.

While the Two Binary Searches approach is also valid and meets the time complexity requirement, the Single Binary Search is more elegant and efficient in practice, as it performs only one binary search instead of two.

### Visualization(s)

To visualize the Single Binary Search approach, we can create a simple React component that demonstrates how the algorithm works on a given matrix. Here's a visualization that shows the binary search process:

```tsx
import React, { useState, useEffect } from "react";
import { Button, Input } from "@/components/ui/button";

const MatrixSearchVisualization = () => {
  const [matrix, setMatrix] = useState([
    [1, 3, 5, 7],
    [10, 11, 16, 20],
    [23, 30, 34, 60],
  ]);
  const [target, setTarget] = useState(3);
  const [currentStep, setCurrentStep] = useState(0);
  const [searchSteps, setSearchSteps] = useState([]);
  const [found, setFound] = useState(false);

  const searchMatrix = () => {
    const rows = matrix.length;
    const cols = matrix[0].length;
    let left = 0;
    let right = rows * cols - 1;
    const steps = [];

    while (left <= right) {
      const mid = Math.floor((left + right) / 2);
      const [row, col] = [Math.floor(mid / cols), mid % cols];
      const value = matrix[row][col];

      steps.push({ left, right, mid, row, col, value });

      if (value === target) {
        setFound(true);
        break;
      } else if (value < target) {
        left = mid + 1;
      } else {
        right = mid - 1;
      }
    }

    setSearchSteps(steps);
    setCurrentStep(0);
  };

  useEffect(() => {
    searchMatrix();
  }, [target]);

  const handleNextStep = () => {
    if (currentStep < searchSteps.length - 1) {
      setCurrentStep(currentStep + 1);
    }
  };

  const handlePrevStep = () => {
    if (currentStep > 0) {
      setCurrentStep(currentStep - 1);
    }
  };

  return (
    <div className="p-4">
      <h2 className="text-2xl font-bold mb-4">
        2D Matrix Search Visualization
      </h2>
      <div className="mb-4">
        <Input
          type="number"
          value={target}
          onChange={(e) => setTarget(parseInt(e.target.value))}
          placeholder="Enter target"
          className="mr-2"
        />
        <Button onClick={searchMatrix}>Search</Button>
      </div>
      <div className="grid grid-cols-4 gap-2 mb-4">
        {matrix.flat().map((value, index) => (
          <div
            key={index}
            className={`p-2 border ${
              searchSteps[currentStep] &&
              Math.floor(index / 4) === searchSteps[currentStep].row &&
              index % 4 === searchSteps[currentStep].col
                ? "bg-yellow-200"
                : ""
            }`}
          >
            {value}
          </div>
        ))}
      </div>
      <div className="mb-4">
        <Button onClick={handlePrevStep} disabled={currentStep === 0}>
          Previous Step
        </Button>
        <Button
          onClick={handleNextStep}
          disabled={currentStep === searchSteps.length - 1}
        >
          Next Step
        </Button>
      </div>
      <div>
        {searchSteps[currentStep] && (
          <p>
            Step {currentStep + 1}: Checking value{" "}
            {searchSteps[currentStep].value} at position (
            {searchSteps[currentStep].row}, {searchSteps[currentStep].col})
          </p>
        )}
        {found && <p>Target {target} found in the matrix!</p>}
        {!found && currentStep === searchSteps.length - 1 && (
          <p>Target {target} not found in the matrix.</p>
        )}
      </div>
    </div>
  );
};

export default MatrixSearchVisualization;
```

This visualization allows you to:

1. Input a target value
2. See the matrix with the current search position highlighted
3. Step through the binary search process
4. Observe how the algorithm narrows down the search range

This visual representation helps reinforce the concept of treating the 2D matrix as a 1D sorted array and shows how the binary search efficiently finds (or doesn't find) the target value.
