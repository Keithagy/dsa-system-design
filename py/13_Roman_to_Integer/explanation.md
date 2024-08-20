## Explanation: Roman to Integer

### Analysis of problem & input data

This problem involves converting Roman numerals to their integer equivalents. The key characteristics of the input data are:

1. The input is a string of Roman numeral symbols.
2. The string length is between 1 and 15 characters.
3. Only valid Roman numeral symbols are used (I, V, X, L, C, D, M).
4. The input is guaranteed to be a valid Roman numeral in the range [1, 3999].

The crucial insight for this problem is understanding the left-to-right reading order of Roman numerals and the special cases of subtraction. Roman numerals are typically written in descending order of value from left to right, except for the six subtraction cases mentioned in the problem description.

The key principle that makes this question simple is the left-to-right processing of the input string, with a look-ahead mechanism to handle subtraction cases. This approach allows for a single pass through the input, making it an efficient O(n) time complexity solution.

### Test cases

Here are some relevant test cases, including edge cases and challenging inputs:

1. Single symbol: "I" (should return 1)
2. Multiple symbols in descending order: "VII" (should return 7)
3. Subtraction case: "IV" (should return 4)
4. Multiple subtraction cases: "MCMXCIV" (should return 1994)
5. Largest possible input: "MMMCMXCIX" (should return 3999)
6. Smallest possible input: "I" (should return 1)
7. Repeated symbols: "XXXIX" (should return 39)

Here's the executable Python code for these test cases:

```python
def roman_to_int(s: str) -> int:
    # Implementation will be provided in the solution section
    pass

# Test cases
test_cases = [
    "I",
    "VII",
    "IV",
    "MCMXCIV",
    "MMMCMXCIX",
    "I",
    "XXXIX"
]

expected_outputs = [1, 7, 4, 1994, 3999, 1, 39]

for i, (test, expected) in enumerate(zip(test_cases, expected_outputs), 1):
    result = roman_to_int(test)
    print(f"Test case {i}: {'Passed' if result == expected else 'Failed'}")
    print(f"Input: {test}")
    print(f"Output: {result}")
    print(f"Expected: {expected}\n")
```

### Solutions

#### Overview of solution approaches

##### Solutions worth learning

1. Hash map with single pass and look-ahead
2. Hash map with single pass and value comparison
3. String replacement with predefined order

Count: 3 solutions

##### Rejected solutions

1. Recursive approach
2. Multiple pass solutions

#### Worthy Solutions

##### Hash map with single pass and look-ahead

```python
def roman_to_int(s: str) -> int:
    roman_values = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    total = 0
    n = len(s)

    for i in range(n):
        # If current value is less than next value, it's a subtraction case
        if i < n - 1 and roman_values[s[i]] < roman_values[s[i + 1]]:
            total -= roman_values[s[i]]
        else:
            total += roman_values[s[i]]

    return total
```

Runtime complexity: O(n), where n is the length of the input string
Memory usage: O(1), as we use a fixed-size hash map

Intuitions and invariants:

- We use a hash map to store the values of individual Roman symbols for quick lookup.
- We iterate through the string once, looking ahead to the next character when possible.
- If the current symbol's value is less than the next symbol's value, it's a subtraction case.
- The total is updated by either adding or subtracting the current symbol's value.
- This approach leverages the left-to-right reading order of Roman numerals and handles subtraction cases efficiently.

##### Hash map with single pass and value comparison

```python
def roman_to_int(s: str) -> int:
    roman_values = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    total = 0
    prev_value = 0

    # Iterate through the string in reverse order
    for symbol in reversed(s):
        current_value = roman_values[symbol]
        # If the current value is less than or equal to the previous value, add it
        # Otherwise, subtract it (handling subtraction cases)
        if current_value >= prev_value:
            total += current_value
        else:
            total -= current_value
        prev_value = current_value

    return total
```

Runtime complexity: O(n), where n is the length of the input string
Memory usage: O(1), as we use a fixed-size hash map

Intuitions and invariants:

- We use a hash map to store the values of individual Roman symbols for quick lookup.
- We iterate through the string in reverse order, comparing each value with the previous one.
- If the current value is less than the previous value, it's a subtraction case.
- This approach eliminates the need for look-ahead and simplifies the logic.
- It leverages the fact that in Roman numerals, a smaller value before a larger value indicates subtraction.

##### String replacement with predefined order

