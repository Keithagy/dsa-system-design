from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        longest_rot_chain = 0

        def is_rotten(row: int, col: int) -> bool:
            return grid[row][col] == 2

        def is_fresh(row: int, col: int) -> bool:
            return grid[row][col] == 1

        def is_empty(row: int, col: int) -> bool:
            return grid[row][col] == 0

        def dfs(row: int, col: int, rot_chain_length: int) -> int:
            nonlocal longest_rot_chain

            longest_path_through_me = rot_chain_length
            for row_offset, col_offset in directions:
                new_row = row + row_offset
                new_col = col + col_offset

                # Only dfs neighboring fresh oranges, excluding neighboring rotten oranges, because they should take precedence as the head of a longest-path calc
                # i.e only let the closest rotten orange rot a fresh orange
                if not (
                    new_row >= 0
                    and new_row < len(grid)
                    and new_col >= 0
                    and new_col < len(grid[0])
                    and is_fresh(new_row, new_col)
                ):
                    continue
                grid[new_row][new_col] = 2
                longest_path_through_me = max(
                    longest_path_through_me, dfs(new_row, new_col, rot_chain_length + 1)
                )
            return longest_path_through_me

        def isolated(row: int, col: int) -> bool:
            for row_offset, col_offset in directions:
                new_row = row + row_offset
                new_col = col + col_offset
                if not (
                    new_row >= 0
                    and new_row < len(grid)
                    and new_col >= 0
                    and new_col < len(grid[0])
                ):
                    continue
                if not is_empty(new_row, new_col):
                    return False
            return True

        isolated_fresh = False
        zero_rottens = True
        has_oranges = False
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if is_fresh(row, col):
                    has_oranges = True
                    if isolated(row, col):
                        isolated_fresh = True
                        break
                if is_rotten(row, col):
                    has_oranges = True
                    zero_rottens = False
                    longest_rot_chain = max(longest_rot_chain, dfs(row, col, 0))
        return (
            -1
            if isolated_fresh or (has_oranges and zero_rottens)
            else longest_rot_chain
        )

