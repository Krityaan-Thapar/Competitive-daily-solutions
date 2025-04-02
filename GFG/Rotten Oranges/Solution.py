from collections import deque

class Solution:
    def orangesRotting(self, grid):
        R, C = len(grid), len(grid[0])
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        q = deque()
        
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 2:
                    q.append((i, j))
        
        t = 0
        while q:
            next_q = deque()
            flag_time = False
            for cx, cy in q:
                for dx, dy in dirs:
                    nx, ny = cx + dx, cy + dy
                    if 0 <= nx < R and 0 <= ny < C and grid[nx][ny] == 1:
                        flag_time = True
                        grid[nx][ny] = 2
                        next_q.append((nx, ny))
            
            if flag_time:
                t += 1
            q = next_q
        
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 1:
                    return -1
        return t