from typing import List, Optional, Tuple


class MinStack:

    def __init__(self):
        self.inner: List[Tuple[int, int]] = []

    def __topTuple__(self) -> Optional[Tuple[int, int]]:
        if len(self.inner) == 0:
            return None
        return self.inner[len(self.inner) - 1]

    def push(self, val: int) -> None:
        top_tuple = self.__topTuple__()
        if not top_tuple:
            self.inner.append((val, val))
            return
        cur_min = top_tuple[1]
        self.inner.append((val, min(cur_min, val)))

    def pop(self) -> None:
        self.inner.pop()

    def top(self) -> int:
        top_tuple = self.__topTuple__()
        if not top_tuple:
            raise ValueError("getting top of empty stack")
        return top_tuple[0]

    def getMin(self) -> int:
        top_tuple = self.__topTuple__()
        if not top_tuple:
            raise ValueError("getting min of empty stack")
        return top_tuple[1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

