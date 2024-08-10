# Explanation: Longest Substring Without Repeating Characters

## Analysis of problem & input data

This problem is a classic example of the sliding window technique, which is particularly useful for substring problems. Here are the key aspects to consider:

1. We're dealing with a string input, which can contain letters, digits, symbols, and spaces.
2. We need to find a substring, not a subsequence. This means the characters must be contiguous.
3. The substring we're looking for must not have any repeating characters.
4. We need to find the longest such substring and return its length.
5. The constraint on the input string length (0 to 5 \* 10^4) suggests that a solution with O(n) time complexity would be ideal.
6. The fact that we're dealing with a wide range of possible characters (not just lowercase letters, for example) impacts how we might choose to keep track of character occurrences.

The key principle that makes this question approachable is that we can build our solution incrementally. As we scan through the string, we can keep track of the last seen position of each character. This allows us to quickly determine if a character repeats and where the new substring should start.

## Solutions

Solution approaches include:

1. Sliding Window with Hash Map
2. Sliding Window with Array (for ASCII characters only)
3. Brute Force
   (3 in total)

### 1. Sliding Window with Hash Map

```python
from typing import Dict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index: Dict[str, int] = {}  # Keep track of the index of each character
        start = 0  # Start of the current substring
        max_length = 0  # Length of the longest substring found

        for end, char in enumerate(s):
            # If we've seen this character before and it's in the current substring
            if char in char_index and char_index[char] >= start:
                # Move the start to the right of the last occurrence of this character
                start = char_index[char] + 1
            else:
                # Update max_length if the current substring is longer
                max_length = max(max_length, end - start + 1)

            # Update the last seen position of this character
            char_index[char] = end

        return max_length
```

Time Complexity: O(n), where n is the length of the string. We iterate through the string once.
Space Complexity: O(min(m, n)), where m is the size of the character set. In the worst case, we might need to store all characters in the hash map.

Intuitions and invariants:

- We use a sliding window approach, where the window represents the current substring without repeating characters.
- The hash map stores the most recent index of each character we've seen.
- When we encounter a repeating character, we move the start of our window to the right of the last occurrence of this character.
- At each step, we update our max_length if the current window is longer.
- This approach ensures we're always considering the longest possible substring ending at the current character.

### 2. Sliding Window with Array (for ASCII characters only)

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = [-1] * 128  # Assuming ASCII characters
        start = 0
        max_length = 0

        for end, char in enumerate(s):
            # If we've seen this character before and it's in the current substring
            if char_index[ord(char)] >= start:
                start = char_index[ord(char)] + 1
            else:
                max_length = max(max_length, end - start + 1)

            # Update the last seen position of this character
            char_index[ord(char)] = end

        return max_length
```

Time Complexity: O(n), where n is the length of the string.
Space Complexity: O(1), as we're using a fixed-size array of 128 elements.

Intuitions and invariants:

- This approach is similar to the hash map solution, but uses an array instead.
- It's more space-efficient if we know we're only dealing with ASCII characters.
- The array indices correspond to ASCII values, and the values stored are the last seen indices of each character.
- This approach trades some flexibility (only works for ASCII) for improved space efficiency.

### 3. Brute Force

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        def allUnique(start: int, end: int) -> bool:
            char_set = set()
            for i in range(start, end + 1):
                if s[i] in char_set:
                    return False
                char_set.add(s[i])
            return True

        n = len(s)
        max_length = 0

        for i in range(n):
            for j in range(i, n):
                if allUnique(i, j):
                    max_length = max(max_length, j - i + 1)

        return max_length
```

Time Complexity: O(n^3). For each of the n(n+1)/2 substrings, we check if it has unique characters, which takes O(n) time.
Space Complexity: O(min(n, m)), where m is the size of the character set. We need a set to check for uniqueness.

Intuitions and invariants:

- This approach checks all possible substrings.
- For each substring, we verify if it contains all unique characters.
- We keep track of the longest valid substring we've found.
- While simple to understand, this approach is inefficient for large inputs.

