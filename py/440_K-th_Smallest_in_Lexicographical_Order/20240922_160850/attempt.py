class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def count_numbers(prefix: int, n: int) -> int:
            count = 0
            current, next = prefix, prefix + 1
            while current <= n:
                count += min(n + 1, next) - current
                current *= 10
                next *= 10
            return count

        current = 1
        k -= 1  # We start from 1, so we need to find the (k-1)th number after 1

        while k > 0:
            count = count_numbers(current, n)
            if k >= count:
                k -= count
                current += 1
            else:
                k -= 1
                current *= 10

        return current

