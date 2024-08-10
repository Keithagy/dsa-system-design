# Explanation: Reverse Bits

## Analysis of problem & input data

This problem presents several key characteristics that are crucial for understanding and solving it effectively:

1. Fixed input size: The input is always a 32-bit unsigned integer. This constant size is a critical piece of information that allows us to design a solution with a fixed number of operations.

2. Bit manipulation: The core of this problem involves manipulating individual bits, which suggests that bitwise operations will be central to the solution.

3. Reversal operation: We need to reverse the order of bits, which implies that we'll need to consider both the least significant bit (LSB) and the most significant bit (MSB) of the input.

4. Unsigned integer representation: While the problem mentions unsigned integers, it notes that the internal binary representation is the same for signed and unsigned integers. This allows us to focus on the bits themselves without worrying about sign representation.

5. Potential for optimization: The follow-up question about optimization for multiple calls suggests that we should consider solutions that can be precomputed or cached for efficiency.

The key principle that makes this question relatively straightforward is that bitwise operations can be used to isolate, manipulate, and reconstruct individual bits efficiently. By leveraging bitwise AND, OR, and shift operations, we can extract each bit from the input and place it in its reversed position in the output.

## Solutions

### Solution 1: Bit-by-bit reversal

This solution iterates through each bit of the input number, extracting the least significant bit and adding it to the result in the appropriate reversed position.

```python
class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for i in range(32):
            # Extract the least significant bit of n
            bit = n & 1
            # Left shift the result to make room for the new bit
            result <<= 1
            # Add the extracted bit to the result
            result |= bit
            # Right shift n to process the next bit
            n >>= 1
        return result
```

Time Complexity: O(1) - We always perform exactly 32 iterations.
Space Complexity: O(1) - We use only a constant amount of extra space.

Intuitions and invariants:

- The loop invariant is that after i iterations, the i least significant bits of the input have been reversed and placed in the i most significant bits of the result.
- We leverage the fact that bitwise AND with 1 isolates the least significant bit.
- Left shifting the result by 1 in each iteration ensures that we're always adding the new bit to the least significant position of the reversed result.

### Solution 2: Byte-by-byte reversal with lookup table

This solution improves performance by reversing bytes instead of individual bits, using a precomputed lookup table.

```python
class Solution:
    def __init__(self):
        self.lookup_table = [0] * 256
        for i in range(256):
            self.lookup_table[i] = int(f"{i:08b}"[::-1], 2)

    def reverseBits(self, n: int) -> int:
        result = 0
        for _ in range(4):  # 4 bytes in a 32-bit integer
            result = (result << 8) | self.lookup_table[n & 0xff]
            n >>= 8
        return result
```

Time Complexity: O(1) - We perform a fixed number of operations.
Space Complexity: O(1) - The lookup table has a fixed size of 256 entries.

Intuitions and invariants:

- Precomputing reversed bytes allows us to process 8 bits at a time instead of 1.
- The lookup table maps each possible byte value to its bit-reversed equivalent.
- We process the input number byte by byte, using the lookup table to reverse each byte efficiently.

## Recommendation

I recommend learning and implementing Solution 1 (Bit-by-bit reversal) for several reasons:

1. It clearly demonstrates the core concept of bit manipulation, which is fundamental to many other problems.
2. It's straightforward to understand and implement, making it a good choice for interviews where clarity and correctness are crucial.
3. It doesn't rely on additional memory (like the lookup table in Solution 2), which can be advantageous in memory-constrained environments.

However, for production environments where the function is called frequently, Solution 2 (Byte-by-byte reversal with lookup table) would be more efficient due to its reduced number of iterations and use of precomputed values.

## Test cases

Here are some test cases to verify the correctness of the implementation:

```python
def test_reverse_bits():
    solution = Solution()

    assert solution.reverseBits(43261596) == 964176192  # Example 1
    assert solution.reverseBits(4294967293) == 3221225471  # Example 2
    assert solution.reverseBits(0) == 0  # All zeros
    assert solution.reverseBits(4294967295) == 4294967295  # All ones
    assert solution.reverseBits(1) == 2147483648  # Single 1 at LSB
    assert solution.reverseBits(2147483648) == 1  # Single 1 at MSB

    print("All test cases passed!")

test_reverse_bits()
```

## Overview of rejected approaches

1. String manipulation: Converting the integer to a binary string, reversing it, and converting back to an integer. While this approach works, it's inefficient in terms of both time and space complexity due to string operations. It also doesn't leverage the bitwise operations that make the problem elegant.

2. Recursive solution: While it's possible to design a recursive solution that reverses bits, it would be unnecessarily complex and potentially lead to stack overflow for 32-bit integers. The iterative solutions are more straightforward and efficient.

3. Using built-in reverse functions: Some languages have built-in functions to reverse bits (e.g., Python's `int.bit_length()` and `int.to_bytes()`). While these can solve the problem, they don't demonstrate understanding of bit manipulation and might not be available in all languages or interview settings.

## Visualization(s)

To visualize the bit-by-bit reversal process, we can create a simple React component that shows how the bits are reversed step by step. Here's a component that demonstrates this:

```tsx
import React, { useState, useEffect } from "react";

const BitReversalVisualization = () => {
  const [input, setInput] = useState(43261596);
  const [step, setStep] = useState(0);
  const [result, setResult] = useState(0);

  useEffect(() => {
    if (step < 32) {
      const timer = setTimeout(() => {
        setResult((prevResult) => {
          const bit = input & (1 << step);
          return (prevResult << 1) | (bit ? 1 : 0);
        });
        setStep((prevStep) => prevStep + 1);
      }, 500);
      return () => clearTimeout(timer);
    }
  }, [step, input]);

  const restart = () => {
    setStep(0);
    setResult(0);
  };

  return (
    <div className="p-4 max-w-lg mx-auto">
      <h2 className="text-2xl font-bold mb-4">Bit Reversal Visualization</h2>
      <div className="mb-4">
        <label className="block mb-2">Input number:</label>
        <input
          type="number"
          value={input}
          onChange={(e) => {
            setInput(Number(e.target.value));
            restart();
          }}
          className="w-full p-2 border rounded"
        />
      </div>
      <div className="mb-4">
        <p>Original: {input.toString(2).padStart(32, "0")}</p>
        <p>Reversed: {result.toString(2).padStart(32, "0")}</p>
      </div>
      <div className="mb-4">
        <progress value={step} max="32" className="w-full" />
      </div>
      <button
        onClick={restart}
        className="bg-blue-500 text-white px-4 py-2 rounded"
      >
        Restart
      </button>
    </div>
  );
};

export default BitReversalVisualization;
```

This visualization shows the step-by-step process of reversing the bits of a 32-bit integer. You can input any number and watch as each bit is reversed one at a time. The progress bar indicates how many bits have been processed.
