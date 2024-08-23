# General Interview Coaching

## Scratch Notes

```python
# given two lists of non-overlapping intervals,
# merge them into a single list of non-overlapping intervals

# example:
# list 1 - [[0,100]]
# list 2 - [[1, 3], [6, 8]]
# temp_interval - [0, 6]
# answer - [[0, 5], [6, 8], [10, 14]]

# general interview outline

# 1. thinking through / discussing your approach
#      -> identify edge cases +
#      -> how clearly you break down the algo / illustrate your approach.
#           for instance:
#           - sort the lists - O(n log n)
#           - iterate through - n (length of the first list) + m (length of second list)
#      -> being able to identify multiple approaches (incl. brute force,
#         just be ready to move past it / signal you know it's brute force)
# 2. discuss time complexity
#      -> is it correct
#      -> if the algo has different parts, identify that
# 3. implementation (collaborative w/ interviewer)
#      -> when you're blocked, communicate the problem clearly
# 4. testing
#      -> you have to construct your own test case
#      -> make it minimal, cover the necessary conditions
#      -> you might have to test multiple cases
#      -> step through the code line by line
#      -> test what you wrote, not what you think you wrote
```

## Process

- Pick a question at random
- Obfuscate a bit (because you need to ask clarifying questions)
- Make sure to discuss approach and agree first
  - Algorithm steps (is this a combination of multiple substeps?)
  - Space and time complexity
- Prompting when stuck
-
