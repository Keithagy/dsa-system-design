# leetcode-practice

All my leetcode practice, indexed by problem, then language, then date.

## Handy resources / references

- [Primeagean's The Last Algorithms Course You'll Need](https://theprimeagen.github.io/fem-algos/lessons/introduction/intro)
- [Leetcode 75](https://leetcode.com/studyplan/leetcode-75/)
- [Grind 75](https://www.techinterviewhandbook.org/grind75)

## Principles collected

- When working with collections (e.g. arrays, hashmaps, sets), make sure you have the following cases covered
  - Empty
  - Single element
  - Multiple elements (bulk of the logic typically goes here)
- Consider if it is important to preserve order of inputs.
  - If no, consider if sorting improves your runtime
- Sometimes, the key to a probablem could lie in chaining array/subarray reversals
  - naturally, this includes strings too
- [Binary search mental model](https://leetcode.com/discuss/general-discussion/786126/python-powerful-ultimate-binary-search-template-solved-many-problems)
- Moving in four directions on a grid:

```python
# Define the directions to move in the grid
  directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
# Check all four directions
for dr, dc in directions:
    new_r, new_c = r + dr, c + dc
    # Check if the new pixel is within bounds and has the original color and not visited
    if (0 <= new_r < len(image) and 0 <= new_c < len(image[0]) and
            image[new_r][new_c] == original_color and (new_r, new_c) not in visited):
        stack.append((new_r, new_c))
```

- Linked list ergonomics

  - Find middle via slow + fast pointers instead of doing two traversals

  ```python
  #Find the midpoint of the linked list
    slow = fast = head
    while fast and fast.next:
      slow = slow.next
      fast = fast.next.next
  ```

  - For list-is-palindrome checks, easier to just reverse the second half instead of tracking first half to first bookend

  ````python
  #Reverse the second half of the linked list
    prev = None
    curr = slow
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node```
  ````

  - Array transformation subtleties
    - When swapping array elements, incrementing the slow pointer after a swap can help ensure the slow pointer gets "in position" before the fast pointer sees the next swap trigger

## TODOs (i.e potentially fun ways to over-engineer this)

- Leetcode templater
  - `leetcode-practice {go/rust/python} {leetcode-problem-url}`
    - GET call to leetcode problem url
    - Deduce question number
    - Create new question folder if not exists
    - Create `problem.md` containing the correct HTML node contents if not exists
    - Create answer folder for today's date if not exists
    - Add file generated from solution template for the selected language (if exists, return error with the filepath)
      - If rust, additional code needed to wire up module tree
    - LATER: support test cases
      - A little bit tricky given desirabilty of generification, certain questions asking for in-place mutation, semantics of return type if any
      - E.g. In some cases the return value might not represent to result vector itself, but its length, or whether it satisfies a certain predicate
  - Can I pipeline this to generate stats?
    - Problems I've failed and should retry?
    - Spaced repetition helper?
    - Dashboard of problems by language? By difficulty? By category?
