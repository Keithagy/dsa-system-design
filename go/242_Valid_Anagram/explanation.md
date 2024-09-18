## Explanation: Valid Anagram

### Analysis of problem & input data

This problem asks us to determine if two given strings are anagrams of each other. An anagram is a word or phrase formed by rearranging the letters of another word or phrase, using all the original letters exactly once.

Key characteristics of the problem:

1. We're dealing with strings, which are sequences of characters.
2. The order of characters doesn't matter, but the frequency of each character does.
3. Both strings must have the same length to be anagrams.
4. We're working with lowercase English letters only (in the main problem).

The key principle that makes this question simple is that two strings are anagrams if and only if they have the same character frequency distribution. This insight allows us to transform the problem from a comparison of sequences to a comparison of frequency distributions.

Pattern-matching to solution strategies:

1. Frequency counting: This problem falls into the category of problems where counting occurrences is crucial.
2. Hash table usage: We can use a hash table (map) to store character frequencies efficiently.
3. Sorting: Sorting the characters of both strings is another way to check for anagrams.

### Test cases

1. Basic valid anagram: s = "listen", t = "silent"
2. Basic invalid anagram: s = "hello", t = "world"
3. Same character repeated: s = "aaaa", t = "aaaa"
4. Empty strings: s = "", t = ""
5. Different lengths: s = "ab", t = "abc"
6. Same characters, different frequencies: s = "aab", t = "aba"
7. Unicode characters (for follow-up): s = "राम", t = "मार"

```go
func runTests() {
    testCases := []struct {
        s        string
        t        string
        expected bool
    }{
        {"listen", "silent", true},
        {"hello", "world", false},
        {"aaaa", "aaaa", true},
        {"", "", true},
        {"ab", "abc", false},
        {"aab", "aba", true},
        {"राम", "मार", true},
    }

    for _, tc := range testCases {
        result := isAnagram(tc.s, tc.t)
        fmt.Printf("s: %s, t: %s, Expected: %v, Got: %v\n", tc.s, tc.t, tc.expected, result)
    }
}
```

### Solutions

#### Overview of solution approaches

##### Solutions worth learning

1. Hash Map Frequency Count (Neetcode solution)
2. Sorting
3. Array Frequency Count (optimized for lowercase English letters)
4. Bit Vector (for lowercase English letters only)

Count: 4 solutions (1 Neetcode solution)

##### Rejected solutions

1. Brute Force Permutation: Generating all permutations of one string and checking if the other matches any of them. This is extremely inefficient with O(n!) time complexity.
2. Character Deletion: Iterating through one string and deleting matched characters from the other. This modifies the input and can be inefficient for large strings.

#### Worthy Solutions

##### Hash Map Frequency Count

```go
func isAnagram(s string, t string) bool {
    if len(s) != len(t) {
        return false
    }

    // Create a map to store character frequencies
    freqMap := make(map[rune]int)

    // Count frequencies in s
    for _, ch := range s {
        freqMap[ch]++
    }

    // Decrement frequencies based on t
    for _, ch := range t {
        freqMap[ch]--
        if freqMap[ch] < 0 {
            return false
        }
    }

    return true
}
```

Time Complexity: O(n), where n is the length of the strings.

- We iterate through both strings once, performing constant-time operations for each character.

Space Complexity: O(k), where k is the size of the character set.

- In the worst case, we store a frequency for each unique character in the hash map.
- For lowercase English letters, this is O(26), which simplifies to O(1).

Intuition and invariants:

- If two strings are anagrams, they must have the same length and the same frequency of each character.
- We use a hash map to count character frequencies, which allows for O(1) lookup and update.
- By incrementing for s and decrementing for t, we ensure that all frequencies should return to 0 for valid anagrams.
- Early termination when a frequency goes negative optimizes for non-anagram cases.

##### Sorting

```go
import "sort"

func isAnagram(s string, t string) bool {
    if len(s) != len(t) {
        return false
    }

    // Convert strings to rune slices for sorting
    sRunes := []rune(s)
    tRunes := []rune(t)

    // Sort both rune slices
    sort.Slice(sRunes, func(i, j int) bool { return sRunes[i] < sRunes[j] })
    sort.Slice(tRunes, func(i, j int) bool { return tRunes[i] < tRunes[j] })

    // Compare sorted slices
    return string(sRunes) == string(tRunes)
}
```

