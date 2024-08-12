# Explanation: Product of Array Except Self

## Analysis of problem & input data

This problem presents an interesting challenge in array manipulation and efficient computation. Let's break down the key aspects:

1. We're given an array of integers and need to return a new array where each element is the product of all other elements except itself.

2. The problem guarantees that the product will fit in a 32-bit integer, which simplifies our approach as we don't need to worry about integer overflow.

3. The constraint of O(n) time complexity without using division forces us to think creatively about how to compute these products efficiently.

4. The follow-up question about O(1) extra space adds another layer of optimization to consider.

5. The input array can contain positive, negative, and zero values, which affects how we handle the computations.

6. The length of the array is at least 2, so we don't need to handle empty or single-element arrays.

Key principle that makes this question simple:
The product of all elements except the current one can be broken down into two parts: the product of all elements to the left of the current element, and the product of all elements to the right. This allows us to build our solution incrementally using two passes through the array.

## Test cases

Let's consider some test cases to cover various scenarios:

1. Basic case:
   Input: [1, 2, 3, 4]
   Expected Output: [24, 12, 8, 6]

2. Array with negative numbers:
   Input: [-1, 1, 0, -3, 3]
   Expected Output: [0, 0, 9, 0, 0]

3. Array with zeros:
   Input: [0, 4, 0]
   Expected Output: [0, 0, 0]

4. Array with one zero:
   Input: [1, 2, 0, 4]
   Expected Output: [0, 0, 8, 0]

5. Array with all ones:
   Input: [1, 1, 1, 1]
   Expected Output: [1, 1, 1, 1]

6. Minimum length array:
   Input: [2, 3]
   Expected Output: [3, 2]

7. Array with extreme values:
   Input: [-30, 30, -30, 30]
   Expected Output: [-27000, 27000, -27000, 27000]

Here's the Python code to run these test cases:

```python
def product_except_self(nums):
    # Implementation will be added later
    pass

test_cases = [
    ([1, 2, 3, 4], [24, 12, 8, 6]),
    ([-1, 1, 0, -3, 3], [0, 0, 9, 0, 0]),
    ([0, 4, 0], [0, 0, 0]),
    ([1, 2, 0, 4], [0, 0, 8, 0]),
    ([1, 1, 1, 1], [1, 1, 1, 1]),
    ([2, 3], [3, 2]),
    ([-30, 30, -30, 30], [-27000, 27000, -27000, 27000])
]

for i, (input_array, expected_output) in enumerate(test_cases):
    result = product_except_self(input_array)
    print(f"Test case {i + 1}:")
    print(f"Input: {input_array}")
    print(f"Expected Output: {expected_output}")
    print(f"Actual Output: {result}")
    print(f"Passed: {result == expected_output}\n")
```

## Solutions

### Overview of solution approaches

#### Solutions worth learning

1. Two-pass approach with prefix and suffix products (O(n) time, O(1) space)
2. Two-pass approach with a single output array (O(n) time, O(1) space)
3. Single-pass approach with running product (O(n) time, O(1) space)

Count: 3 solutions

#### Rejected solutions

