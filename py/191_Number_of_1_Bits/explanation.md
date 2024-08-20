## Explanation: Number of 1 Bits

### Analysis of problem & input data

This problem, also known as the "Hamming Weight" problem, is a classic bit manipulation question. The key characteristics to note are:

1. The input is a positive integer, which we need to treat as its binary representation.
2. We need to count the number of set bits (1s) in this binary representation.
3. The input range is from 1 to 2^31 - 1, which means we're dealing with 32-bit integers.

The principle that makes this question simple is the bitwise AND operation. When you AND a number with 1, it isolates the least significant bit. This allows us to check each bit of the number systematically.

Another key insight is that we can use bit shifting to move through the bits of the number efficiently. Right-shifting by 1 is equivalent to dividing by 2 in binary.

Lastly, there's a clever trick in bit manipulation where `n & (n-1)` always turns off the rightmost set bit. This leads to a very efficient solution.

### Test cases

1. Edge cases:

   - n = 1 (binary: 1)
   - n = 0 (binary: 0) - although not in the given range, it's a good edge case to consider
   - n = 2^31 - 1 (binary: 11111111111111111111111111111111)

2. Normal cases:

   - n = 11 (binary: 1011)
   - n = 128 (binary: 10000000)

3. Challenging inputs:
   - n = 2147483645 (binary: 1111111111111111111111111111101)

Here's the Python code for these test cases:

```python
def test_hamming_weight(func):
    test_cases = [
        (1, 1),
        (0, 0),
        (2**31 - 1, 31),
        (11, 3),
        (128, 1),
        (2147483645, 30)
    ]
    for n, expected in test_cases:
        result = func(n)
        print(f"Input: {n}, Expected: {expected}, Got: {result}, {'Pass' if result == expected else 'Fail'}")

# You would call this function with your implementation, e.g.:
# test_hamming_weight(hamming_weight)
```

### Solutions

#### Overview of solution approaches

##### Solutions worth learning

1. Bit Manipulation (AND with 1 and right shift)
2. Brian Kernighan's Algorithm
3. Lookup Table / Divide and Conquer

Count: 3 solutions

##### Rejected solutions

1. Converting to string and counting '1's
2. Recursion (not optimal for large numbers)

#### Worthy Solutions

##### Bit Manipulation (AND with 1 and right shift)

```python
def hamming_weight(n: int) -> int:
    count = 0
    while n:
        count += n & 1  # Check the least significant bit
        n >>= 1  # Right shift by 1 (equivalent to n //= 2)
    return count
```

- Time Complexity: O(1) - We always iterate 32 times for a 32-bit integer
- Space Complexity: O(1) - We only use a single variable for counting

- Intuitions and invariants:
  - `n & 1` isolates the least significant bit
  - Right shifting by 1 moves us to the next bit
  - The loop continues until all bits have been checked (n becomes 0)

##### Brian Kernighan's Algorithm

```python
def hamming_weight(n: int) -> int:
    count = 0
    while n:
        n &= (n - 1)  # Turn off the rightmost set bit
        count += 1
    return count
```

- Time Complexity: O(1) - In the worst case, we iterate the number of set bits times (max 32 for a 32-bit integer)
- Space Complexity: O(1) - We only use a single variable for counting

- Intuitions and invariants:
  - `n & (n - 1)` always turns off the rightmost set bit
  - The loop continues until all set bits have been turned off (n becomes 0)
  - The number of iterations equals the number of set bits

##### Lookup Table / Divide and Conquer

```python
def hamming_weight(n: int) -> int:
    # Precomputed lookup table for 8-bit integers
    bit_count = [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4] * 16

    count = 0
    while n:
        count += bit_count[n & 0xf]  # Count bits in the lowest 4 bits
        n >>= 4  # Move to the next 4 bits
    return count
```

- Time Complexity: O(1) - We always perform 8 iterations for a 32-bit integer
- Space Complexity: O(1) - We use a fixed-size lookup table

- Intuitions and invariants:
  - We can precompute the bit counts for all 8-bit integers (0-255)
  - We can process the 32-bit integer in 4-bit chunks
  - The total count is the sum of counts for each 4-bit chunk

#### Rejected Approaches

1. Converting to string and counting '1's:

   ```python
   def hamming_weight(n: int) -> int:
       return bin(n).count('1')
   ```

   This approach works but is not optimal for large numbers and doesn't demonstrate understanding of bit manipulation.

2. Recursion:

   ```python
   def hamming_weight(n: int) -> int:
       if n == 0:
           return 0
       return (n & 1) + hamming_weight(n >> 1)
   ```

   This approach works but can lead to stack overflow for large numbers and is less efficient than iterative solutions.

#### Final Recommendations

For a technical coding interview, I recommend learning and using Brian Kernighan's Algorithm. It's efficient, demonstrates a deep understanding of bit manipulation, and is elegant in its simplicity. The Bit Manipulation approach with AND and right shift is also good to know as it's straightforward and easy to explain. The Lookup Table approach, while efficient, might be overkill for this problem and takes more time to implement in an interview setting.

### Visualization(s)

To visualize Brian Kernighan's Algorithm, let's use a simple React component:

```tsx
import React, { useState, useEffect } from "react";

const BrianKernighanVisualization = () => {
  const [number, setNumber] = useState(11);
  const [binaryString, setBinaryString] = useState("");
  const [count, setCount] = useState(0);
  const [step, setStep] = useState(0);

  useEffect(() => {
    setBinaryString(number.toString(2).padStart(8, "0"));
    setCount(0);
    setStep(0);
  }, [number]);

  const nextStep = () => {
    if (number === 0) return;

    const newNumber = number & (number - 1);
    setNumber(newNumber);
    setBinaryString(newNumber.toString(2).padStart(8, "0"));
    setCount(count + 1);
    setStep(step + 1);
  };

  return (
    <div className="p-4 max-w-md mx-auto bg-white rounded-xl shadow-md overflow-hidden md:max-w-2xl">
      <h2 className="text-xl font-bold mb-4">Brian Kernighan's Algorithm</h2>
      <div className="mb-4">
        <label
          className="block text-gray-700 text-sm font-bold mb-2"
          htmlFor="number-input"
        >
          Enter a number (0-255):
        </label>
        <input
          id="number-input"
          type="number"
          min="0"
          max="255"
          value={number}
          onChange={(e) => setNumber(parseInt(e.target.value) || 0)}
          className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
        />
      </div>
      <div className="mb-4">
        <p className="text-lg font-semibold">Binary: {binaryString}</p>
        <p className="text-lg font-semibold">Count: {count}</p>
        <p className="text-lg font-semibold">Step: {step}</p>
      </div>
      <button
        onClick={nextStep}
        disabled={number === 0}
        className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
      >
        Next Step
      </button>
    </div>
  );
};

export default BrianKernighanVisualization;
```

This visualization allows you to input a number and step through Brian Kernighan's Algorithm, showing how the binary representation changes and how the count of set bits increases with each step.
