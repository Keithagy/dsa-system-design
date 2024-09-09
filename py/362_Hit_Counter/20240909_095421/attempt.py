import bisect


class HitCounter:

    def __init__(self):
        self.inner = []

    def hit(self, timestamp: int) -> None:
        self.inner.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        i = bisect.bisect_left(self.inner, timestamp)
        start_bound = timestamp - 300  # look back 300 seconds
        if start_bound > 0:
            j = bisect.bisect_left(self.inner, start_bound)
            return len(self.inner[j : i + 1])
        return len(self.inner[: i + 1])


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
