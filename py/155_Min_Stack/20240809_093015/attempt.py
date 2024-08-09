class MinStack:

    def __init__(self):
        self.stack = []
        self.mins = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.mins or val <= self.mins[len(self.mins) - 1]:
            self.mins.append(val)

    def pop(self) -> None:
        popped = self.stack.pop()
        if popped == self.mins[len(self.mins) - 1]:
            self.mins.pop()

    def top(self) -> int:
        return self.stack[len(self.stack) - 1]

    def getMin(self) -> int:
        return self.mins[len(self.mins) - 1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

