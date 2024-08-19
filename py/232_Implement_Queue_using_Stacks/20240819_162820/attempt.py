from typing import List


class MyQueue:
    class Stack:
        def __init__(self) -> None:
            self.inner: List[int] = []

        def push(self, x: int) -> None:
            self.inner.append(x)

        def pop(self) -> int:
            return self.inner.pop()

        def __getitem__(self, idx: int) -> int:
            return self.inner[idx]

        def empty(self) -> bool:
            return len(self.inner) == 0

    def __init__(self):
        self.back = MyQueue.Stack()
        self.front = MyQueue.Stack()

    def push(self, x: int) -> None:
        self.back.push(x)

    def pop(self) -> int:
        if self.front.empty():
            self.__pack__()
        return self.front.pop()

    def peek(self) -> int:
        return self.front[-1] if not self.front.empty() else self.back[0]

    def empty(self) -> bool:
        return self.back.empty() and self.front.empty()

    def __pack__(self):
        while not self.back.empty():
            self.front.push(self.back.pop())


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

