from typing import List
import unittest


def binarySearch(sorted: List[int], target: int) -> int:
    def binarySearchInvariant(idx: int) -> bool:
        return sorted[idx] >= target

    left, right = 0, len(sorted) - 1
    while left < right:
        mid = left + ((right - left) // 2)
        if binarySearchInvariant(mid):
            right = mid
        else:
            left = mid + 1
    return left if left > 0 and left < len(sorted) and sorted[left] == target else -1


class TestBinarySearch(unittest.TestCase):
    def testEmptyList(self):
        self.assertEqual(binarySearch([], 5), -1)

    def testMissing(self):
        self.assertEqual(binarySearch([1, 2, 3, 4, 7], 5), -1)

    def testPresentEven(self):
        self.assertEqual(binarySearch([10, 20, 50, 89, 100], 50), 2)

    def testPresentOdd(self):
        self.assertEqual(binarySearch([10, 11, 20, 50, 89, 100], 50), 3)


if __name__ == "__main__":
    unittest.main()
