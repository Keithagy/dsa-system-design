# Explanation: Longest Palindromic Substring

## Analysis of problem & input data

The Longest Palindromic Substring problem is a classic string manipulation problem that requires finding the longest substring within a given string that reads the same forwards and backwards. Key aspects to consider:

1. Palindrome property: A palindrome reads the same forwards and backwards.
2. Substring vs. subsequence: We're looking for a contiguous sequence of characters, not a subsequence.
3. Multiple valid answers: There can be multiple palindromic substrings of the same maximum length.
4. Input characteristics: The string contains only digits and English letters, which simplifies character comparison.
5. Length constraints: The input string length is between 1 and 1000, inclusive.

Key principle: Palindromes have a center (either a single character or between two characters) and expand outwards symmetrically. This property allows us to check for palindromes by expanding from potential centers.

### Test cases

1. Basic cases:

   - Input: "babad" -> Output: "bab" or "aba"
   - Input: "cbbd" -> Output: "bb"

2. Edge cases:

   - Single character: "a" -> "a"
   - All same characters: "aaaa" -> "aaaa"
   - No palindromes longer than 1: "abcd" -> "a" (or "b", "c", or "d")

3. Challenging inputs:
   - Long palindrome at the end: "abcdefghhgfedcba" -> "abcdefghhgfedcba"
   - Multiple palindromes of same length: "aabbaa" -> "aabbaa"
   - Palindrome with odd length: "racecar" -> "racecar"
   - Palindrome with even length: "abccba" -> "abccba"

Here's the Python code for these test cases:

```python
def test_longest_palindrome(func):
    test_cases = [
        ("babad", {"bab", "aba"}),
        ("cbbd", {"bb"}),
        ("a", {"a"}),
        ("aaaa", {"aaaa"}),
        ("abcd", {"a", "b", "c", "d"}),
        ("abcdefghhgfedcba", {"abcdefghhgfedcba"}),
        ("aabbaa", {"aabbaa"}),
        ("racecar", {"racecar"}),
        ("abccba", {"abccba"})
    ]

    for i, (s, expected) in enumerate(test_cases):
        result = func(s)
        assert result in expected, f"Test case {i + 1} failed. Input: {s}, Expected: {expected}, Got: {result}"
    print("All test cases passed!")

# The longest_palindrome function would be tested like this:
# test_longest_palindrome(longest_palindrome)
```

## Solutions

### Overview of solution approaches

#### Solutions worth learning

1. Expand Around Center (Two-Pointer)
2. Dynamic Programming
3. Manacher's Algorithm

3 solutions worth learning.

#### Rejected solutions

1. Brute Force (checking all substrings)
2. Suffix Tree

### Worthy Solutions

#### 1. Expand Around Center (Two-Pointer)

```python
def longest_palindrome(s: str) -> str:
    if not s:
        return ""

    def expand_around_center(left: int, right: int) -> int:
        """
        Expands around a potential palindrome center, returning the length.
        This function leverages the symmetric nature of palindromes.
        """
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1  # Length of the palindrome

    start, max_length = 0, 0
    for i in range(len(s)):
        # Check for odd-length palindromes (single character center)
        len1 = expand_around_center(i, i)
        # Check for even-length palindromes (between two characters)
        len2 = expand_around_center(i, i + 1)

        # Update if a longer palindrome is found
        curr_max = max(len1, len2)
        if curr_max > max_length:
            max_length = curr_max
            # Calculate the start index of the palindrome
            start = i - (curr_max - 1) // 2

    return s[start:start + max_length]
```

Time Complexity: O(n^2), where n is the length of the string.
Space Complexity: O(1), as we only use a constant amount of extra space.

Key intuitions and invariants:

- Palindromes expand symmetrically around their center.
- There are 2n-1 possible centers (n single-character centers and n-1 between-character centers).
- By expanding from the center, we avoid unnecessary checks of invalid palindromes.
- The algorithm maintains the invariant that it always finds the longest palindrome centered at each possible center.

#### 2. Dynamic Programming