1. Naive approach with nested loops (O(n^2) time complexity)
2. Using division operation (violates problem constraint)
3. Calculating total product and dividing (doesn't handle zero elements properly)

### Worthy Solutions

#### 1. Two-pass approach with prefix and suffix products (O(n) time, O(n) space)

```python
from typing import List

def product_except_self(nums: List[int]) -> List[int]:
    n = len(nums)

    # Initialize prefix and suffix product arrays
    prefix_products = [1] * n
    suffix_products = [1] * n

    # Calculate prefix products
    for i in range(1, n):
        prefix_products[i] = prefix_products[i-1] * nums[i-1]

    # Calculate suffix products
    for i in range(n-2, -1, -1):
        suffix_products[i] = suffix_products[i+1] * nums[i+1]

    # Calculate the final result
    result = [prefix_products[i] * suffix_products[i] for i in range(n)]

    return result
```

Time Complexity: O(n)
Space Complexity: O(n)

Intuition and invariants:

- We can break down the product of all elements except the current one into two parts: the product of all elements to the left (prefix) and the product of all elements to the right (suffix).
- By pre-computing these prefix and suffix products, we can then combine them to get the final result for each position.
- The prefix product at index i is the product of all elements from 0 to i-1.
- The suffix product at index i is the product of all elements from i+1 to n-1.
- The final result at index i is the product of prefix[i] and suffix[i].

#### 2. Two-pass approach with a single output array (O(n) time, O(1) space)

```python
from typing import List

def product_except_self(nums: List[int]) -> List[int]:
    n = len(nums)

    # Initialize the output array
    output = [1] * n

    # Calculate prefix products
    prefix_product = 1
    for i in range(n):
        output[i] = prefix_product
        prefix_product *= nums[i]

    # Calculate suffix products and combine with prefix products
    suffix_product = 1
    for i in range(n-1, -1, -1):
        output[i] *= suffix_product
        suffix_product *= nums[i]

    return output
```

Time Complexity: O(n)
Space Complexity: O(1) (excluding the output array)

Intuition and invariants:

- This approach is similar to the previous one but optimizes space usage by using the output array to store intermediate results.
- In the first pass, we store the prefix products in the output array.
- In the second pass, we multiply each element by its corresponding suffix product.
- The invariant maintained is that after the first pass, output[i] contains the product of all elements to the left of nums[i].
- After the second pass, output[i] contains the product of all elements except nums[i].

#### 3. Single-pass approach with running product (O(n) time, O(1) space)

```python
from typing import List

def product_except_self(nums: List[int]) -> List[int]:
    n = len(nums)

    # Initialize the output array
    output = [1] * n

    # Calculate products in a single pass
    left_product = 1
    right_product = 1

    for i in range(n):
        # Update the left product
        output[i] *= left_product
        left_product *= nums[i]

        # Update the right product
        output[n-1-i] *= right_product
        right_product *= nums[n-1-i]

    return output
```

Time Complexity: O(n)
Space Complexity: O(1) (excluding the output array)

Intuition and invariants:

- This approach combines the two passes into a single pass by updating both left and right products simultaneously.
- We maintain two running products: left_product (product of elements to the left) and right_product (product of elements to the right).
- As we iterate, we update the output array from both ends, multiplying by the corresponding running product.
- The invariant is that at each step, output[i] contains the partial product from the left, and output[n-1-i] contains the partial product from the right.
- By the end of the iteration, each position in the output array has been multiplied by both the left and right products, giving us the correct result.

### Rejected Approaches

1. Naive approach with nested loops (O(n^2) time complexity):
   This approach would involve calculating the product for each element by iterating through the entire array, excluding the current element. While correct, it's inefficient for large inputs and doesn't meet the O(n) time complexity requirement.

2. Using division operation:
   A tempting approach might be to calculate the total product of all elements and then divide by each element to get the result. However, this violates the problem constraint of not using division. Additionally, it fails when there are zero elements in the array.

3. Calculating total product and dividing:
   Even if division were allowed, this approach wouldn't work correctly when there are zero elements in the array. It would also face potential issues with integer overflow when calculating the total product.

### Final Recommendations

The recommended solution to learn and implement is the "Two-pass approach with a single output array" (Solution 2). This approach offers the best balance of efficiency, simplicity, and space optimization:

1. It meets the O(n) time complexity requirement.
2. It achieves O(1) extra space complexity (excluding the output array).
3. It's relatively simple to understand and implement.
4. It handles all edge cases, including arrays with zeros.

The single-pass approach (Solution 3) is also excellent and slightly more optimal in terms of the number of iterations, but it might be a bit harder to understand at first glance. It's worth learning as an optimization of the two-pass approach.

The first solution with separate prefix and suffix arrays is a good starting point for understanding the problem, but it uses extra space and doesn't meet the follow-up challenge of O(1) extra space.

When approaching this problem in an interview setting, start by explaining the intuition behind breaking the problem into prefix and suffix products. Then, if time allows, optimize the solution to use less space. This demonstrates both problem-solving skills and optimization abilities.

## Visualization(s)

To visualize the "Two-pass approach with a single output array" (Solution 2), let's create a simple diagram using ASCII art:

```
Input array: [1, 2, 3, 4]

First Pass (Prefix Products):
[1] -> [1, 1, 1, 1]
[1, 2] -> [1, 1, 2, 1]
[1, 2, 3] -> [1, 1, 2, 6]
[1, 2, 3, 4] -> [1, 1, 2, 6]

Second Pass (Suffix Products and Final Result):
[1, 2, 3, 4] <- [24]
[1, 2, 3, 4] <- [12, 24]
[1, 2, 3, 4] <- [8, 12, 24]
[1, 2, 3, 4] <- [6, 8, 12, 24]

Final Output: [24, 12, 8, 6]
```

This visualization shows how the output array is built up in two passes. In the first pass, we calculate the prefix products, and in the second pass, we incorporate the suffix products to get the final result.