```python
def roman_to_int(s: str) -> int:
    # Define replacements in descending order of value
    replacements = [
        ("IV", "IIII"), ("IX", "VIIII"),
        ("XL", "XXXX"), ("XC", "LXXXX"),
        ("CD", "CCCC"), ("CM", "DCCCC")
    ]

    # Replace subtraction cases with addition equivalents
    for old, new in replacements:
        s = s.replace(old, new)

    # Sum up the values of individual symbols
    return sum(s.count(symbol) * value for symbol, value in [
        ('M', 1000), ('D', 500), ('C', 100), ('L', 50),
        ('X', 10), ('V', 5), ('I', 1)
    ])
```

Runtime complexity: O(1), as the input size is limited to 15 characters
Memory usage: O(1), as we use fixed-size lists and the input size is limited

Intuitions and invariants:

- We first replace all subtraction cases with their addition equivalents.
- This transformation allows us to simply count the occurrences of each symbol and multiply by its value.
- The replacements are done in descending order of value to avoid conflicts.
- This approach leverages the fact that there are only six subtraction cases in Roman numerals.
- After replacement, we can treat each symbol independently, simplifying the counting process.

#### Rejected Approaches

1. Recursive approach: While a recursive solution could work, it would be less efficient and more complex than the iterative solutions presented. It might also lead to stack overflow for very long inputs.

2. Multiple pass solutions: These would involve separate passes for identifying subtraction cases and summing up values. While correct, they are less efficient than single-pass solutions and not worth learning for interview preparation.

#### Final Recommendations

The hash map with single pass and look-ahead approach is recommended as the best solution to learn. It offers a good balance of efficiency, readability, and demonstration of understanding of the problem. This approach directly tackles the core challenge of the problem - handling subtraction cases while processing the input from left to right.

The other two solutions, while valid, have some drawbacks:

- The reverse iteration method, while clever, might be less intuitive to explain in an interview setting.
- The string replacement method, although interesting, relies more on string manipulation than on direct numeral processing, which might not demonstrate as deep an understanding of the problem.

### Visualization(s)

For this problem, a simple visualization can help understand the process of converting Roman numerals to integers, especially for cases involving subtraction. Here's a React component that demonstrates the conversion process:

```tsx
import React, { useState } from "react";

const RomanNumeralConverter = () => {
  const [romanInput, setRomanInput] = useState("");
  const [conversionSteps, setConversionSteps] = useState([]);

  const romanValues = {
    I: 1,
    V: 5,
    X: 10,
    L: 50,
    C: 100,
    D: 500,
    M: 1000,
  };

  const convertRomanToInt = (s) => {
    let total = 0;
    let steps = [];

    for (let i = 0; i < s.length; i++) {
      let currentValue = romanValues[s[i]];
      let nextValue = i < s.length - 1 ? romanValues[s[i + 1]] : 0;

      if (currentValue < nextValue) {
        total -= currentValue;
        steps.push(
          `${s[i]} (${currentValue}) is less than ${s[i + 1]} (${nextValue}), so subtract ${currentValue}`,
        );
      } else {
        total += currentValue;
        steps.push(`Add ${s[i]} (${currentValue})`);
      }

      steps.push(`Current total: ${total}`);
    }

    setConversionSteps(steps);
    return total;
  };

  const handleInputChange = (e) => {
    setRomanInput(e.target.value.toUpperCase());
  };

  const handleConvert = () => {
    convertRomanToInt(romanInput);
  };

  return (
    <div className="p-4 max-w-md mx-auto bg-white rounded-xl shadow-md overflow-hidden md:max-w-2xl">
      <h2 className="text-2xl font-bold mb-4">Roman Numeral Converter</h2>
      <input
        type="text"
        value={romanInput}
        onChange={handleInputChange}
        placeholder="Enter Roman numeral"
        className="w-full p-2 mb-4 border rounded"
      />
      <button
        onClick={handleConvert}
        className="w-full bg-blue-500 text-white p-2 rounded hover:bg-blue-600"
      >
        Convert
      </button>
      <div className="mt-4">
        <h3 className="text-xl font-semibold mb-2">Conversion Steps:</h3>
        <ul className="list-disc pl-5">
          {conversionSteps.map((step, index) => (
            <li key={index} className="mb-1">
              {step}
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
};

export default RomanNumeralConverter;
```

This component provides an interactive way to visualize the conversion process. Users can input a Roman numeral, and the component will display the step-by-step process of converting it to an integer, highlighting the subtraction cases.
