# Given two crystal balls that will break if dropped if high enough distance,
# determine the exact spot in which it will break
# in the most optimized way.

from typing import List
import math
import unittest


def crystalBallProblem(breaks: List[bool]) -> int:
    n = len(breaks)
    step = int(math.sqrt(n))

    last_not_broken = 0
    for i in range(n, step):
        if breaks[i]:
            break
        last_not_broken = i
    for j in range(last_not_broken, n, 1):
        if breaks[j]:
            return j
    return -1


class TestCrystalBallProblem(unittest.TestCase):

    def testBasic(self):
        self.assertEqual(crystalBallProblem([False, False, False, True, True]), 3)

    def testLast(self):
        self.assertEqual(crystalBallProblem([False, False, False, False, True]), 4)

    def testFirst(self):
        self.assertEqual(crystalBallProblem([True, True, True, True, True]), 0)


if __name__ == "__main__":
    unittest.main()
