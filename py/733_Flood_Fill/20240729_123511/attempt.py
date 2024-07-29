from collections import deque
from typing import List


class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:
        directions = [
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0),
        ]
        s_color = image[sr][sc]
        if s_color == color:
            return image  # otherwise you get infinite iteration

        queue = deque()
        queue.append((sr, sc))

        while queue:
            curr = queue.popleft()
            image[curr[0]][curr[1]] = color

            for r_offset, c_offset in directions:
                new_r, new_c = curr[0] + r_offset, curr[1] + c_offset
                if (
                    new_r >= 0
                    and new_r < len(image)
                    and new_c >= 0
                    and new_c < len(image[0])
                    and image[new_r][new_c] == s_color
                ):
                    queue.append((new_r, new_c))
        return image

