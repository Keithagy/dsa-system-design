## Explanation: Find All Anagrams in a String

### Analysis of problem & input data

This problem is a classic example of the sliding window technique combined with frequency counting. The key insights are:

1. Anagrams have the same frequency of characters, just in a different order.
2. We're looking for substrings of `s` that are the same length as `p`.
3. As we slide our window through `s`, we only need to update the frequencies of characters entering and leaving the window.

The problem's characteristics that enable pattern-matching to a sliding window solution are:

- We're searching for substrings (contiguous sequences) in a larger string.
- These substrings have a fixed length (the length of `p`).
- We need to consider all possible substrings of this length.

The key principle that makes this question simple is that anagrams are defined by character frequencies, not order. This allows us to use a frequency-based comparison instead of sorting or permutation generation.

### Test cases

1. Basic case:

   - `s = "cbaebabacd"`, `p = "abc"`
   - Expected output: `[0, 6]`

2. Overlapping anagrams:

   - `s = "abab"`, `p = "ab"`
   - Expected output: `[0, 1, 2]`

3. No anagrams:

   - `s = "hello"`, `p = "world"`
   - Expected output: `[]`

4. Single character anagram:

   - `s = "aaaaaaa"`, `p = "a"`
   - Expected output: `[0, 1, 2, 3, 4, 5, 6]`

5. Anagram is the entire string:

   - `s = "abc"`, `p = "abc"`
   - Expected output: `[0]`

6. Pattern longer than string:
   - `s = "ab"`, `p = "abc"`
   - Expected output: `[]`

Here's the Python code for these test cases:

```python
def find_anagrams(s: str, p: str) -> List[int]:
    # Implementation goes here
    pass

# Test cases
test_cases = [
    ("cbaebabacd", "abc"),
    ("abab", "ab"),
    ("hello", "world"),
    ("aaaaaaa", "a"),
    ("abc", "abc"),
    ("ab", "abc")
]

for s, p in test_cases:
    print(f"s = {s}, p = {p}")
    print(f"Output: {find_anagrams(s, p)}")
    print()
```

### Solutions

#### Overview of solution approaches

##### Solutions worth learning

1. Sliding Window with Character Frequency Count
2. Sliding Window with Array (for lowercase English letters only)
3. Sliding Window with Sorting (less efficient but conceptually simple)

Count: 3 solutions

##### Rejected solutions

1. Brute Force with Permutations: Generating all permutations of `p` and checking if each substring of `s` matches any permutation.
2. Naive Sliding Window with Sorting: Sorting each substring of `s` and comparing with sorted `p`.

#### Worthy Solutions

##### Sliding Window with Character Frequency Count

```python
from collections import Counter

def find_anagrams(s: str, p: str) -> List[int]:
    result = []
    p_freq = Counter(p)
    window_freq = Counter()

    for i in range(len(s)):
        # Add the incoming character to the window
        window_freq[s[i]] += 1

        # If the window size exceeds p's length, remove the outgoing character
        if i >= len(p):
            if window_freq[s[i - len(p)]] == 1:
                del window_freq[s[i - len(p)]]
            else:
                window_freq[s[i - len(p)]] -= 1

        # Check if the current window is an anagram of p
        if window_freq == p_freq:
            result.append(i - len(p) + 1)

    return result
```

Time Complexity: O(n), where n is the length of string s
Space Complexity: O(k), where k is the number of unique characters in p (at most 26 for lowercase English letters)

- This solution leverages the fact that anagrams have identical character frequencies.
- We use a sliding window to maintain the frequency count of characters in the current substring.
- The `Counter` class from Python's collections module efficiently handles frequency counting.
- By updating frequencies for characters entering and leaving the window, we avoid recounting the entire substring each time.
- The comparison `window_freq == p_freq` is O(1) on average for small alphabets like lowercase English letters.

##### Sliding Window with Array (for lowercase English letters only)

```python
def find_anagrams(s: str, p: str) -> List[int]:
    result = []
    p_freq = [0] * 26
    window_freq = [0] * 26

    # Initialize frequency arrays
    for char in p:
        p_freq[ord(char) - ord('a')] += 1

    for i in range(len(s)):
        # Add the incoming character to the window
        window_freq[ord(s[i]) - ord('a')] += 1

        # If the window size exceeds p's length, remove the outgoing character
        if i >= len(p):
            window_freq[ord(s[i - len(p)]) - ord('a')] -= 1

        # Check if the current window is an anagram of p
        if window_freq == p_freq:
            result.append(i - len(p) + 1)

    return result
```

Time Complexity: O(n), where n is the length of string s
Space Complexity: O(1), as we use fixed-size arrays of length 26

- This solution is similar to the previous one but uses fixed-size arrays instead of hash tables.
- It's more efficient in terms of space and potentially faster for small alphabets, but less flexible (only works for lowercase English letters).
- We use ASCII value manipulation to map characters to array indices.
- The comparison `window_freq == p_freq` is always O(26), which is effectively O(1).

