from typing import List

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        r, c = len(grid), len(grid[0])
        row_count, col_count = [0 for _ in range(r)], [0 for _ in range(c)]

        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1:
                    row_count[i] += 1
                    col_count[j] += 1
        
        ans = 0
        for i in range(r):
            for j in range(c):
                if row_count[i] > 1 or col_count[j] > 1:
                    ans += grid[i][j]
        return ans