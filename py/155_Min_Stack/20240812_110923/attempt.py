class MinStack:

    def __init__(self):
        self.inner = []
        self.mins = []

    def push(self, val: int) -> None:
        self.inner.append(val)
        self.mins.append(
            val if not self.mins else min(self.mins[len(self.mins) - 1], val)
        )

    def pop(self) -> None:
        self.inner.pop()
        self.mins.pop()

    def top(self) -> int:
        return self.inner[len(self.inner) - 1]

    def getMin(self) -> int:
        return self.mins[len(self.mins) - 1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