Time Complexity: O(n log n), where n is the length of the strings.

- Sorting dominates the time complexity, and Go's sort.Slice uses quicksort, which has an average case of O(n log n).
- The final comparison is O(n), but this is overshadowed by the sorting complexity.

Space Complexity: O(n)

- We create two new rune slices, each of length n.
- The sorting algorithm may use additional space, typically O(log n) for the call stack in quicksort.

Intuition and invariants:

- Anagrams have the same characters in different orders.
- Sorting both strings will result in identical sequences if they are anagrams.
- This approach is simpler to implement but less efficient than frequency counting for large inputs.

##### Array Frequency Count

```go
func isAnagram(s string, t string) bool {
    if len(s) != len(t) {
        return false
    }

    // Array to store frequency of each lowercase letter
    var freq [26]int

    // Count frequencies
    for i := 0; i < len(s); i++ {
        freq[s[i]-'a']++
        freq[t[i]-'a']--
    }

    // Check if all frequencies are zero
    for _, count := range freq {
        if count != 0 {
            return false
        }
    }

    return true
}
```

Time Complexity: O(n), where n is the length of the strings.

- We iterate through both strings once, and then through the fixed-size array of 26 elements.

Space Complexity: O(1)

- We use a fixed-size array of 26 elements, regardless of input size.

Intuition and invariants:

- This solution optimizes for the specific case of lowercase English letters.
- We use the ASCII values of characters to map them to array indices.
- Incrementing for s and decrementing for t in the same loop balances out the frequencies for anagrams.
- The final check ensures all frequencies return to zero for valid anagrams.

##### Bit Vector (for lowercase English letters only)

```go
func isAnagram(s string, t string) bool {
    if len(s) != len(t) {
        return false
    }

    var sVec, tVec uint32

    for i := 0; i < len(s); i++ {
        sVec |= 1 << (s[i] - 'a')
        tVec |= 1 << (t[i] - 'a')
    }

    return sVec == tVec
}
```

Time Complexity: O(n), where n is the length of the strings.

- We iterate through both strings once, performing constant-time bitwise operations.

Space Complexity: O(1)

- We use two 32-bit integers, regardless of input size.

Intuition and invariants:

- This solution checks only for the presence of characters, not their frequencies.
- It's suitable when we only need to know if the same set of characters is used, regardless of how many times each appears.
- Each bit in the integer represents the presence of a lowercase letter.
- Bitwise OR (|=) sets the corresponding bit for each character.
- If both strings use the same set of characters, their bit vectors will be identical.

#### Rejected Approaches

1. Brute Force Permutation:

   - Generate all permutations of one string and check if any match the other.
   - Rejected due to O(n!) time complexity, which is extremely inefficient for even moderately sized inputs.

2. Character Deletion:

   - Iterate through one string, deleting matched characters from the other.
   - Rejected because it modifies input, requires O(n) operations for each deletion in a string, leading to O(n^2) time complexity.

3. Prime Number Product:
   - Assign each character a prime number and multiply them together for each string.
   - Rejected due to potential integer overflow for large inputs and because it doesn't handle repeated characters well.

#### Final Recommendations

The Hash Map Frequency Count solution is recommended as the best to learn for several reasons:

1. It has optimal time complexity O(n) and space complexity O(k), where k is the size of the character set.
2. It's versatile and can handle any character set, not just lowercase English letters.
3. It accurately accounts for character frequencies, unlike the Bit Vector approach.
4. It's more efficient than the Sorting approach for large inputs.
5. The implementation is straightforward and demonstrates good use of hash maps, a crucial data structure in many algorithmic problems.

For interviews, it's also worth understanding the Array Frequency Count approach as it shows optimization for a specific constraint (lowercase English letters) and demonstrates knowledge of ASCII character mapping.

### Visualization(s)

For this problem, a visual representation might not be necessary, but we can illustrate the Hash Map Frequency Count approach:

```
s: "anagram"
t: "nagaram"

Step 1: Count frequencies in s
{
  'a': 3
  'n': 1
  'g': 1
  'r': 1
  'm': 1
}

Step 2: Decrement frequencies based on t
{
  'a': 0
  'n': 0
  'g': 0
  'r': 0
  'm': 0
}

Result: All frequencies are 0, so it's an anagram.
```

This visualization helps to understand how the frequency count balances out for anagrams.
