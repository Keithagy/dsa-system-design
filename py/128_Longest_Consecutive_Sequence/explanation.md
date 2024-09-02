## Explanation: Longest Consecutive Sequence

### Analysis of problem & input data

This problem presents us with an unsorted array of integers and asks us to find the length of the longest consecutive sequence of elements. The key aspects to consider are:

1. The array is unsorted, which means we can't rely on the order of elements as given.
2. We need to find consecutive elements, meaning numbers that follow each other sequentially (like 1, 2, 3, 4).
3. The sequence doesn't need to be contiguous in the original array.
4. The time complexity requirement is O(n), which rules out sorting-based solutions.
5. The array can contain duplicates, as seen in Example 2.
6. The array can be empty, as per the constraints.

The key principle that makes this question simple is the realization that we can use a hash set to achieve O(1) lookup time for each number. This allows us to efficiently check for the presence of consecutive numbers without sorting the array.

The pattern-matching here leads us to consider hash-based solutions, as they often provide O(1) lookup time which is crucial for meeting the O(n) time complexity requirement. This problem falls into the category of "array manipulation with optimal time complexity", which often involves using additional data structures (like hash sets or hash maps) to trade space for time.

### Test cases

1. Empty array: `[]` (Edge case)
2. Array with one element: `[1]`
3. Array with all identical elements: `[5, 5, 5, 5]`
4. Array with no consecutive sequences: `[2, 4, 6, 8]`
5. Array with multiple sequences of same length: `[1, 2, 3, 100, 101, 102]`
6. Array with negative numbers: `[-1, -3, -2, -4, 0, 1]`
7. Array with large range of numbers: `[1000000, -1000000, 0, 1, 2, 3]`
8. Example 1: `[100, 4, 200, 1, 3, 2]`
9. Example 2: `[0, 3, 7, 2, 5, 8, 4, 6, 0, 1]`

Here's the Python code for these test cases:

```python
def longest_consecutive(nums):
    # Implementation will go here
    pass

test_cases = [
    [],
    [1],
    [5, 5, 5, 5],
    [2, 4, 6, 8],
    [1, 2, 3, 100, 101, 102],
    [-1, -3, -2, -4, 0, 1],
    [1000000, -1000000, 0, 1, 2, 3],
    [100, 4, 200, 1, 3, 2],
    [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
]

for i, case in enumerate(test_cases, 1):
    result = longest_consecutive(case)
    print(f"Test case {i}: {case}")
    print(f"Result: {result}\n")
```

### Solutions

#### Overview of solution approaches

##### Solutions worth learning

1. Hash Set Approach (Neetcode solution)
2. Union-Find (Disjoint Set) Approach
3. Dynamic Programming Approach

Count: 3 solutions (1 Neetcode solution)

##### Rejected solutions

1. Sorting-based approach: This would give us O(n log n) time complexity, which doesn't meet the O(n) requirement.
2. Brute force approach: Checking every possible sequence would result in O(n^2) time complexity, which is too slow.

#### Worthy Solutions

##### Hash Set Approach (Neetcode solution)

```python
from typing import List

def longestConsecutive(nums: List[int]) -> int:
    num_set = set(nums)  # Convert list to set for O(1) lookup
    longest = 0

    for num in num_set:
        # Check if this is the start of a sequence
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1

            # Extend the sequence as far as possible
            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1

            longest = max(longest, current_streak)

    return longest
```

Time Complexity: O(n)

- We iterate through the array once to create the set: O(n)
- We then iterate through each number in the set: O(n)
- For each number, we might check consecutive numbers, but each number is checked at most twice (once as a sequence start, once as a sequence member): O(n)
- Total: O(n) + O(n) + O(n) = O(n)

Space Complexity: O(n)

- We store all numbers in a set, which in the worst case (all unique numbers) will be of size n.

Intuitions and invariants:

- By using a set, we achieve O(1) lookup time for each number.
- We only need to check for the start of a sequence (where num - 1 is not in the set), avoiding redundant checks.
- For each sequence start, we extend the sequence as far as possible.
- The longest sequence found is always maintained and updated.

##### Union-Find (Disjoint Set) Approach

```python
from typing import List

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.size = [1] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return
        if self.rank[px] < self.rank[py]:
            self.parent[px] = py
            self.size[py] += self.size[px]
        elif self.rank[px] > self.rank[py]:
            self.parent[py] = px
            self.size[px] += self.size[py]
        else:
            self.parent[py] = px
            self.rank[px] += 1
            self.size[px] += self.size[py]

def longestConsecutive(nums: List[int]) -> int:
    if not nums:
        return 0

    # Map each number to an index
    num_index = {num: i for i, num in enumerate(nums)}
    uf = UnionFind(len(nums))

    for num in nums:
        if num + 1 in num_index:
            uf.union(num_index[num], num_index[num + 1])

    return max(uf.size)
```

Time Complexity: O(n \* α(n)), where α is the inverse Ackermann function

- Creating the num_index dictionary: O(n)
- Initializing UnionFind: O(n)
- Iterating through nums and performing union operations: O(n \* α(n))
- The inverse Ackermann function α(n) grows very slowly and is effectively constant for all practical values of n, so this is effectively O(n)

Space Complexity: O(n)

- The UnionFind data structure uses O(n) space
- The num_index dictionary uses O(n) space

