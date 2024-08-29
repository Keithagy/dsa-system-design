## Explanation: Design Add and Search Words Data Structure

### Analysis of problem & input data

This problem is a classic example of a trie (prefix tree) application with a twist - the search functionality needs to handle wildcard characters (dots). The key characteristics of the problem that guide us towards a trie-based solution are:

1. We need to efficiently store and search for words.
2. The search operation involves pattern matching, where '.' can match any character.
3. The words consist only of lowercase English letters, which limits our alphabet size to 26.
4. The maximum word length is 25, which is relatively small.
5. The number of calls to addWord and search can be up to 10^4, suggesting we need an efficient data structure.

The principle that makes this question simple is understanding that a trie can be traversed character by character, making it perfect for pattern matching. The dot wildcard simply means we need to explore all possible paths at that level of the trie.

### Test cases

Here are some relevant test cases:

1. Basic functionality:

   - Add "cat", "car", "dog"
   - Search "cat" (true)
   - Search "car" (true)
   - Search "cot" (false)

2. Wildcard searches:

   - Search "c.t" (true)
   - Search "c.." (true)
   - Search ".at" (true)
   - Search "..." (true)

3. Edge cases:

   - Empty string: Add "" and search ""
   - Single character: Add "a" and search "."
   - All wildcards: Search "....." (assuming we've added some 5-letter words)
   - No wildcards: Search "abcde" (assuming we've added "abcde")

4. Tricky cases:
   - Add "a", search "a." (false)
   - Add "a", search ".a" (false)

Here's the Python code for these test cases:

```python
def test_word_dictionary():
    wd = WordDictionary()

    # Basic functionality
    wd.addWord("cat")
    wd.addWord("car")
    wd.addWord("dog")
    assert wd.search("cat") == True
    assert wd.search("car") == True
    assert wd.search("cot") == False

    # Wildcard searches
    assert wd.search("c.t") == True
    assert wd.search("c..") == True
    assert wd.search(".at") == True
    assert wd.search("...") == True

    # Edge cases
    wd.addWord("")
    assert wd.search("") == True
    wd.addWord("a")
    assert wd.search(".") == True
    wd.addWord("abcde")
    assert wd.search(".....") == True
    assert wd.search("abcde") == True

    # Tricky cases
    assert wd.search("a.") == False
    assert wd.search(".a") == False

    print("All tests passed!")

test_word_dictionary()
```

### Solutions

#### Overview of solution approaches

##### Solutions worth learning

1. Trie with DFS for search (Neetcode solution)
2. Trie with BFS for search
3. HashMap of word lengths with lists

Count: 3 solutions (1 Neetcode solution)

##### Rejected solutions

1. Simple list or set of words: While easy to implement, this would be inefficient for searching, especially with wildcards.
2. Regular expressions: Although they can handle wildcards, building and compiling regex for each search would be inefficient.

#### Worthy Solutions

##### Trie with DFS for search (Neetcode solution)

```python
class TrieNode:
    def __init__(self):
        self.children = {}  # Map each character to a TrieNode
        self.is_word = False  # Flag to mark end of a word

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_word = True

    def search(self, word: str) -> bool:
        def dfs(node, index):
            if index == len(word):
                return node.is_word

            if word[index] == '.':
                for child in node.children.values():
                    if dfs(child, index + 1):
                        return True
            else:
                if word[index] in node.children:
                    return dfs(node.children[word[index]], index + 1)

            return False

        return dfs(self.root, 0)
```

Time Complexity:

- addWord: O(L), where L is the length of the word. We traverse the trie once for each character.
- search: O(26^M), where M is the number of dots in the search word. In the worst case (all dots), we explore all possible paths.

Space Complexity:

- O(N), where N is the total number of characters in all added words. In the worst case, we store each character as a separate node.

Intuitions and invariants:

- The trie structure allows efficient prefix matching.
- Each node in the trie represents a character in a word.
- The is_word flag marks the end of complete words.
- DFS allows us to explore all possible paths when encountering a dot.
- The search terminates early if a mismatch is found.

##### Trie with BFS for search

```python
from collections import deque

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_word = True

    def search(self, word: str) -> bool:
        queue = deque([(self.root, 0)])
        while queue:
            node, index = queue.popleft()
            if index == len(word):
                if node.is_word:
                    return True
            elif word[index] == '.':
                for child in node.children.values():
                    queue.append((child, index + 1))
            elif word[index] in node.children:
                queue.append((node.children[word[index]], index + 1))
        return False
```

Time Complexity:

- addWord: O(L), where L is the length of the word. We traverse the trie once for each character.
- search: O(26^M), where M is the number of dots in the search word. In the worst case (all dots), we explore all possible paths.

Space Complexity:

- O(N), where N is the total number of characters in all added words. In the worst case, we store each character as a separate node.

Intuitions and invariants:

- The trie structure remains the same as in the DFS approach.
- BFS explores the trie level by level, which can be more efficient for shorter matches.
- The queue stores (node, index) pairs to keep track of the search progress.
- Early termination occurs when a full match is found.

##### HashMap of word lengths with lists

```python
from collections import defaultdict

class WordDictionary:
    def __init__(self):
        self.word_dict = defaultdict(list)

    def addWord(self, word: str) -> None:
        self.word_dict[len(word)].append(word)

    def search(self, word: str) -> bool:
        if '.' not in word:
            return word in self.word_dict[len(word)]

        for candidate in self.word_dict[len(word)]:
            if all(w == '.' or w == c for w, c in zip(word, candidate)):
                return True
        return False
```

Time Complexity:

- addWord: O(1), as we're just appending to a list.
- search: O(N \* L), where N is the number of words of the same length as the search word, and L is the length of the word. In the worst case, we compare each character of each word.

Space Complexity:

- O(M), where M is the total number of characters in all added words.

Intuitions and invariants:

- Grouping words by length allows us to quickly filter out irrelevant words.
- For exact matches, we can do a simple lookup in the list.
- For wildcard searches, we only need to compare with words of the same length.
- The `all()` function with `zip()` allows for efficient character-by-character comparison.

#### Rejected Approaches

1. Simple list or set of words:
   While this approach would work for exact matches, it would be highly inefficient for wildcard searches. We would need to check every word against the pattern, resulting in O(N \* L) time complexity for each search, where N is the total number of words and L is the average word length.

2. Regular expressions:
   Although regular expressions can handle wildcards easily, compiling a new regex for each search query would be inefficient. Additionally, the performance of regex matching can be unpredictable and potentially slow for complex patterns.

3. HashMap without length grouping:
   Storing all words in a single HashMap without grouping by length would still require checking every word for wildcard searches, leading to poor performance.

#### Final Recommendations

The Trie with DFS for search (Neetcode solution) is the best approach to learn for this problem. Here's why:

1. Efficiency: It provides O(L) time complexity for adding words and handles wildcard searches efficiently.
2. Scalability: It performs well even with a large number of words, as it doesn't need to check every word for each search.
3. Memory usage: While it uses more memory than a simple list approach, it's still efficient and scales well with the number of words.
4. Flexibility: The trie structure can be easily extended for other string-related problems, making it a valuable data structure to master.
5. Interview performance: Implementing a trie demonstrates a strong understanding of advanced data structures, which is highly valued in technical interviews.

The BFS approach is a good alternative to understand, as it showcases a different traversal method. The HashMap solution, while less efficient, is worth knowing as a simpler alternative that could be useful in scenarios with fewer words or where memory is a primary concern.

### Visualization(s)

For a visual representation of the trie structure, consider the following ASCII art diagram:

```
       root
    /    |     \
   c     d      m
  / \     \      \
 a   a     a      a
 |   |     |      |
 t   r     d      d
```

This represents the trie after adding "cat", "car", "dad", and "mad". Each node represents a character, and the paths from root to leaf nodes form complete words. The search process would traverse this structure, exploring multiple paths when encountering a dot.