##### Sliding Window with Sorting (less efficient but conceptually simple)

```python
def find_anagrams(s: str, p: str) -> List[int]:
    result = []
    p_sorted = sorted(p)

    for i in range(len(s) - len(p) + 1):
        if sorted(s[i:i+len(p)]) == p_sorted:
            result.append(i)

    return result
```

Time Complexity: O(n _ k _ log(k)), where n is the length of s and k is the length of p
Space Complexity: O(k) for sorting

- This solution sorts the substring of s and compares it with the sorted p.
- While less efficient, it's conceptually simpler and can be a good starting point for understanding the problem.
- The sorting approach naturally handles the frequency matching required for anagrams.
- This method becomes inefficient for large inputs due to repeated sorting.

#### Rejected Approaches

1. Brute Force with Permutations:

   - Generating all permutations of p and checking each substring of s against these permutations.
   - Rejected because it's extremely inefficient, with a time complexity of O(n \* k!), where k is the length of p.

2. Naive Sliding Window with Sorting:
   - Similar to the third accepted solution, but without reusing the sorted p.
   - Rejected because it unnecessarily sorts p multiple times, leading to worse performance.

#### Final Recommendations

The Sliding Window with Character Frequency Count is the best solution to learn. It offers:

1. Optimal time complexity (O(n))
2. Reasonable space complexity (O(k), where k ≤ 26 for lowercase English letters)
3. Flexibility to handle various character sets
4. A good balance between efficiency and readability
5. Demonstrates important concepts like sliding window and frequency counting

This solution showcases how to optimize string matching problems and is applicable to many similar questions, making it valuable for interviews and real-world scenarios.

### Visualization(s)

To visualize the sliding window approach, we can use a simple ASCII-based representation:

```
s = "c b a e b a b a c d"
p = "a b c"

Window 1: [c b a] e b a b a c d  -> Anagram found at index 0
Window 2:  c [b a e] b a b a c d
Window 3:  c b [a e b] a b a c d
Window 4:  c b a [e b a] b a c d
Window 5:  c b a e [b a b] a c d
Window 6:  c b a e b [a b a] c d  -> Anagram found at index 6
Window 7:  c b a e b a [b a c] d
Window 8:  c b a e b a b [a c d]
```

This visualization helps to understand how the window slides through the string s, checking each substring of length 3 (length of p) for an anagram match.

```tsx
import React, { useState, useEffect } from "react";
import { motion } from "framer-motion";

const SlidingWindow = () => {
  const [s, setS] = useState("cbaebabacd");
  const [p, setP] = useState("abc");
  const [windowStart, setWindowStart] = useState(0);
  const [foundAnagrams, setFoundAnagrams] = useState([]);

  useEffect(() => {
    const timer = setInterval(() => {
      setWindowStart((prev) => (prev + 1) % (s.length - p.length + 1));
    }, 1000);

    return () => clearInterval(timer);
  }, [s, p]);

  useEffect(() => {
    const isAnagram = (str1, str2) => {
      return str1.split("").sort().join("") === str2.split("").sort().join("");
    };

    if (isAnagram(s.slice(windowStart, windowStart + p.length), p)) {
      setFoundAnagrams((prev) => [...new Set([...prev, windowStart])]);
    }
  }, [windowStart, s, p]);

  return (
    <div className="p-4 bg-gray-100 rounded-lg">
      <div className="mb-4">
        <label className="mr-2">s:</label>
        <input
          value={s}
          onChange={(e) => setS(e.target.value)}
          className="border rounded px-2 py-1"
        />
      </div>
      <div className="mb-4">
        <label className="mr-2">p:</label>
        <input
          value={p}
          onChange={(e) => setP(e.target.value)}
          className="border rounded px-2 py-1"
        />
      </div>
      <div className="font-mono text-xl space-x-1">
        {s.split("").map((char, index) => (
          <motion.span
            key={index}
            className={`inline-block ${
              index >= windowStart && index < windowStart + p.length
                ? "bg-yellow-200"
                : ""
            } ${foundAnagrams.includes(index) ? "text-green-600 font-bold" : ""}`}
            animate={{ y: [0, -5, 0] }}
            transition={{
              duration: 0.5,
              repeat: Infinity,
              repeatType: "reverse",
            }}
          >
            {char}
          </motion.span>
        ))}
      </div>
      <div className="mt-4">
        Found anagrams at indices: {foundAnagrams.join(", ")}
      </div>
    </div>
  );
};

export default SlidingWindow;
```

This interactive visualization demonstrates the sliding window technique used in the "Find All Anagrams in a String" problem. The yellow highlight shows the current window, and green characters indicate the starting positions of found anagrams. You can modify the input strings to see how the algorithm works with different inputs.
