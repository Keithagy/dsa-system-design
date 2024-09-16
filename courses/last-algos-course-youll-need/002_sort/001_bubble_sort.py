from typing import List
import unittest


def bubbleSort(nums: List[int]) -> List[int]:
    for i in range(len(nums)):
        for j in range(len(nums) - 1 - i):
            # notice that we aren't comparing i and j
            # we are instead comparing j with a single-position lookahead!
            # that's why we need to range j only till len-1
            # on top of that, each time i increments, the (i+1)th largest element
            # would have been bubbled up. j and j + 1 lookahead no longer has to cover that
            # so, range j only till len-1-i
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums


class TestBubbleSort(unittest.TestCase):
    def testEmptyList(self):
        self.assertEqual(bubbleSort([]), [])

    def testSingleElement(self):
        self.assertEqual(bubbleSort([5]), [5])

    def testAlreadySorted(self):
        self.assertEqual(bubbleSort([1, 2, 3, 4, 5, 6]), [1, 2, 3, 4, 5, 6])

    def testNeedSorting(self):
        self.assertEqual(bubbleSort([7, 0, 12, -5, 99, 6]), [-5, 0, 6, 7, 12, 99])

    def testReverseSorted(self):
        self.assertEqual(bubbleSort([1, 2, 5, 7, 9][::-1]), [1, 2, 5, 7, 9])


if __name__ == "__main__":
    unittest.main()
