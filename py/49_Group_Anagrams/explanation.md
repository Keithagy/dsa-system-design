## Explanation: Group Anagrams

### Analysis of problem & input data

This problem is fundamentally about categorizing strings based on their character composition, regardless of the order of characters. The key observation is that anagrams are strings that have the same characters, just in a different order. This immediately suggests a strategy of finding a way to represent each string that is order-independent.

The input data consists of an array of strings, where each string contains only lowercase English letters. This is important because it limits the character set we need to consider, which can influence our choice of solution.

The problem fits into the category of string manipulation and hash table usage. The core principle that makes this question simple is that anagrams will have the same sorted string representation. Alternatively, they will have the same character count representation. This allows us to use either of these as a key in a hash table to group anagrams together efficiently.

### Test cases

1. Standard case:
   Input: ["eat","tea","tan","ate","nat","bat"]
   Expected Output: [["eat","tea","ate"],["tan","nat"],["bat"]]

2. Empty string:
   Input: [""]
   Expected Output: [[""]]

3. Single character:
   Input: ["a"]
   Expected Output: [["a"]]

4. All unique (no anagrams):
   Input: ["cat", "dog", "bird"]
   Expected Output: [["cat"], ["dog"], ["bird"]]

5. All same (all anagrams):
   Input: ["a", "a", "a"]
   Expected Output: [["a", "a", "a"]]

6. Mixed lengths:
   Input: ["abc", "cab", "day", "had", "bad"]
   Expected Output: [["abc", "cab"], ["day"], ["had"], ["bad"]]

Here's the Python code for these test cases:

```python
def test_group_anagrams(func):
    test_cases = [
        (["eat","tea","tan","ate","nat","bat"], [["eat","tea","ate"],["tan","nat"],["bat"]]),
        ([""], [[""]]),
        (["a"], [["a"]]),
        (["cat", "dog", "bird"], [["cat"], ["dog"], ["bird"]]),
        (["a", "a", "a"], [["a", "a", "a"]]),
        (["abc", "cab", "day", "had", "bad"], [["abc", "cab"], ["day"], ["had"], ["bad"]])
    ]

    for i, (input_strs, expected_output) in enumerate(test_cases):
        result = func(input_strs)
        if sorted(map(sorted, result)) == sorted(map(sorted, expected_output)):
            print(f"Test case {i+1} passed!")
        else:
            print(f"Test case {i+1} failed.")
            print(f"Input: {input_strs}")
            print(f"Expected: {expected_output}")
            print(f"Got: {result}")
    print("All test cases completed.")

# Usage:
# test_group_anagrams(group_anagrams)
```

### Solutions

#### Overview of solution approaches

##### Solutions worth learning

1. Sorted String as Key (Neetcode solution)
2. Character Count as Key
3. Prime Number Product as Key

Count: 3 solutions (1 Neetcode solution)

##### Rejected solutions

1. Brute Force Comparison: Comparing each string with every other string would be O(n^2 \* k) time complexity, where n is the number of strings and k is the average length of the strings. This is inefficient for large inputs.
2. Permutation Generation: Generating all permutations of each string to find matches would be extremely inefficient, with a time complexity of O(n \* k!), where k is the length of the strings.

#### Worthy Solutions

##### Sorted String as Key (Neetcode solution)

```python
from collections import defaultdict
from typing import List

def group_anagrams(strs: List[str]) -> List[List[str]]:
    anagram_groups = defaultdict(list)

    for s in strs:
        # Sort the string to create a unique key for all anagrams
        sorted_s = ''.join(sorted(s))
        # Add the original string to the list of anagrams with this sorted key
        anagram_groups[sorted_s].append(s)

    # Return the values (lists of anagrams) from the dictionary
    return list(anagram_groups.values())
```

Time Complexity: O(n \* k log k), where n is the number of strings and k is the maximum length of a string. This is because we iterate through each of the n strings (O(n)) and sort each string (O(k log k)).

