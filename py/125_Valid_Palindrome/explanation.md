# Explanation: Valid Palindrome

## Analysis of problem & input data

The "Valid Palindrome" problem is a classic string manipulation and two-pointer technique question. Here are the key aspects of the problem:

1. **String Preprocessing**: The problem requires converting uppercase letters to lowercase and removing non-alphanumeric characters. This preprocessing step is crucial before checking for palindrome property.

2. **Palindrome Definition**: After preprocessing, the string should read the same forward and backward to be considered a palindrome.

3. **Input Characteristics**:

   - The input string can contain uppercase and lowercase letters, numbers, and special characters.
   - The string length can vary from 1 to 2 \* 10^5 characters.
   - The string consists only of printable ASCII characters.

4. **Edge Cases**:

   - Empty string after preprocessing (e.g., " " or ".,")
   - Single character strings
   - Strings with all non-alphanumeric characters

5. **Key Principle**: The core of this problem lies in comparing characters from both ends of the preprocessed string, moving towards the center. If at any point the characters don't match, it's not a palindrome.

### Test cases

Here are some test cases to cover various scenarios:

1. Normal case: "A man, a plan, a canal: Panama" (true)
2. Normal case with numbers: "12321" (true)
3. False case: "race a car" (false)
4. Empty string: " " (true)
5. Single character: "a" (true)
6. All non-alphanumeric: ".,?" (true)
7. Mixed case: "AbBa" (true)
8. Long string: "a" _100000 + "b" + "a"_ 100000 (false)

Here's the Python code for these test cases:

```python
def is_palindrome(s: str) -> bool:
    # Implementation will be added later
    pass

# Test cases
test_cases = [
    ("A man, a plan, a canal: Panama", True),
    ("12321", True),
    ("race a car", False),
    (" ", True),
    ("a", True),
    (".,?", True),
    ("AbBa", True),
    ("a" * 100000 + "b" + "a" * 100000, False)
]

for i, (input_str, expected) in enumerate(test_cases, 1):
    result = is_palindrome(input_str)
    print(f"Test case {i}: {'Passed' if result == expected else 'Failed'}")
    if result != expected:
        print(f"  Input: {input_str}")
        print(f"  Expected: {expected}, Got: {result}")
```

## Solutions

### Overview of solution approaches

#### Solutions worth learning

1. Two-pointer approach with in-place character comparison
2. Two-pointer approach with preprocessed string
3. Recursive approach
4. Built-in functions approach

Count: 4 solutions

#### Rejected solutions

1. Reversing the entire string
2. Using a stack or queue data structure

### Worthy Solutions

#### 1. Two-pointer approach with in-place character comparison

This approach is the most efficient in terms of both time and space complexity.

```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left < right:
            # Move left pointer to the next alphanumeric character
            while left < right and not s[left].isalnum():
                left += 1

            # Move right pointer to the previous alphanumeric character
            while left < right and not s[right].isalnum():
                right -= 1

            # Compare characters, ignoring case
            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True
```

Time Complexity: O(n), where n is the length of the string
Space Complexity: O(1), as we're using constant extra space

Intuition and invariants:

- We use two pointers, one starting from the beginning (left) and one from the end (right) of the string.
- We skip non-alphanumeric characters as they don't contribute to the palindrome property.
- We compare characters case-insensitively.
- The invariant is that at each step, we've verified that all characters up to the current pointers form a palindrome.
- If we reach the point where left >= right, we've checked all characters and confirmed it's a palindrome.

#### 2. Two-pointer approach with preprocessed string

This approach preprocesses the string first, which can be beneficial for readability and when multiple operations need to be performed on the cleaned string.

```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Preprocess the string
        cleaned = ''.join(char.lower() for char in s if char.isalnum())

        # Use two pointers to check for palindrome
        left, right = 0, len(cleaned) - 1
        while left < right:
            if cleaned[left] != cleaned[right]:
                return False
            left += 1
            right -= 1

        return True
```