## Recommendation

The Sliding Window with Hash Map approach is the best solution to learn for this problem. It offers the optimal balance of time and space efficiency, and it's a versatile technique that can be applied to many similar substring problems. Here's why:

1. Time Efficiency: It solves the problem in O(n) time, which is optimal for this problem.
2. Space Efficiency: While it uses O(min(m, n)) space, this is often acceptable in practice and necessary to achieve the O(n) time complexity.
3. Flexibility: It works for any character set, not just ASCII.
4. Technique: The sliding window technique used here is a fundamental algorithmic pattern that's useful in many string and array problems.

The Array-based approach is a good optimization to know if you're certain you're only dealing with ASCII characters, but it's less flexible.

The Brute Force approach, while intuitive, is not efficient enough for larger inputs and wouldn't be acceptable in most interview settings.

## Test cases

Here are some test cases to verify the implementation:

1. Normal case: "abcabcbb" -> 3
2. All repeating characters: "bbbbb" -> 1
3. Repeats with unique substring in middle: "pwwkew" -> 3
4. Empty string: "" -> 0
5. Single character: "a" -> 1
6. No repeating characters: "abcdef" -> 6
7. Repeats at the end: "abcda" -> 4
8. Complex case with symbols and spaces: "ab c@b#c$ab" -> 6

## Overview of rejected approaches

1. Using a Set: One might be tempted to use a set to keep track of unique characters and grow/shrink it as we move through the string. While this would work, it's less efficient than the hash map approach because we'd need to remove characters from the set as we shrink our window, which is an O(k) operation where k is the number of characters to remove.

2. Dynamic Programming: This problem might seem like a candidate for dynamic programming, but it's actually not well-suited for it. The optimal substructure property doesn't hold here because knowing the longest substring without repeating characters ending at position i-1 doesn't directly help us find the longest substring ending at position i.

3. Sorting: Sorting the string or using any sort-based approach wouldn't be helpful here, as we need to maintain the original order of characters in the substring.

4. Two Pointers without Hash Map: While we do use two pointers (start and end) in our optimal solution, trying to solve this problem with just two pointers and without any additional data structure to keep track of character positions would result in a less efficient solution.

## Visualization(s)

To visualize the sliding window approach, let's consider the string "abcabcbb":

```tsx
import React, { useState, useEffect } from "react";
import { motion } from "framer-motion";

const SlidingWindowVisualization = () => {
  const [step, setStep] = useState(0);
  const string = "abcabcbb";
  const steps = [
    { start: 0, end: 0, maxLength: 1 },
    { start: 0, end: 1, maxLength: 2 },
    { start: 0, end: 2, maxLength: 3 },
    { start: 0, end: 3, maxLength: 3 },
    { start: 1, end: 4, maxLength: 3 },
    { start: 2, end: 5, maxLength: 3 },
    { start: 3, end: 6, maxLength: 3 },
    { start: 5, end: 7, maxLength: 3 },
  ];

  useEffect(() => {
    const timer = setInterval(() => {
      setStep((prevStep) => (prevStep + 1) % steps.length);
    }, 1500);
    return () => clearInterval(timer);
  }, []);

  return (
    <div className="p-4">
      <div className="flex justify-center space-x-2 mb-4">
        {string.split("").map((char, index) => (
          <motion.div
            key={index}
            className={`w-8 h-8 flex items-center justify-center border ${
              index >= steps[step].start && index <= steps[step].end
                ? "bg-blue-200"
                : "bg-gray-100"
            }`}
            animate={{ scale: index === steps[step].end ? 1.1 : 1 }}
          >
            {char}
          </motion.div>
        ))}
      </div>
      <div className="text-center">Max Length: {steps[step].maxLength}</div>
    </div>
  );
};

export default SlidingWindowVisualization;
```

This visualization shows how the sliding window moves through the string. The blue highlighted area represents the current window (substring without repeating characters). The window expands when it encounters a new character and contracts when it encounters a repeat. The max length updates as we find longer substrings.
