from typing import List, Optional


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        """
        Asteroids only collide if an earlier-moving one is going right
        and a later moving one is going left
        an earlier moving one that is going left never crashes, because it diverges from all subsequent right moving asteroids
        """
        stack = []

        def movingRight(asteroid: int) -> bool:
            return asteroid > 0

        def movingLeft(asteroid: int) -> bool:
            return asteroid < 0

        def willCollide(onStack: int, incoming: int) -> bool:
            return movingRight(onStack) and movingLeft(incoming)

        def collide(onStack: int, incoming: int) -> Optional[int]:
            if abs(onStack) == abs(incoming):
                return None
            return onStack if abs(onStack) > abs(incoming) else incoming

        for asteroid in asteroids:
            if not stack or not willCollide(stack[-1], asteroid):
                stack.append(asteroid)
                continue
            while stack and asteroid and willCollide(stack[-1], asteroid):
                asteroid = collide(stack.pop(), asteroid)
            if asteroid is not None:
                stack.append(asteroid)
        return stack

