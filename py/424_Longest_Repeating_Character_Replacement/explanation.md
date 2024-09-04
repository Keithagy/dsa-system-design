## Explanation: Longest Repeating Character Replacement

### Analysis of problem & input data

This problem falls into the category of sliding window problems, specifically dealing with string manipulation and character frequency. The key aspects to consider are:

1. We're working with a string of uppercase English letters.
2. We have a constraint `k`, which represents the maximum number of character replacements allowed.
3. We need to find the longest substring where all characters are the same after performing at most `k` replacements.

The key principle that makes this question simple is the sliding window technique combined with character frequency counting. By maintaining a window and a count of the most frequent character within that window, we can determine if the current window is valid (can be made into a string of all the same characters with at most `k` replacements).

The pattern-matching here is recognizing that we don't actually need to perform the replacements, but rather keep track of the character frequencies and the most frequent character in our current window. This allows us to calculate how many replacements would be needed to make all characters in the window the same.

### Test cases

1. Basic case:

   - Input: s = "ABAB", k = 2
   - Output: 4

2. Case with one replacement:

   - Input: s = "AABABBA", k = 1
   - Output: 4

3. No replacements needed:

   - Input: s = "AAAA", k = 2
   - Output: 4

4. More replacements than needed:

   - Input: s = "ABCD", k = 5
   - Output: 4

5. Single character string:

   - Input: s = "A", k = 0
   - Output: 1

6. Long string with small k:
   - Input: s = "AABABBACCCCCDDDDEEEE", k = 2
   - Output: 7

Here's the Python code for these test cases:

```python
def characterReplacement(s: str, k: int) -> int:
    # Implementation will go here
    pass

# Test cases
test_cases = [
    ("ABAB", 2, 4),
    ("AABABBA", 1, 4),
    ("AAAA", 2, 4),
    ("ABCD", 5, 4),
    ("A", 0, 1),
    ("AABABBACCCCCDDDDEEEE", 2, 7)
]

for i, (s, k, expected) in enumerate(test_cases):
    result = characterReplacement(s, k)
    print(f"Test case {i+1}: {'Passed' if result == expected else 'Failed'}")
    print(f"Input: s = '{s}', k = {k}")
    print(f"Expected: {expected}, Got: {result}\n")
```

### Solutions

#### Overview of solution approaches

##### Solutions worth learning

1. Sliding Window with Character Frequency Count (Neetcode solution)
2. Sliding Window with Binary Search
3. Dynamic Programming (less optimal but conceptually important)

Count: 3 solutions (1 Neetcode solution)

##### Rejected solutions

1. Brute Force: Checking all substrings and performing replacements (O(n^3) time complexity, too slow)
2. Recursive approach: Not suitable due to potential stack overflow for large inputs

#### Worthy Solutions

##### Sliding Window with Character Frequency Count

```python
from collections import defaultdict

def characterReplacement(s: str, k: int) -> int:
    char_count = defaultdict(int)
    max_length = 0
    max_count = 0
    left = 0

    for right in range(len(s)):
        # Update the count of the current character
        char_count[s[right]] += 1

        # Update the count of the most frequent character in the current window
        max_count = max(max_count, char_count[s[right]])

        # If the number of replacements needed exceeds k, shrink the window
        while (right - left + 1) - max_count > k:
            char_count[s[left]] -= 1
            left += 1

        # Update the max_length
        max_length = max(max_length, right - left + 1)

    return max_length
```

Time Complexity: O(n), where n is the length of the string

- We iterate through the string once with the right pointer.
- The left pointer also moves from left to right, never moving back, resulting in amortized O(1) for the inner while loop.

Space Complexity: O(1)

- We use a defaultdict to store character counts, but since we're dealing with uppercase English letters only, the size of this dictionary is bounded by 26, which is constant.

Intuitions and invariants:

- The sliding window maintains a valid substring where at most k replacements are needed to make all characters the same.
- `max_count` represents the count of the most frequent character in the current window.
- The condition `(right - left + 1) - max_count > k` checks if the current window requires more than k replacements.
- We don't need to track which character is the most frequent, only its count.
- The window expands as long as it's valid and contracts when it becomes invalid.

##### Sliding Window with Binary Search

