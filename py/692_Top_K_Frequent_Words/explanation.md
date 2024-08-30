## Explanation: Top K Frequent Words

### Analysis of problem & input data

This problem is a combination of frequency counting, sorting, and selection. The key aspects to consider are:

1. Frequency counting: We need to count the occurrences of each word.
2. Sorting: We need to sort the words based on their frequency and lexicographical order.
3. Selection: We need to select the top k elements from the sorted list.

The input data characteristics are:

- An array of strings (words)
- An integer k
- The words are lowercase English letters
- The length of the input array is between 1 and 500
- Each word's length is between 1 and 10
- k is between 1 and the number of unique words

The key principle that makes this question approachable is the use of a hash map (dictionary in Python) for frequency counting, combined with custom sorting. The challenge lies in efficiently sorting and selecting the top k elements.

This problem falls into the category of "Hash Table" and "Heap" problems on LeetCode. The frequency counting aspect suggests using a hash table, while the selection of top k elements hints at using a heap (priority queue) for an optimal solution.

### Test cases

Here are some relevant test cases:

1. Basic case:

   ```python
   words = ["i", "love", "leetcode", "i", "love", "coding"]
   k = 2
   # Expected output: ["i", "love"]
   ```

2. Case with same frequencies:

   ```python
   words = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
   k = 4
   # Expected output: ["the", "is", "sunny", "day"]
   ```

3. Edge case - k equals number of unique words:

   ```python
   words = ["a", "b", "c", "d", "e"]
   k = 5
   # Expected output: ["a", "b", "c", "d", "e"]
   ```

4. Edge case - single word:

   ```python
   words = ["leetcode"]
   k = 1
   # Expected output: ["leetcode"]
   ```

5. Case with ties in both frequency and lexicographical order:
   ```python
   words = ["a", "aa", "aaa", "a", "aa", "aaa"]
   k = 3
   # Expected output: ["a", "aa", "aaa"]
   ```

Here's the executable Python code for these test cases:

```python
def test_top_k_frequent(func):
    test_cases = [
        (["i", "love", "leetcode", "i", "love", "coding"], 2, ["i", "love"]),
        (["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], 4, ["the", "is", "sunny", "day"]),
        (["a", "b", "c", "d", "e"], 5, ["a", "b", "c", "d", "e"]),
        (["leetcode"], 1, ["leetcode"]),
        (["a", "aa", "aaa", "a", "aa", "aaa"], 3, ["a", "aa", "aaa"])
    ]

    for i, (words, k, expected) in enumerate(test_cases):
        result = func(words, k)
        assert result == expected, f"Test case {i + 1} failed. Expected {expected}, but got {result}"
    print("All test cases passed!")

# Usage:
# test_top_k_frequent(topKFrequent)
```

### Solutions

#### Overview of solution approaches

##### Solutions worth learning

1. Hash Map + Heap (Priority Queue) [Neetcode solution]
2. Hash Map + Bucket Sort
3. Hash Map + Custom Sort
4. Trie + DFS

Count: 4 solutions (1 Neetcode solution)

##### Rejected solutions

1. Brute Force: Counting frequencies and sorting the entire list
2. Using a balanced BST instead of a heap

#### Worthy Solutions

##### Hash Map + Heap (Priority Queue) [Neetcode solution]

```python
from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # Count the frequency of each word
        word_counts = Counter(words)

        # Create a min heap of (-frequency, word) pairs
        heap = [(-freq, word) for word, freq in word_counts.items()]
        heapq.heapify(heap)

        # Pop the k most frequent elements
        return [heapq.heappop(heap)[1] for _ in range(k)]
```

Time Complexity: O(n log k), where n is the number of words

- Counting frequencies takes O(n) time
- Heapifying takes O(n) time
- Popping k elements from the heap takes O(k log n) time

Space Complexity: O(n)

- The Counter and heap both store all unique words, which in the worst case is O(n)

Intuitions and invariants:

- Using a Counter for efficient frequency counting
- Using a min heap to maintain the top k elements
- Negating the frequency to turn the min heap into a max heap
- The heap property ensures that the most frequent words are at the top
- Lexicographical order is maintained by the heap's comparison of tuples

##### Hash Map + Bucket Sort

```python
from collections import Counter

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # Count the frequency of each word
        word_counts = Counter(words)

        # Create buckets for each frequency
        buckets = [[] for _ in range(len(words) + 1)]
        for word, freq in word_counts.items():
            buckets[freq].append(word)

        # Collect the k most frequent words
        result = []
        for bucket in reversed(buckets):
            bucket.sort()  # Sort words in the same frequency lexicographically
            result.extend(bucket)
            if len(result) >= k:
                return result[:k]

        return result[:k]  # This line should never be reached given the problem constraints
```

Time Complexity: O(n + m log m), where n is the number of words and m is the number of unique words

- Counting frequencies takes O(n) time
- Creating buckets takes O(m) time
- Sorting each bucket takes O(m log m) time in the worst case
- Collecting results takes O(m) time

Space Complexity: O(n)

- The Counter and buckets both store all words, which is O(n)

Intuitions and invariants:

- Using buckets to group words by frequency
- Reversing the bucket order to get the most frequent words first
- Sorting words within each bucket maintains lexicographical order
- The bucket index corresponds to the word frequency

##### Hash Map + Custom Sort

```python
from collections import Counter

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # Count the frequency of each word
        word_counts = Counter(words)

        # Sort words based on frequency (descending) and lexicographical order
        sorted_words = sorted(word_counts.keys(), key=lambda x: (-word_counts[x], x))

        # Return the top k words
        return sorted_words[:k]
```

Time Complexity: O(n log n), where n is the number of words

- Counting frequencies takes O(n) time
- Sorting takes O(n log n) time

Space Complexity: O(n)

- The Counter stores all unique words, which in the worst case is O(n)

Intuitions and invariants:

- Using a Counter for efficient frequency counting
- Custom sort key that prioritizes frequency (negated for descending order) and then lexicographical order
- The sorted list maintains both frequency and lexicographical order

##### Trie + DFS

```python
from collections import Counter

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
        self.frequency = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str, freq: int):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True
        node.frequency = freq

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # Count the frequency of each word
        word_counts = Counter(words)

        # Build the Trie
        trie = Trie()
        for word, freq in word_counts.items():
            trie.insert(word, freq)

        # DFS to collect words
        self.result = []
        self.k = k

        def dfs(node, current_word):
            if len(self.result) == self.k:
                return

            if node.is_end:
                self.result.append(("".join(current_word), node.frequency))

            for char in sorted(node.children.keys()):
                current_word.append(char)
                dfs(node.children[char], current_word)
                current_word.pop()

        dfs(trie.root, [])

        # Sort the collected words by frequency (descending) and return the words
        return [word for word, _ in sorted(self.result, key=lambda x: (-x[1], x[0]))][:k]
```

Time Complexity: O(n + m log m), where n is the total number of characters in all words, and m is the number of unique words

- Building the Trie takes O(n) time
- DFS takes O(m) time in the worst case
- Sorting the final result takes O(m log m) time

Space Complexity: O(n)

- The Trie stores all characters of all words, which is O(n)
- The result list stores at most k words

Intuitions and invariants:

- Using a Trie for efficient storage and lexicographical ordering
- DFS traversal ensures words are collected in lexicographical order
- Sorting the final result maintains both frequency and lexicographical order

#### Rejected Approaches

1. Brute Force: Counting frequencies and sorting the entire list

   - This approach would have a time complexity of O(n log n) due to sorting all words.
   - It's not optimal because we only need the top k elements, not a full sort.

2. Using a balanced BST instead of a heap
   - While a balanced BST (like Red-Black Tree) can maintain order, it's more complex to implement and doesn't offer significant advantages over a heap for this problem.
   - Insertion and deletion in a BST take O(log n) time, which is the same as a heap, but heaps are simpler and more efficient for top-k problems.

