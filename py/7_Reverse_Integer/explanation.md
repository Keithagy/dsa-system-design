## Explanation: Reverse Integer

### Analysis of problem & input data

This problem involves reversing the digits of a given integer while handling several key aspects:

1. Sign preservation: The sign of the number should be maintained in the reversed result.
2. 32-bit integer range: The solution must handle potential overflow, returning 0 if the reversed number exceeds the 32-bit integer range.
3. Trailing zeros: Any trailing zeros in the original number should be omitted in the reversed result.
4. No 64-bit integer storage: We cannot use 64-bit integers to store intermediate results.

The key principle that makes this question simple is the use of modulo and integer division operations to extract digits from right to left, which naturally reverses the number. The challenge lies in handling the edge cases and constraints effectively.

### Test cases

1. Positive number: 123 → 321
2. Negative number: -123 → -321
3. Number with trailing zeros: 120 → 21
4. Zero: 0 → 0
5. Maximum 32-bit integer: 2147483647 → 0 (overflow)
6. Minimum 32-bit integer: -2147483648 → 0 (overflow)
7. Number that causes overflow when reversed: 1534236469 → 0

Here's the executable Python code for these test cases:

```python
def reverse_integer(x: int) -> int:
    # Implementation goes here
    pass

# Test cases
test_cases = [
    123,
    -123,
    120,
    0,
    2147483647,
    -2147483648,
    1534236469
]

for case in test_cases:
    result = reverse_integer(case)
    print(f"Input: {case}, Output: {result}")
```

### Solutions

#### Overview of solution approaches

##### Solutions worth learning

1. Digit extraction and reconstruction (Neetcode solution)
2. String conversion and reversal
3. Recursive approach

Count: 3 solutions (1 Neetcode solution)

##### Rejected solutions

1. Using 64-bit integers: This violates the problem constraint.
2. Converting to string and using built-in reverse function: While easy to implement, it doesn't demonstrate understanding of the underlying numerical operations.

#### Worthy Solutions

##### Digit extraction and reconstruction (Neetcode solution)

```python
def reverse(x: int) -> int:
    # Store the sign of the input number
    sign = 1 if x > 0 else -1
    x = abs(x)

    reversed_num = 0
    while x != 0:
        # Extract the rightmost digit
        digit = x % 10

        # Check for potential overflow before adding the new digit
        if (reversed_num > 214748364) or (reversed_num == 214748364 and digit > 7):
            return 0
        if (reversed_num < -214748364) or (reversed_num == -214748364 and digit > 8):
            return 0

        # Add the digit to the reversed number
        reversed_num = reversed_num * 10 + digit

        # Remove the rightmost digit from x
        x //= 10

    # Apply the original sign to the reversed number
    return sign * reversed_num
```

Runtime complexity: O(log x), where x is the input integer. This is because the number of digits in an integer is proportional to log10(x), and we process each digit once.

Memory usage: O(1), as we only use a constant amount of extra space regardless of the input size.

Intuitions and invariants:

- The modulo operation (%) extracts the rightmost digit of a number.
- Integer division (//) removes the rightmost digit of a number.
- Multiplying by 10 and adding a digit effectively appends that digit to the right of a number.
- Checking for overflow before adding each digit prevents the need for 64-bit storage.

##### String conversion and reversal

```python
def reverse(x: int) -> int:
    # Convert to string, preserving the sign
    s = str(abs(x))

    # Reverse the string
    reversed_s = s[::-1]

    # Convert back to integer, restoring the sign
    result = int(reversed_s) * (-1 if x < 0 else 1)

    # Check for 32-bit integer overflow
    if result > 2**31 - 1 or result < -2**31:
        return 0

    return result
```

Runtime complexity: O(n), where n is the number of digits in x. This is because string slicing and integer conversion both take linear time.

Memory usage: O(n), as we create a new string of length n.

Intuitions and invariants:

- Strings can be easily reversed using slicing in Python.
- Converting to and from strings preserves the magnitude of the number.
- The sign needs to be handled separately when using string conversion.

##### Recursive approach

```python
def reverse(x: int) -> int:
    def reverse_recursive(n: int, reversed_num: int) -> int:
        if n == 0:
            return reversed_num

        digit = n % 10
        new_reversed = reversed_num * 10 + digit

        # Check for overflow
        if new_reversed > 2**31 - 1 or new_reversed < -2**31:
            return 0

        return reverse_recursive(n // 10, new_reversed)

    return reverse_recursive(abs(x), 0) * (-1 if x < 0 else 1)
```

Runtime complexity: O(log x), where x is the input integer, as we process each digit recursively.

Memory usage: O(log x) due to the recursive call stack.

Intuitions and invariants:

- Each recursive call processes one digit of the input number.
- The reversed number is built up in the `reversed_num` parameter.
- Base case is when the input number becomes 0, indicating all digits have been processed.

#### Rejected Approaches

1. Using 64-bit integers: While this would simplify the overflow checking, it violates the problem constraint of not using 64-bit integers.

2. Converting to string and using built-in reverse function:
   ```python
   def reverse(x: int) -> int:
       result = int(str(abs(x))[::-1]) * (-1 if x < 0 else 1)
       return result if -2**31 <= result <= 2**31 - 1 else 0
   ```
   While this approach is concise, it relies heavily on Python's built-in functions and doesn't demonstrate understanding of the underlying numerical operations. In a technical interview, it's generally better to show your ability to work with the numbers directly.

#### Final Recommendations

The digit extraction and reconstruction method (Neetcode solution) is the best to learn for this problem. It directly addresses all the requirements:

1. It handles the sign correctly.
2. It checks for overflow at each step, ensuring 32-bit integer compliance.
3. It naturally handles trailing zeros.
4. It doesn't rely on 64-bit integer storage.

Moreover, this solution demonstrates a good understanding of basic number theory and bitwise operations, which are valuable skills in coding interviews. It's also the most efficient in terms of both time and space complexity.

### Visualization(s)

For this problem, a step-by-step visualization of the digit extraction process might be helpful. Here's a simple ASCII representation for the number 123:

```
Step 1: 123 % 10 = 3, reversed = 3, x = 12
Step 2: 12 % 10 = 2, reversed = 32, x = 1
Step 3: 1 % 10 = 1, reversed = 321, x = 0
Result: 321
```

This visualization helps to understand how the algorithm extracts digits from right to left and reconstructs the reversed number.
