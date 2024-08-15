# Explanation: Word Break

## Analysis of problem & input data

This problem is a classic example of string segmentation, which often lends itself to dynamic programming or recursive solutions with memoization. The key characteristics and insights are:

1. We need to determine if the entire string can be segmented, not just find one valid segmentation.
2. Words from the dictionary can be reused multiple times.
3. The order of words in the dictionary doesn't matter.
4. The problem exhibits optimal substructure: if we can segment the first part of the string and the remaining part is in the dictionary, the whole string is segmentable.
5. There are overlapping subproblems: we might check the same substring multiple times in different recursive calls.

The key principle that makes this question approachable is that we can build up the solution for the entire string by solving and remembering solutions for its prefixes. This is a hallmark of dynamic programming problems.

### Test cases

```python
def test_word_break():
    # Test case 1: Basic case with simple segmentation
    assert word_break("leetcode", ["leet", "code"]) == True

    # Test case 2: Word reuse allowed
    assert word_break("applepenapple", ["apple", "pen"]) == True

    # Test case 3: Impossible segmentation
    assert word_break("catsandog", ["cats", "dog", "sand", "and", "cat"]) == False

    # Test case 4: Empty string (edge case)
    assert word_break("", ["a"]) == True

    # Test case 5: Single character string
    assert word_break("a", ["a"]) == True

    # Test case 6: Long string with many segmentations
    assert word_break("aaaaaaa", ["a", "aa", "aaa", "aaaa"]) == True

    # Test case 7: String not in dictionary
    assert word_break("abcd", ["a", "abc", "b", "cd"]) == False

    # Test case 8: Overlapping words
    assert word_break("abcde", ["ab", "abc", "cd", "de"]) == True

    print("All test cases passed!")

# Run the tests
test_word_break()
```

## Solutions

### Overview of solution approaches

#### Solutions worth learning

1. Dynamic Programming (Bottom-up)
2. Recursion with Memoization (Top-down)
3. BFS with Queue
4. Trie-based Solution

Count: 4 solutions

#### Rejected solutions

1. Brute Force Recursion without Memoization
2. Greedy Approach
3. Regular Expression Matching

### Worthy Solutions

#### 1. Dynamic Programming (Bottom-up)

```python
from typing import List

def word_break(s: str, word_dict: List[str]) -> bool:
    n = len(s)
    dp = [False] * (n + 1)  # dp[i] represents if s[:i] can be segmented
    dp[0] = True  # Empty string is always segmentable

    word_set = set(word_dict)  # Convert list to set for O(1) lookup

    for i in range(1, n + 1):
        for j in range(i):
            # If s[:j] is segmentable and s[j:i] is in the dictionary,
            # then s[:i] is segmentable
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break  # Once we find a valid segmentation, we can stop checking

    return dp[n]  # dp[n] represents if the entire string s is segmentable
```

Time Complexity: O(n^2 \* m), where n is the length of the string and m is the average length of words in the dictionary (for substring comparison).
Space Complexity: O(n) for the dp array.

Key intuitions and invariants:

- `dp[i]` represents whether the substring `s[:i]` can be segmented into words from the dictionary.
- We build up the solution for longer substrings using solutions for shorter substrings.
- The base case is an empty string, which is always segmentable.
- For each index i, we check all possible splits of the substring s[:i] into two parts: s[:j] and s[j:i].
- If s[:j] is segmentable (dp[j] is True) and s[j:i] is in the dictionary, then s[:i] is segmentable.

#### 2. Recursion with Memoization (Top-down)

```python
from typing import List

def word_break(s: str, word_dict: List[str]) -> bool:
    word_set = set(word_dict)
    memo = {}  # Memoization cache

    def can_break(start: int) -> bool:
        if start == len(s):
            return True

        if start in memo:
            return memo[start]

        for end in range(start + 1, len(s) + 1):
            # If the current substring is in the dictionary and the rest can be broken
            if s[start:end] in word_set and can_break(end):
                memo[start] = True
                return True

        memo[start] = False
        return False

    return can_break(0)
```

Time Complexity: O(n^2 \* m) in the worst case, where n is the length of the string and m is the average length of words in the dictionary.
Space Complexity: O(n) for the recursion stack and memoization cache.

Key intuitions and invariants:

- We use recursion to try all possible splits of the string.
- The memoization cache stores results for subproblems to avoid redundant computations.
- The base case is when we've successfully segmented the entire string.
- For each recursive call, we try to find a prefix that's in the dictionary and recursively solve for the remaining suffix.
- The memoization ensures that we solve each subproblem only once.

#### 3. BFS with Queue

