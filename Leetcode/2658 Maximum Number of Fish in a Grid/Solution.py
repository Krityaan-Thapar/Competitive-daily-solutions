from typing import List
from collections import deque

class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        ans = 0
        r, c = len(grid), len(grid[0])
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def bfs(x, y):
            q = deque([(x, y)])
            local = grid[x][y]
            grid[x][y] = -1

            while q:
                cx, cy = q.popleft()
                for dx, dy in dirs:
                    nx, ny = cx + dx, cy + dy
                    if 0 <= nx < r and 0 <= ny < c and grid[nx][ny] > 0:
                        local += grid[nx][ny]
                        grid[nx][ny] = -1
                        q.append((nx, ny))
            return local
        
        for i in range(r):
            for j in range(c):
                if grid[i][j] > 0:
                    tmp = bfs(i, j)
                    ans = max(ans, tmp)
        return ans