Space Complexity: O(n \* k), as in the worst case, we store all strings in our dictionary.

- The key insight is that anagrams will have the same sorted string representation.
- Using a defaultdict allows us to automatically create a new list when we encounter a new sorted string key, simplifying our code.
- By sorting each string, we create a unique identifier for each group of anagrams, which becomes the key in our hash table.
- The final step of returning the values of the dictionary gives us the grouped anagrams.

##### Character Count as Key

```python
from collections import defaultdict
from typing import List

def group_anagrams(strs: List[str]) -> List[List[str]]:
    anagram_groups = defaultdict(list)

    for s in strs:
        # Create a count array for lowercase English letters
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1

        # Use the count array as a tuple (immutable) for the dictionary key
        anagram_groups[tuple(count)].append(s)

    return list(anagram_groups.values())
```

Time Complexity: O(n \* k), where n is the number of strings and k is the maximum length of a string. We iterate through each character of each string once.

Space Complexity: O(n \* 26) = O(n), as we store a count array for each unique anagram group, and the count array has a fixed size of 26.

- This solution leverages the fact that anagrams will have the same character count.
- By using a fixed-size array to count characters, we avoid the need for sorting.
- The count array serves as a unique identifier for each anagram group.
- This approach is particularly efficient when the strings are long but consist of a limited character set (in this case, lowercase English letters).

##### Prime Number Product as Key

```python
from collections import defaultdict
from typing import List

def group_anagrams(strs: List[str]) -> List[List[str]]:
    # First 26 prime numbers for a-z
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
    anagram_groups = defaultdict(list)

    for s in strs:
        key = 1
        for c in s:
            key *= primes[ord(c) - ord('a')]
        anagram_groups[key].append(s)

    return list(anagram_groups.values())
```

Time Complexity: O(n \* k), where n is the number of strings and k is the maximum length of a string. We iterate through each character of each string once.

Space Complexity: O(n), as we store the grouped anagrams.

- This solution assigns a unique prime number to each letter and uses the product of these primes as the key.
- The fundamental theorem of arithmetic guarantees that this product will be unique for each anagram group.
- This method avoids sorting and provides a single integer key, which can be more efficient in some scenarios.
- However, for very long strings, there's a risk of integer overflow, which is a limitation of this approach.

#### Rejected Approaches

1. Brute Force Comparison: This approach would compare each string with every other string to check if they are anagrams. It's rejected because its O(n^2 \* k) time complexity is inefficient for large inputs.

2. Permutation Generation: Generating all permutations of each string to find matches would be extremely inefficient, with a time complexity of O(n \* k!). This approach is entirely impractical for strings longer than a few characters.

#### Final Recommendations

The Character Count as Key solution is recommended as the best to learn. It offers a good balance of efficiency (O(n \* k) time complexity) and simplicity. It avoids the need for sorting, making it faster than the Sorted String approach for longer strings. It's also more intuitive and less prone to errors than the Prime Number Product approach, which could suffer from integer overflow for very long strings.

The Sorted String approach is a close second and is worth learning due to its simplicity and wide applicability. It's particularly good for interview situations where you need to quickly implement a working solution.

The Prime Number Product approach, while clever, is less practical due to potential overflow issues and is more of an interesting theoretical solution than one you'd use in practice.

### Visualization(s)

For this problem, a visual representation of how strings are grouped can be helpful. Here's a simple ASCII art visualization of the Character Count as Key approach:

```
Input: ["eat", "tea", "tan", "ate", "nat", "bat"]

Character Counts:
"eat" -> [1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0]
"tea" -> [1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0]
"tan" -> [1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0]
"ate" -> [1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0]
"nat" -> [1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0]
"bat" -> [1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0]

Grouped Anagrams:
[1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0] -> ["eat", "tea", "ate"]
[1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0] -> ["tan", "nat"]
[1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0] -> ["bat"]

Output: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
```

This visualization shows how the character count serves as a unique identifier for each group of anagrams, allowing us to efficiently group the strings without needing to sort them.