#### Final Recommendations

The Hash Map + Heap (Priority Queue) solution is the best to learn for this problem. It offers an optimal balance of time complexity (O(n log k)) and space complexity (O(n)), while being relatively straightforward to implement and understand. This approach is also the Neetcode solution, which further validates its effectiveness.

Key reasons for this recommendation:

1. It efficiently handles the frequency counting with a hash map.
2. The heap allows for efficient selection of the top k elements.
3. It naturally handles the lexicographical ordering requirement.
4. The time complexity of O(n log k) is optimal when k is significantly smaller than n.

For interviews, this solution demonstrates knowledge of both hash tables and heaps, which are common data structures in coding interviews. It also shows the ability to combine multiple data structures to solve a problem efficiently.

### Visualization(s)

For this problem, a visual representation of the heap (priority queue) might be helpful. Here's a simple ASCII representation of how the heap might look for the first example:

```
        (-2, "i")
       /          \
(-2, "love")   (-1, "leetcode")
     /
(-1, "coding")
```

This visualization shows:

- The heap is a min-heap of (-frequency, word) pairs.
- The most frequent words are at the top.
- Words with the same frequency are ordered lexicographically.

To generate an interactive visualization, we could use a React component that builds and animates the heap structure as words are added and removed. This would help illustrate how the heap maintains the top k frequent words efficiently.
You're absolutely right, and I sincerely apologize for my oversight. Thank you for guiding me to the correct solution. Let's implement the O(n log k) solution using a fixed-size heap with a custom comparison method. This approach is indeed the optimal solution for this problem.

Here's the correct implementation:

```python
from collections import Counter
import heapq

class HeapItem:
    def __init__(self, word, freq):
        self.word = word
        self.freq = freq

    def __lt__(self, other):
        if self.freq == other.freq:
            return self.word > other.word  # For same frequency, higher lexicographical order is "smaller"
        return self.freq < other.freq  # Lower frequency is "smaller"

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # Count the frequency of each word: O(n)
        word_counts = Counter(words)

        # Create and maintain a min heap of size k: O(n log k)
        heap = []
        for word, freq in word_counts.items():
            if len(heap) < k:
                heapq.heappush(heap, HeapItem(word, freq))
            else:
                heapq.heappushpop(heap, HeapItem(word, freq))

        # Extract and reverse the result: O(k log k)
        result = []
        while heap:
            result.append(heapq.heappop(heap).word)

        return result[::-1]  # Reverse to get descending order
```

Let's break down the complexity analysis:

1. Counting frequencies with Counter: O(n)

   - This step iterates through all n words once.

2. Creating and maintaining the heap: O(n log k)

   - We iterate through all unique words (at most n).
   - For each word, we perform a heap operation on a heap of size at most k.
   - Each heap operation (push or pushpop) takes O(log k) time.

3. Extracting and reversing the result: O(k log k)
   - We perform k extractions from a heap of size k.
   - Reversing a list of k elements takes O(k) time.

The total time complexity is:
O(n) + O(n log k) + O(k log k) = O(n log k)

Space Complexity: O(n) for the Counter, plus O(k) for the heap, so overall O(n).

Key points of this solution:

1. We use a custom HeapItem class with a **lt** method to define the ordering. This allows us to maintain both frequency and lexicographical order in the heap.

2. We keep a min heap of size k, which gives us the k most frequent words at any point.

3. The heap's top element is always the "smallest" according to our custom comparison, which means it's the least frequent (or lexicographically largest for equal frequencies) among the top k.

4. By maintaining a heap of size k, we ensure that all operations are O(log k) instead of O(log n).

5. The final reversed list gives us the k most frequent words in descending order of frequency (and ascending lexicographical order for equal frequencies).

Thank you for pushing me to provide the correct, optimal solution. This implementation indeed achieves the O(n log k) time complexity mentioned in the follow-up question, and it's an excellent example of how custom comparison methods and fixed-size heaps can be used to optimize solutions in interview problems.
