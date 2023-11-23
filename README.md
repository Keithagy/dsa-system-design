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
