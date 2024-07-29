from typing import Dict, List, Set, Tuple


# TODO: Future challenge: implement BFS, A* approach to maze solving
def maze_solver(
    maze: List[List[str]], wall: str, start: Tuple[int, int], end: Tuple[int, int]
) -> List[Tuple[int, int]]:
    return traverse(maze, wall, start, end, {start})


def traverse(
    maze: List[List[str]],
    wall: str,
    curr: Tuple[int, int],
    end: Tuple[int, int],
    seen: Set[Tuple[int, int]],
) -> List[Tuple[int, int]]:
    directions: Dict[str, Tuple[int, int]] = {
        "up": (-1, 0),
        "down": (1, 0),
        "left": (0, -1),
        "right": (0, 1),
    }

    (row_no, col_no) = curr
    if row_no < 0 or row_no >= len(maze) or col_no < 0 or col_no >= len(maze[0]):
        return []
    if maze[row_no][col_no] == wall:
        return []
    if curr in seen:
        return []
    if curr == end:
        return [end]

    seen.add(curr)
    for row_diff, col_diff in directions.values():
        new_row_no = row_no + row_diff
        new_col_no = col_no + col_diff

        path = [curr] + traverse(maze, wall, (new_row_no, new_col_no), end, seen)
        if len(path) > 0 and path[-1] == end:
            return path
    return []  # only get here if no end, which realistically is invalid
