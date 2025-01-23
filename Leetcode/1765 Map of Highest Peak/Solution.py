from typing import List
from collections import deque

class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        # Mutlisource BFS
        r, c = len(isWater), len(isWater[0])
        grid = [[-1 for _ in range(c)] for _ in range(r)]
        q = deque([])
        dirs = [[0, 1], [1, 0], [-1, 0], [0, -1]]

        for i in range(r):
            for j in range(c):
                if isWater[i][j] == 1:
                    grid[i][j] = 0
                    q.append((0, i, j))
        
        while q:
            h, x, y = q.popleft()
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < r and 0 <= ny < c and grid[nx][ny] == -1:
                    grid[nx][ny] = h + 1
                    q.append((h + 1, nx, ny))
        return grid