```python
def longest_palindrome(s: str) -> str:
    n = len(s)
    # dp[i][j] will be True if substring s[i:j+1] is a palindrome
    dp = [[False] * n for _ in range(n)]

    # All substrings of length 1 are palindromes
    for i in range(n):
        dp[i][i] = True

    start = 0
    max_length = 1

    # Check for substrings of length 2
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            start = i
            max_length = 2

    # Check for lengths greater than 2
    # k is the length of substring
    for k in range(3, n + 1):
        # Fix the starting index
        for i in range(n - k + 1):
            # Get the ending index of substring from
            # starting index i and length k
            j = i + k - 1

            # Checking for substring from ith index to jth index
            # if s[i+1] to s[j-1] is a palindrome
            if dp[i + 1][j - 1] and s[i] == s[j]:
                dp[i][j] = True
                if k > max_length:
                    start = i
                    max_length = k

    return s[start:start + max_length]
```

Time Complexity: O(n^2), where n is the length of the string.
Space Complexity: O(n^2) to store the dp table.

Key intuitions and invariants:

- A string is a palindrome if its first and last characters match, and the substring between them is also a palindrome.
- We build up solutions for longer palindromes using solutions for shorter palindromes.
- The dp table maintains the invariant that dp[i][j] is true if and only if the substring s[i:j+1] is a palindrome.
- We fill the table diagonally, ensuring that when we check dp[i+1][j-1], it's already computed.

#### 3. Manacher's Algorithm

```python
def longest_palindrome(s: str) -> str:
    # Transform S into T.
    # For example, S = "abba", T = "^#a#b#b#a#$".
    # ^ and $ signs are sentinels appended to each end to avoid bounds checking
    T = '#'.join('^{}$'.format(s))
    n = len(T)
    P = [0] * n
    C = R = 0
    for i in range(1, n-1):
        # If i is within the last palindrome, mirror the value
        P[i] = (R > i) and min(R - i, P[2*C - i])

        # Attempt to expand palindrome centered at i
        while T[i + 1 + P[i]] == T[i - 1 - P[i]]:
            P[i] += 1

        # If palindrome centered at i expands past R,
        # adjust center based on expanded palindrome.
        if i + P[i] > R:
            C, R = i, i + P[i]

    # Find the maximum element in P
    maxLen, centerIndex = max((n, i) for i, n in enumerate(P))
    start = (centerIndex - maxLen) // 2
    return s[start:start + maxLen]
```

Time Complexity: O(n), where n is the length of the string.
Space Complexity: O(n) to store the transformed string and the P array.

Key intuitions and invariants:

- By transforming the string, we unify the treatment of odd and even length palindromes.
- The algorithm leverages previously computed information to avoid unnecessary comparisons.
- The P array maintains the invariant that P[i] is the radius of the longest palindrome centered at i in the transformed string.
- The center (C) and right boundary (R) of the currently known rightmost palindrome are maintained as invariants throughout the algorithm.

### Rejected Approaches

1. Brute Force (checking all substrings):

   - Time Complexity: O(n^3)
   - Reason for rejection: Highly inefficient for larger inputs. Doesn't leverage the palindrome property effectively.

2. Suffix Tree:
   - While efficient for certain string problems, it's overkill for this specific problem.
   - The construction of a suffix tree takes O(n) time and space, but the algorithm to find the longest palindromic substring using a suffix tree is more complex and not as intuitive as other methods.

### Final Recommendations

The Expand Around Center approach is recommended as the best solution to learn for this problem. Here's why:

1. Intuitive: It directly leverages the palindrome property of expanding from the center.
2. Space-efficient: Uses O(1) extra space.
3. Reasonably time-efficient: O(n^2) is acceptable for most interview scenarios.
4. Easy to implement: The code is straightforward and doesn't require complex data structures.

The Dynamic Programming solution is also worth understanding as it demonstrates a classic DP approach to string problems. However, it's less space-efficient than the center expansion method.

Manacher's Algorithm, while theoretically the most efficient with O(n) time complexity, is more complex and might be overkill for an interview setting unless specifically asked for or if dealing with extremely large strings.

The brute force approach of checking all substrings (O(n^3)) should be avoided as it's highly inefficient and doesn't leverage the problem's properties effectively.

## Visualization(s)

To visualize the Expand Around Center approach, consider this ASCII art representation:

```
String: "racecar"
         ↑
         center

Step 1:  r a c e c a r
           ↑ ↑ ↑
           l c r

Step 2:  r a c e c a r
         ↑ ↑     ↑ ↑
         l       r

Step 3:  r a c e c a r
       ↑ ↑         ↑ ↑
       l           r

Final:  r a c e c a r
      ↑ ↑           ↑ ↑
      l             r
```

This visualization shows how the algorithm expands from the center (in this case, 'e') outwards, comparing characters symmetrically until it can't expand further. The process is repeated for each possible center (including between-character centers for even-length palindromes).