```python
from collections import defaultdict

def characterReplacement(s: str, k: int) -> int:
    def canMakeValidSubstring(length):
        char_count = defaultdict(int)
        max_count = 0

        for i in range(len(s)):
            if i >= length:
                char_count[s[i - length]] -= 1

            char_count[s[i]] += 1
            max_count = max(max_count, char_count[s[i]])

            if i >= length - 1 and length - max_count <= k:
                return True

        return False

    left, right = 1, len(s)
    result = 0

    while left <= right:
        mid = (left + right) // 2
        if canMakeValidSubstring(mid):
            result = mid
            left = mid + 1
        else:
            right = mid - 1

    return result
```

Time Complexity: O(n log n), where n is the length of the string

- The binary search runs O(log n) times
- For each iteration of binary search, we scan the string once, which is O(n)

Space Complexity: O(1)

- We use a defaultdict to store character counts, but its size is bounded by 26 (constant)

Intuitions and invariants:

- We binary search on the length of the valid substring
- For each length, we check if we can make a valid substring of that length using at most k replacements
- The `canMakeValidSubstring` function uses a sliding window of fixed size to check validity
- We optimize by keeping track of the maximum count in the current window

##### Dynamic Programming

```python
def characterReplacement(s: str, k: int) -> int:
    n = len(s)
    dp = [[0] * 26 for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(26):
            if ord(s[i-1]) - ord('A') == j:
                dp[i][j] = dp[i-1][j] + 1
            else:
                dp[i][j] = dp[i-1][j]

    def isValid(length):
        for i in range(length, n + 1):
            for j in range(26):
                if i - dp[i][j] <= k:
                    return True
        return False

    left, right = 1, n
    result = 0

    while left <= right:
        mid = (left + right) // 2
        if isValid(mid):
            result = mid
            left = mid + 1
        else:
            right = mid - 1

    return result
```

Time Complexity: O(n^2), where n is the length of the string

- We fill the dp table in O(n) time
- The binary search runs O(log n) times
- For each iteration of binary search, we check validity in O(n) time

Space Complexity: O(n)

- We use a 2D dp table of size n \* 26

Intuitions and invariants:

- `dp[i][j]` represents the count of character `chr(ord('A') + j)` in the prefix `s[:i]`
- We use binary search to find the maximum valid length
- For each length, we check if we can make a valid substring of that length using at most k replacements
- This approach is less optimal than the sliding window solutions but demonstrates a different way of thinking about the problem

#### Rejected Approaches

1. Brute Force: Checking all substrings and performing replacements

   - Time Complexity: O(n^3)
   - Reason for rejection: Too slow for large inputs, doesn't leverage the problem's properties effectively

2. Recursive approach
   - Reason for rejection: Potential for stack overflow with large inputs, and doesn't efficiently reuse computed information

#### Final Recommendations

The Sliding Window with Character Frequency Count (Neetcode solution) is the best to learn for this problem. It's the most efficient in terms of both time and space complexity, and it directly leverages the problem's properties. This approach demonstrates a deep understanding of the sliding window technique and how to apply it to string manipulation problems.

The Binary Search approach is also worth understanding as it showcases how to optimize when you have a clear monotonic property (in this case, if a length l is valid, all lengths <= l are also valid).

The Dynamic Programming solution, while less optimal, is valuable for understanding how to approach such problems from a different angle and can be useful in related problems where maintaining a running count is beneficial.

### Visualization(s)

For the Sliding Window approach, we can visualize the window expansion and contraction:

```
s = "AABABBA", k = 1

Step 1: [A]ABABBA    max_count = 1, length = 1
Step 2: [AA]BABBA    max_count = 2, length = 2
Step 3: [AAB]ABBA    max_count = 2, length = 3
Step 4: [AABA]BBA    max_count = 3, length = 4
Step 5: A[ABAB]BA    max_count = 2, length = 4
Step 6: AA[BABB]A    max_count = 3, length = 4
Step 7: AAB[ABBA]    max_count = 3, length = 4

Final result: 4
```

This visualization shows how the window expands when it's valid (can be made into a string of all the same characters with at most k replacements) and contracts when it becomes invalid. The max_count represents the count of the most frequent character in the current window.
