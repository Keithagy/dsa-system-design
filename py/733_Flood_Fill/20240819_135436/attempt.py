from typing import List
from collections import deque


class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:
        initial = image[sr][sc]
        if initial == color:
            return image
        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1),
        ]
        queue = deque([(sr, sc)])
        while queue:
            r, c = queue.popleft()
            image[r][c] = color
            for r_diff, c_diff in directions:
                nr, nc = r + r_diff, c + c_diff
                if (
                    0 <= nr < len(image)
                    and 0 <= nc < len(image[0])
                    and image[nr][nc] == initial
                ):
                    queue.append((nr, nc))
        return image

