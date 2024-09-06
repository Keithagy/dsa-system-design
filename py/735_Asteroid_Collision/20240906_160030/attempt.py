from typing import List, Optional


class Solution:
    # At least 2 asteroids
    # size can be 1-1000, in either direction (-1000 to 1000)
    # it will never be zero
    # if all asteroids moving in one direction, no collisions
    # in the aftermath, all asteroids will have the same sign
    # so you can scan forward for the first asteroid pair with different signs
    # brute force way is to keep running the simulation until all asteroids point the same direction
    # there will be as many collisions as there are pairs of opposing-signed elements, which at the maximum will be n/2
    # however, each simulation will involve traversing O(n) items, making the algorithm n^2
    #
    # this is rather similar to stack-based string manipulation.
    # You can push items if they are the same sign as last seen, and pop otherwise. it is a monotonic stack kind of thing.
    # you will visit each item at most twice. at best you only push, and worst you push and then you pop. So you have an O(n) solution.
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        def sameDirection(a1: int, a2: int) -> bool:
            if (a1 < 0 and a2 < 0) or (a1 > 0 and a2 > 0):
                return True
            return False

        def collide(a1: int, a2: int) -> Optional[int]:
            aa1, aa2 = abs(a1), abs(a2)
            if aa1 == aa2:
                return None
            return a1 if aa1 > aa2 else a2

        def movingLeft(a: int) -> bool:
            return a < 0

        def movingRight(a: int) -> bool:
            return a > 0

        for a in asteroids:
            if (movingLeft(a) and (not stack or not movingRight(stack[-1]))) or (
                movingRight(a) and (not stack or movingLeft(stack[-1]))
            ):
                stack.append(a)
                continue

            a_destroyed = False
            while stack and not sameDirection(a, stack[-1]):
                survivor = collide(a, stack[-1])

                if survivor == a:
                    stack.pop()
                    continue

                if survivor is None or survivor == stack[-1]:
                    if survivor is None:
                        stack.pop()
                    a_destroyed = True
                    break

            if not a_destroyed and (not stack or sameDirection(a, stack[-1])):
                stack.append(a)
        return stack