```python
from typing import List
from collections import deque

def word_break(s: str, word_dict: List[str]) -> bool:
    word_set = set(word_dict)
    queue = deque([0])  # Start index
    visited = set()  # To avoid revisiting indices

    while queue:
        start = queue.popleft()
        if start == len(s):
            return True

        for end in range(start + 1, len(s) + 1):
            if end in visited:
                continue

            if s[start:end] in word_set:
                queue.append(end)
                visited.add(end)

    return False
```

Time Complexity: O(n^2 \* m), where n is the length of the string and m is the average length of words in the dictionary.
Space Complexity: O(n) for the queue and visited set.

Key intuitions and invariants:

- We use BFS to explore all possible segmentations level by level.
- Each level represents the end index of a potential word.
- The queue stores the starting indices for the next word to be checked.
- The visited set prevents re-checking the same index, avoiding cycles and redundant work.
- If we reach the end of the string (len(s)), we've found a valid segmentation.

#### 4. Trie-based Solution

```python
from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_word = True

def word_break(s: str, word_dict: List[str]) -> bool:
    trie = Trie()
    for word in word_dict:
        trie.insert(word)

    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True

    for i in range(1, n + 1):
        node = trie.root
        for j in range(i, 0, -1):
            if s[j-1] not in node.children:
                break
            node = node.children[s[j-1]]
            if node.is_word and dp[j-1]:
                dp[i] = True
                break

    return dp[n]
```

Time Complexity: O(n^2), where n is the length of the string. The Trie construction is O(k), where k is the total length of all words in the dictionary.
Space Complexity: O(k) for the Trie, plus O(n) for the dp array.

Key intuitions and invariants:

- We use a Trie to efficiently store and search for dictionary words.
- The dp array is used similarly to the bottom-up DP approach.
- For each index, we traverse the Trie backwards from that index, checking if we can form valid words.
- If we find a valid word and the previous segment is breakable, we mark the current index as breakable.
- The Trie allows us to stop searching early if a prefix is not in the dictionary.

### Rejected Approaches

1. Brute Force Recursion without Memoization:

   - This approach would try all possible segmentations recursively.
   - It's correct but highly inefficient, with a time complexity of O(2^n) in the worst case.
   - Rejected due to exponential time complexity, making it impractical for longer strings.

2. Greedy Approach:

   - Attempting to always choose the longest possible word at each step.
   - This doesn't work because sometimes we need to choose shorter words to make the overall segmentation possible.
   - Example where it fails: s = "catsandogcat", dict = ["cats", "cat", "sand", "and", "dog"]

3. Regular Expression Matching:
   - Creating a regex pattern from the dictionary and matching against the string.
   - While theoretically possible, it's inefficient and doesn't leverage the specific structure of the problem.
   - Regex matching can have poor performance for complex patterns and long strings.

### Final Recommendations

The Dynamic Programming (Bottom-up) approach is recommended as the best solution to learn for this problem. Here's why:

1. It's intuitive and directly translates the problem into code.
2. It has a predictable time and space complexity.
3. It's iterative, which often performs better than recursive solutions in practice.
4. It's easier to understand and explain in an interview setting.

The Recursion with Memoization approach is a close second and is worth learning as it demonstrates top-down dynamic programming.

The BFS approach, while less common, is an interesting alternative that demonstrates how graph traversal techniques can be applied to string problems.

The Trie-based solution, while efficient, might be overkill for this specific problem and is more complex to implement in an interview setting. However, it's a good solution to know if you're dealing with a large dictionary or need to perform many word break operations.

The brute force recursion without memoization, while correct, is not worth implementing due to its exponential time complexity. It's important to recognize why it's inefficient and how memoization or dynamic programming improves upon it.

The greedy approach and regex matching are examples of solutions that might seem appealing at first but are actually incorrect or impractical for this problem. It's valuable to understand why they don't work to avoid similar pitfalls in other problems.

## Visualization(s)

For the Dynamic Programming approach, we can visualize the dp array as it's being filled:

```
s = "leetcode"
wordDict = ["leet", "code"]

dp array:
[T, F, F, F, F, F, F, F, F]
 ^  ^  ^  ^
 0  1  2  3  4  5  6  7  8

After processing "l":
[T, F, F, F, F, F, F, F, F]

After processing "le":
[T, F, F, F, F, F, F, F, F]

After processing "lee":
[T, F, F, F, F, F, F, F, F]

After processing "leet":
[T, F, F, F, T, F, F, F, F]
             ^
             "leet" found

After processing "leetc":
[T, F, F, F, T, F, F, F, F]

After processing "leetco":
[T, F, F, F, T, F, F, F, F]

After processing "leetcod":
[T, F, F, F, T, F, F, F, F]

After processing "leetcode":
[T, F, F, F, T, F, F, F, T]
                         ^
                         "code" found after "leet"

Final result: True (dp[8] is True)
```

This visualization shows how the dp array is filled from left to right, with True values indicating that the substring up to that index can be segmented using words from the dictionary.
