from collections import deque

class Solution:
    def numIslands(self, grid):
        R, C = len(grid), len(grid[0])
        dirs = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (0, -1), (1, 1), (1, -1), (1, 0)]
        num = 0
        
        def process(x, y):
            nonlocal num
            q = deque()
            q.append((x, y))
            
            while q:
                cx, cy = q.popleft()
                for dx, dy in dirs:
                    nx, ny = cx + dx, cy + dy
                    if 0 <= nx < R and 0 <= ny < C and grid[nx][ny] == "L":
                        grid[nx][ny] = num
                        q.append((nx, ny))
        
        for i in range(R):
            for j in range(C):
                if grid[i][j] == "L":
                    num += 1
                    grid[i][j] = num
                    process(i, j)
        return num