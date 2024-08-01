## Overview of python bitwise operators

Here's a concise primer on bitwise operators in Python:

```python
# Bitwise AND (&)
a = 5  # 101
b = 3  # 011
print(a & b)  # 001 (1 in decimal)

# Bitwise OR (|)
print(a | b)  # 111 (7 in decimal)

# Bitwise XOR (^)
print(a ^ b)  # 110 (6 in decimal)

# Bitwise NOT (~)
print(~a)  # -6 (2's complement: 11111010)

# Left Shift (<<)
print(a << 1)  # 1010 (10 in decimal)

# Right Shift (>>)
print(a >> 1)  # 10 (2 in decimal)

# Practical example: Check if a number is odd
def is_odd(n):
    return n & 1 == 1

print(is_odd(5))  # True
print(is_odd(6))  # False

# Practical example: Set/unset/check a specific bit
def set_bit(x, position):
    return x | (1 << position)

def clear_bit(x, position):
    return x & ~(1 << position)

def check_bit(x, position):
    return (x & (1 << position)) != 0

x = 5  # 101
print(bin(set_bit(x, 1)))    # 0b111 (7 in decimal)
print(bin(clear_bit(x, 2)))  # 0b001 (1 in decimal)
print(check_bit(x, 1))       # False
print(check_bit(x, 2))       # True

```

This primer covers the basic bitwise operators in Python and includes some practical examples. Would you like me to explain any part of it in more detail?

## Techniques

Certainly! Bitwise operations are indeed popular in coding interviews, especially for optimizing certain algorithms or solving specific types of problems. Here's a compilation of common bitwise tricks and techniques that could be useful in LeetCode interviews:

```python
# 1. Add 1 to a number
def add_one(n):
    return -~n

# 2. Subtract 1 from a number
def subtract_one(n):
    return ~-n

# 3. Multiply by 2
def multiply_by_2(n):
    return n << 1

# 4. Divide by 2
def divide_by_2(n):
    return n >> 1

# 5. Check if a number is even or odd
def is_even(n):
    return not (n & 1)

# 6. Check if a number is a power of 2
def is_power_of_2(n):
    return n and not (n & (n - 1))

# 7. Find the rightmost set bit
def rightmost_set_bit(n):
    return n & -n

# 8. Clear the rightmost set bit
def clear_rightmost_set_bit(n):
    return n & (n - 1)

# 9. Count the number of set bits (Brian Kernighan's Algorithm)
def count_set_bits(n):
    count = 0
    while n:
        n &= (n - 1)
        count += 1
    return count

# 10. Swap two numbers without using a temporary variable
def swap(a, b):
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return a, b

# 11. Find the missing number in an array of n integers (1 to n)
def find_missing(arr):
    n = len(arr) + 1
    xor_all = 0
    for i in range(1, n + 1):
        xor_all ^= i
    for num in arr:
        xor_all ^= num
    return xor_all

# 12. Get the absolute value of a number without branching
def abs_value(n):
    mask = n >> 31
    return (n + mask) ^ mask

# Usage examples
print(add_one(5))  # 6
print(subtract_one(5))  # 4
print(multiply_by_2(5))  # 10
print(divide_by_2(5))  # 2
print(is_even(5))  # False
print(is_power_of_2(8))  # True
print(bin(rightmost_set_bit(12)))  # 0b100
print(bin(clear_rightmost_set_bit(12)))  # 0b1000
print(count_set_bits(7))  # 3
print(swap(5, 10))  # (10, 5)
print(find_missing([1, 2, 4, 5]))  # 3
print(abs_value(-5))  # 5

```

Here's an explanation of some key techniques from this code:

1. Adding/Subtracting 1: These use the fact that -~n is equivalent to n + 1, and ~-n is equivalent to n - 1.

2. Multiply/Divide by 2: Left shift (<<) multiplies by 2, right shift (>>) divides by 2.

3. Checking even/odd: The least significant bit is 1 for odd numbers and 0 for even numbers.

4. Power of 2 check: Numbers that are powers of 2 have only one bit set, so n & (n-1) will be 0.

5. Rightmost set bit: n & -n isolates the rightmost set bit due to two's complement representation.

6. Counting set bits: Brian Kernighan's algorithm clears the rightmost set bit in each iteration.

7. XOR swap: This is a classic technique to swap numbers without a temporary variable.

8. Finding missing number: XOR all numbers from 1 to n with all numbers in the array. The result is the missing number.

9. Absolute value: This uses the sign bit to create a mask for flipping bits if the number is negative.

These bitwise operations are often used to optimize solutions, especially in problems involving:

- Bit manipulation
- Finding unique elements
- Detecting duplicates
- Space optimization (using bits to represent states)
- Certain mathematical operations

Would you like me to elaborate on any of these techniques or provide more examples?