Intuitions and invariants:

- We use Union-Find to group consecutive numbers together.
- Each number is initially in its own set.
- We union a number with its consecutive next number if it exists.
- The size of the largest set at the end gives us the length of the longest consecutive sequence.

##### Dynamic Programming Approach

```python
from typing import List

def longestConsecutive(nums: List[int]) -> int:
    if not nums:
        return 0

    num_dict = {}
    max_length = 0

    for num in nums:
        if num not in num_dict:
            left = num_dict.get(num - 1, 0)
            right = num_dict.get(num + 1, 0)

            current_length = left + right + 1
            max_length = max(max_length, current_length)

            # Update the length for the current number and its boundaries
            num_dict[num] = current_length
            num_dict[num - left] = current_length
            num_dict[num + right] = current_length

    return max_length
```

Time Complexity: O(n)

- We iterate through the array once: O(n)
- Each dictionary operation (get and set) is O(1) on average
- Total: O(n)

Space Complexity: O(n)

- In the worst case, we store all numbers in the dictionary

Intuitions and invariants:

- We use a dictionary to store the length of the sequence for each number.
- For each number, we check if its left and right neighbors exist in the dictionary.
- We update the length for the current number and its sequence boundaries.
- The maximum length is updated with each new number processed.

#### Rejected Approaches

1. Sorting-based approach: While sorting the array would make it easy to find consecutive sequences, it would result in O(n log n) time complexity, which doesn't meet the problem's requirement of O(n) time.

2. Brute force approach: Checking every possible sequence by iterating through the array for each number would result in O(n^2) time complexity, which is too slow for large inputs.

3. Binary Search Tree (BST) approach: While a BST could be used to maintain a sorted order of numbers, constructing and querying the BST would result in O(n log n) time complexity in the average case, which doesn't meet the O(n) requirement.

#### Final Recommendations

The Hash Set Approach (Neetcode solution) is the best solution to learn for this problem. Here's why:

1. Time and Space Efficiency: It meets the O(n) time complexity requirement while using O(n) space, which is optimal for this problem.

2. Simplicity: It's straightforward to understand and implement, making it easier to explain in an interview setting.

3. Intuitive: The logic behind checking for the start of a sequence and then extending it is clear and intuitive.

4. No complex data structures: Unlike the Union-Find approach, it doesn't require implementing a separate data structure.

5. Widely applicable: The concept of using a hash set for O(1) lookups is a common pattern in many algorithmic problems.

While the Union-Find and Dynamic Programming approaches are interesting and worth understanding, they are more complex and might be harder to implement correctly under interview pressure. The Hash Set approach strikes the best balance between efficiency, simplicity, and demonstrating problem-solving skills.

### Visualization(s)

For the Hash Set Approach, we can visualize the process using a simple HTML/JavaScript implementation. Here's an artifact that demonstrates this:

```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Longest Consecutive Sequence Visualization</title>
    <style>
      body {
        font-family: Arial, sans-serif;
        display: flex;
        flex-direction: column;
        align-items: center;
        padding: 20px;
      }
      #inputArray,
      #output {
        margin: 10px 0;
        font-size: 18px;
      }
      #visualization {
        display: flex;
        flex-wrap: wrap;
        gap: 10px;
        margin-top: 20px;
      }
      .number {
        width: 40px;
        height: 40px;
        display: flex;
        justify-content: center;
        align-items: center;
        border: 1px solid #ccc;
        border-radius: 5px;
      }
      .highlight {
        background-color: #ffff00;
      }
      .sequence {
        background-color: #90ee90;
      }
    </style>
  </head>
  <body>
    <h1>Longest Consecutive Sequence Visualization</h1>
    <div id="inputArray"></div>
    <div id="visualization"></div>
    <div id="output"></div>

    <script>
      function longestConsecutive(nums) {
        const numSet = new Set(nums);
        let longest = 0;
        const visualizationDiv = document.getElementById("visualization");

        for (const num of numSet) {
          if (!numSet.has(num - 1)) {
            let currentNum = num;
            let currentStreak = 1;

            while (numSet.has(currentNum + 1)) {
              currentNum++;
              currentStreak++;
            }

            // Highlight the sequence
            for (let i = num; i <= currentNum; i++) {
              const numElement = document.querySelector(
                `.number[data-value="${i}"]`,
              );
              if (numElement) {
                numElement.classList.add("sequence");
              }
            }

            longest = Math.max(longest, currentStreak);
          }
        }

        return longest;
      }

      const nums = [100, 4, 200, 1, 3, 2];
      document.getElementById("inputArray").textContent =
        `Input Array: [${nums.join(", ")}]`;

      // Create number elements
      const visualizationDiv = document.getElementById("visualization");
      nums.forEach((num) => {
        const numElement = document.createElement("div");
        numElement.className = "number";
        numElement.textContent = num;
        numElement.dataset.value = num;
        visualizationDiv.appendChild(numElement);
      });

      const result = longestConsecutive(nums);
      document.getElementById("output").textContent =
        `Longest Consecutive Sequence: ${result}`;
    </script>
  </body>
</html>
```

This visualization creates a simple interface where you can see the input array and the longest consecutive sequence highlighted. The numbers in the longest consecutive sequence will be highlighted in green.
