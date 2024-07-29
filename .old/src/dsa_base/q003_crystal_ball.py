import math


# Given two crystal balls that will break if dropped from high enough distance,
# determine the exact spot in which it will break in the most optimized way
# Assume threshold > 0
def two_crystal_balls(threshold: int, n: int) -> int:
    jump_counts, jump_dist = int(math.sqrt(n) // 1), int(
        math.sqrt(n) // 1
    )  # use the lowest index
    i = 0
    # First ball breaks
    while i < jump_counts:
        if will_break(threshold, i):
            break
        i += jump_dist

    i -= jump_dist  # move back one for walking startpoint

    while i < n:
        if will_break(threshold, i):
            return i
        i += 1
    return n


def will_break(threshold: int, height: int) -> bool:
    return height >= threshold