Time Complexity: O(n), where n is the length of the string
Space Complexity: O(n), as we create a new string

Intuition and invariants:

- We first create a cleaned version of the string, removing non-alphanumeric characters and converting to lowercase.
- The two-pointer approach on the cleaned string is straightforward, as we don't need to skip characters or handle case sensitivity.
- The invariant is the same as in the first approach, but applied to the cleaned string.

#### 3. Recursive approach

While not the most efficient, this approach demonstrates a different way of thinking about the problem.

```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        def clean_string(s: str) -> str:
            return ''.join(char.lower() for char in s if char.isalnum())

        def is_palindrome_recursive(s: str, left: int, right: int) -> bool:
            if left >= right:
                return True
            if s[left] != s[right]:
                return False
            return is_palindrome_recursive(s, left + 1, right - 1)

        cleaned = clean_string(s)
        return is_palindrome_recursive(cleaned, 0, len(cleaned) - 1)
```

Time Complexity: O(n), where n is the length of the string
Space Complexity: O(n) for the cleaned string, plus O(n) for the call stack in the worst case

Intuition and invariants:

- We first clean the string similar to approach 2.
- The recursive function checks the outermost characters and then calls itself on the inner substring.
- The base case is when we've checked all characters (left >= right).
- The invariant is that at each recursive call, we've verified that the outer characters match.

#### 4. Built-in functions approach

This approach leverages Python's built-in functions for a concise solution.

```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ''.join(filter(str.isalnum, s)).lower()
        return cleaned == cleaned[::-1]
```

Time Complexity: O(n), where n is the length of the string
Space Complexity: O(n) for the cleaned string and its reverse

Intuition and invariants:

- We use `filter()` and `str.isalnum` to remove non-alphanumeric characters.
- `lower()` converts the string to lowercase.
- We then compare the cleaned string with its reverse.
- While concise, this approach may be less efficient due to creating two copies of the cleaned string.

### Rejected Approaches

1. **Reversing the entire string**: While it might seem intuitive to reverse the entire string and compare, this is less efficient than the two-pointer approach. It requires O(n) extra space and doesn't allow for early termination if a mismatch is found.

2. **Using a stack or queue**: Some might consider using a stack to push characters from the first half of the string and then compare with the second half. However, this adds unnecessary complexity and extra space usage compared to the two-pointer approach.

### Final Recommendations

The two-pointer approach with in-place character comparison (Solution 1) is the best to learn and use in an interview setting. It has the following advantages:

1. Optimal time complexity (O(n))
2. Optimal space complexity (O(1))
3. Demonstrates ability to handle string manipulation without relying on built-in functions
4. Shows understanding of two-pointer technique
5. Handles the problem requirements (case insensitivity, ignoring non-alphanumeric characters) elegantly

The other approaches, while valid, have drawbacks:

- Solution 2 uses extra space for the cleaned string
- Solution 3 (recursive) has potential stack overflow issues for very long strings and is less intuitive
- Solution 4, while concise, might be seen as relying too heavily on Python's built-in functions in an interview setting

In an interview, it's good to mention these alternative approaches to demonstrate breadth of knowledge, but implement the two-pointer in-place solution as the primary answer.

## Visualization(s)

For the recommended two-pointer approach, a simple visualization can help understand the algorithm:

```
Input: "A man, a plan, a canal: Panama"

Step 1:   A m a n, a  p l a n,  a   c a  n  a  l  :   P  a  n  a  m  a
         ↑                                                          ↑
        left                                                      right

Step 2:   A m a n, a  p l a n,  a   c a  n  a  l  :   P  a  n  a  m  a
           ↑                                                      ↑
          left                                                  right

...

Final:   A m a n, a  p l a n,  a   c a  n  a  l  :   P  a  n  a  m  a
                            ↑↑
                          left right

Result: True (palindrome)
```

This visualization shows how the two pointers move towards each other, skipping non-alphanumeric characters and comparing the valid characters until they meet in the middle or a mismatch is found.
