# Explanation: Valid Anagram

## Analysis of problem & input data

The Valid Anagram problem is a classic string manipulation and comparison task. Here are the key aspects to consider:

1. We're dealing with two strings, `s` and `t`.
2. The goal is to determine if `t` is an anagram of `s`.
3. An anagram is formed by rearranging all the letters of the original word, using each letter exactly once.
4. The problem constraints specify that both strings consist of lowercase English letters only.
5. The length of the strings can be up to 5 \* 10^4^ characters.

Key principles that make this question simple:

1. Anagrams have the same character frequency, just in a different order.
2. We're dealing with a limited character set (26 lowercase English letters).
3. The order of characters doesn't matter for anagrams, only their frequency.

### Test cases

Here are some test cases to consider:

1. Basic valid anagram:

   - Input: s = "listen", t = "silent"
   - Expected Output: True

2. Basic invalid anagram:

   - Input: s = "hello", t = "world"
   - Expected Output: False

3. Same length, different characters:

   - Input: s = "aacc", t = "ccac"
   - Expected Output: False

4. Different lengths:

   - Input: s = "ab", t = "a"
   - Expected Output: False

5. Empty strings:

   - Input: s = "", t = ""
   - Expected Output: True

6. Single character:

   - Input: s = "a", t = "a"
   - Expected Output: True

7. Repeated characters:

   - Input: s = "anagram", t = "nagaram"
   - Expected Output: True

8. Unicode characters (for follow-up):
   - Input: s = "こんにちは", t = "はちにんこ"
   - Expected Output: True

Here's the Python code to implement these test cases:

```python
def is_anagram(s: str, t: str) -> bool:
    # Implementation to be added later
    pass

# Test cases
test_cases = [
    ("listen", "silent", True),
    ("hello", "world", False),
    ("aacc", "ccac", False),
    ("ab", "a", False),
    ("", "", True),
    ("a", "a", True),
    ("anagram", "nagaram", True),
    ("こんにちは", "はちにんこ", True)
]

for i, (s, t, expected) in enumerate(test_cases, 1):
    result = is_anagram(s, t)
    print(f"Test case {i}: {'Passed' if result == expected else 'Failed'}")
    if result != expected:
        print(f"  Input: s = '{s}', t = '{t}'")
        print(f"  Expected: {expected}, Got: {result}")
```

## Solutions

### Overview of solution approaches

#### Solutions worth learning

1. Sorting approach
2. Hash map / Character count approach
3. Array-based character count (for fixed character set)

Count: 3 solutions

#### Rejected solutions

1. Brute force permutation generation
2. Prime number product approach

### Worthy Solutions

#### 1. Sorting approach

```python
def is_anagram(s: str, t: str) -> bool:
    # If the lengths are different, they can't be anagrams
    if len(s) != len(t):
        return False

    # Sort both strings and compare them
    # Sorting rearranges the characters in a deterministic order
    # If the strings are anagrams, they will be identical after sorting
    return sorted(s) == sorted(t)
```

Time Complexity: O(n log n), where n is the length of the strings (due to sorting)
Space Complexity: O(n) for the sorted strings (depending on the sorting algorithm)

Intuitions and invariants:

- Anagrams have the same characters, just in a different order
- Sorting both strings will result in identical sequences if they are anagrams
- This approach works regardless of the character set (handles the Unicode follow-up naturally)

#### 2. Hash map / Character count approach

```python
from collections import Counter

def is_anagram(s: str, t: str) -> bool:
    # If the lengths are different, they can't be anagrams
    if len(s) != len(t):
        return False

    # Use Counter to count the frequency of each character
    # Counter is a specialized dictionary for counting hashable objects
    char_count = Counter(s)

    # Iterate through t, decrementing the count for each character
    for char in t:
        # If we encounter a character not in s, or its count becomes negative,
        # t is not an anagram of s
        if char not in char_count or char_count[char] == 0:
            return False
        char_count[char] -= 1

    # If we've made it through all characters in t without returning False,
    # t must be an anagram of s
    return True
```

Time Complexity: O(n), where n is the length of the strings
Space Complexity: O(k), where k is the number of unique characters in s

Intuitions and invariants:

- Anagrams have the same character frequency
- We can count characters in one string and verify against the other
- This approach is more efficient for larger strings or when sorting is expensive
- It can handle any character set, addressing the Unicode follow-up question

#### 3. Array-based character count (for fixed character set)

```python
def is_anagram(s: str, t: str) -> bool:
    # If the lengths are different, they can't be anagrams
    if len(s) != len(t):
        return False

    # Initialize an array to store character counts
    # We use 26 for lowercase English letters (a-z)
    char_count = [0] * 26

    # Count characters in s and decrement for t
    for c_s, c_t in zip(s, t):
        # Convert character to index (0-25) and update count
        char_count[ord(c_s) - ord('a')] += 1
        char_count[ord(c_t) - ord('a')] -= 1

    # If all counts are zero, s and t are anagrams
    return all(count == 0 for count in char_count)
```

Time Complexity: O(n), where n is the length of the strings
Space Complexity: O(1), as we use a fixed-size array of 26 elements

Intuitions and invariants:

- For a fixed character set (lowercase English letters), we can use an array instead of a hash map
- The array indices represent characters, and the values represent their frequency difference between s and t
- If s and t are anagrams, all counts in the array will be zero after processing both strings
- This approach is memory-efficient for the given constraint of lowercase English letters

### Rejected Approaches

1. Brute force permutation generation:

   - Generate all permutations of s and check if t is among them
   - Rejected because it has a time complexity of O(n!), which is extremely inefficient
   - Not suitable for strings longer than ~10 characters

2. Prime number product approach:
   - Assign a unique prime number to each character and compute the product for both strings
   - Rejected because it can lead to integer overflow for long strings
   - Doesn't handle the case where characters are repeated different numbers of times in s and t

### Final Recommendations

The hash map / character count approach (Solution 2) is the best one to learn and use in an interview setting. Here's why:

1. It has optimal time complexity O(n) and space complexity O(k), where k is the number of unique characters.
2. It's versatile and can handle any character set, addressing the Unicode follow-up question.
3. It demonstrates understanding of hash maps, a crucial data structure in coding interviews.
4. The implementation is straightforward and easy to explain.

The sorting approach, while simple, is less efficient due to its O(n log n) time complexity. However, it's worth mentioning in an interview as an initial solution before optimizing.

The array-based approach is very efficient for the given constraint of lowercase English letters, but it's less flexible for handling different character sets. It's a good optimization to mention if the interviewer specifically asks about optimizing for the given constraints.

The rejected approaches (brute force permutation and prime number product) are worth mentioning briefly to demonstrate problem-solving breadth, but should be quickly dismissed due to their inefficiencies or limitations.

## Visualization(s)

To visualize the hash map / character count approach, we can use a simple ASCII-based representation:

```
Input: s = "anagram", t = "nagaram"

Step 1: Count characters in s
+---+---+---+---+---+---+
| a | n | g | r | m |   |
+---+---+---+---+---+---+
| 3 | 1 | 1 | 1 | 1 |   |
+---+---+---+---+---+---+

Step 2: Process t and decrement counts
+---+---+---+---+---+---+
| a | n | g | r | m |   |
+---+---+---+---+---+---+
| 0 | 0 | 0 | 0 | 0 |   |
+---+---+---+---+---+---+

Result: All counts are zero, so s and t are anagrams
```

This visualization helps to understand how the algorithm counts characters in s and then verifies them against t, resulting in all zero counts for a valid anagram.
