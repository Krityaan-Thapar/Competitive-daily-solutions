from typing import List

class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        r, c = len(grid), len(grid[0])
        ans = 0
        for col in range(c):
            for row in range(1, r):
                if grid[row][col] <= grid[row - 1][col]:
                    ans += (grid[row - 1][col] + 1 - grid[row][col])
                    grid[row][col] = grid[row - 1][col] + 1
        return ans