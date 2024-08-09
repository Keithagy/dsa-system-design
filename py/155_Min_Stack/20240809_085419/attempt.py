from typing import Optional


class MinStack:

    def __init__(self):
        self.inner = []
        self.min: Optional[int] = None

    def push(self, val: int) -> None:
        self.inner.append(val)
        self.min = val if self.min is None else min(self.min, val)

    def pop(self) -> None:
        val = self.inner.pop()
        next_smallest = None if len(self.inner) == 0 else min(self.inner)
        self.min = next_smallest
        return val

    def top(self) -> int:
        return self.inner[len(self.inner) - 1]

    def getMin(self) -> int:
        if self.min is None:
            raise ValueError("Empty Stack")
        return self.min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

