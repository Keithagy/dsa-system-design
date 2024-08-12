# Explanation: Implement Trie (Prefix Tree)

## Analysis of problem & input data

This problem is about implementing a Trie, also known as a prefix tree. The key aspects of this problem are:

1. Data Structure: The core of this problem is understanding and implementing the Trie data structure.
2. String Operations: All operations involve manipulating and searching strings.
3. Prefix Matching: The Trie is particularly efficient for prefix matching operations.
4. Character Set: The input is constrained to lowercase English letters, which simplifies our implementation.
5. Multiple Operations: We need to implement insert, search, and prefix search operations.

Key principles that make this question manageable:

- A Trie node typically represents a single character.
- Each node can have multiple children (up to 26 in this case, for each lowercase letter).
- The path from the root to a node forms a prefix of the inserted words.
- End-of-word markers are crucial for distinguishing between prefixes and complete words.

### Test cases

Here are some test cases to consider:

1. Basic functionality:

   - Insert "apple" and search for "apple" (should return True)
   - Search for "app" (should return False)
   - Check if "app" is a prefix (should return True)

2. Empty string:

   - Insert "" and search for "" (implementation-dependent)
   - Check if "" is a prefix (should return True)

3. Overlapping words:

   - Insert "app" and "apple"
   - Search for both "app" and "apple" (both should return True)

4. Non-existent words:

   - Search for "appl" after inserting "apple" (should return False)
   - Check if "b" is a prefix after inserting "apple" (should return False)

5. Case sensitivity:
   - Insert "Apple" and search for "apple" (should return False due to case mismatch)

Here's the Python code for these test cases:

```python
def run_tests(trie):
    # Test case 1: Basic functionality
    trie.insert("apple")
    assert trie.search("apple") == True
    assert trie.search("app") == False
    assert trie.startsWith("app") == True

    # Test case 2: Empty string (implementation-dependent)
    trie.insert("")
    assert trie.search("") == True  # Assuming empty string is valid
    assert trie.startsWith("") == True

    # Test case 3: Overlapping words
    trie.insert("app")
    assert trie.search("app") == True
    assert trie.search("apple") == True

    # Test case 4: Non-existent words
    assert trie.search("appl") == False
    assert trie.startsWith("b") == False

    # Test case 5: Case sensitivity
    trie.insert("Apple")
    assert trie.search("apple") == True  # "apple" was inserted before
    assert trie.search("Apple") == True

    print("All tests passed!")

# Run the tests after implementing the Trie class
trie = Trie()
run_tests(trie)
```

## Solutions

### Overview of solution approaches

#### Solutions worth learning

1. Array-based Trie implementation
2. Dictionary-based Trie implementation

Count: 2 solutions

#### Rejected solutions

1. Using a simple list or set to store words
2. Using a hash table (dictionary) to store all prefixes

### Worthy Solutions

#### 1. Array-based Trie implementation

```python
class TrieNode:
    def __init__(self):
        self.children = [None] * 26  # Array for lowercase English letters
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            index = ord(char) - ord('a')
            if not node.children[index]:
                node.children[index] = TrieNode()
            node = node.children[index]
        node.is_end_of_word = True

    def search(self, word: str) -> bool:
        node = self._find_node(word)
        return node is not None and node.is_end_of_word

    def startsWith(self, prefix: str) -> bool:
        return self._find_node(prefix) is not None

    def _find_node(self, prefix: str) -> TrieNode:
        node = self.root
        for char in prefix:
            index = ord(char) - ord('a')
            if not node.children[index]:
                return None
            node = node.children[index]
        return node
```

Time complexity:

- Insert: O(m), where m is the length of the word
- Search: O(m), where m is the length of the word
- StartsWith: O(m), where m is the length of the prefix

Space complexity:

- O(n \* m), where n is the number of words and m is the average length of words

Intuitions and invariants:

- Each node represents a character in the trie
- The path from the root to any node represents a prefix
- The is_end_of_word flag marks complete words
- Using an array for children provides constant-time access to child nodes

#### 2. Dictionary-based Trie implementation

```python
class TrieNode:
    def __init__(self):
        self.children = {}  # Dictionary to store child nodes
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word: str) -> bool:
        node = self._find_node(word)
        return node is not None and node.is_end_of_word

    def startsWith(self, prefix: str) -> bool:
        return self._find_node(prefix) is not None

    def _find_node(self, prefix: str) -> TrieNode:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return None
            node = node.children[char]
        return node
```

Time complexity:

- Insert: O(m), where m is the length of the word
- Search: O(m), where m is the length of the word
- StartsWith: O(m), where m is the length of the prefix

Space complexity:

- O(n \* m), where n is the number of words and m is the average length of words

Intuitions and invariants:

- Each node represents a character in the trie
- The path from the root to any node represents a prefix
- The is_end_of_word flag marks complete words
- Using a dictionary for children provides flexibility for different character sets

### Rejected Approaches

1. Using a simple list or set to store words:

   - This approach would be inefficient for prefix matching operations.
   - Time complexity for startsWith would be O(n\*m) where n is the number of words and m is the average word length.

2. Using a hash table (dictionary) to store all prefixes:
   - While this could provide O(1) lookup for both words and prefixes, it would consume excessive memory.
   - For each word of length m, we would store m prefixes, leading to a space complexity of O(n\*m^2) where n is the number of words.

### Final Recommendations

The array-based Trie implementation (Solution 1) is recommended for learning and use in interview settings. Here's why:

1. Efficiency: It provides O(m) time complexity for all operations, where m is the length of the word or prefix.
2. Memory usage: It's more memory-efficient than storing all possible prefixes.
3. Simplicity: The array-based approach is straightforward to implement and explain.
4. Optimization: For the given constraint of lowercase English letters, using an array of size 26 is optimal.

The dictionary-based implementation is also correct and worth knowing, especially for scenarios where the character set is unknown or large. However, for this specific problem with a known, limited character set, the array-based approach is more efficient.

Approaches like using a list or set of words, or a hash table of all prefixes, while potentially simpler to implement, do not demonstrate understanding of the Trie data structure and its benefits. They would also be less efficient for prefix matching operations, which is a key aspect of this problem.

## Visualization(s)

Here's a simple visualization of how the Trie would look after inserting the words "app" and "apple":

```
       root
        |
        a
        |
        p
        |
        p*
       /
      l
      |
      e*

* indicates end of word
```

This visualization shows how the Trie efficiently stores overlapping prefixes and distinguishes between complete words and prefixes. The nodes marked with \* represent the end of a word, corresponding to the `is_end_of_word` flag in our implementation.
