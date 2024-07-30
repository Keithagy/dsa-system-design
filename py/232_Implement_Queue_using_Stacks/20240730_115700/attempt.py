from typing import List, Optional


class MyQueue:

    def __init__(self):
        self.back = MyStack()
        self.front = MyStack()

    def push(self, x: int) -> None:
        self.back.push(x)

    # `pop` seems to assume it is only ever called when not empty...
    def pop(self) -> Optional[int]:
        if self.empty():
            return None
        if self.front.isEmpty():
            self.__flip()

        return self.front.pop()

    def peek(self) -> Optional[int]:
        if self.empty():
            return None
        if self.front.isEmpty():
            self.__flip()

        return self.front.peek()

    def empty(self) -> bool:
        return self.front.isEmpty() and self.back.isEmpty()

    def __flip(self) -> None:
        while not self.back.isEmpty():
            self.front.push(self.back.pop())


class MyStack:

    def __init__(self) -> None:
        self.inner: List[int] = []

    def push(self, val: int) -> None:
        self.inner.append(val)

    def peek(self) -> Optional[int]:
        if self.isEmpty():
            return None
        return self.inner[len(self.inner) - 1]

    def pop(self) -> Optional[int]:
        if self.isEmpty():
            return None
        return self.inner.pop()

    def isEmpty(self) -> bool:
        return len(self.inner) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

