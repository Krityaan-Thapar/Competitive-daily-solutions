from typing import List
from collections import deque

class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        r, c = len(grid), len(grid[0])
        q = deque([])
        q.append((0, 0, 0))
        d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        visited = set()
        visited.add((0, 0))

        while q:
            x, y, cost = q.popleft()
            if x == r - 1 and y == c - 1:
                return cost
            
            for dx, dy in d:
                nx, ny = x + dx, y + dy
                if 0 <= nx < r and 0 <= ny < c and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    if grid[nx][ny] == 0:
                        q.appendleft((nx, ny, cost))
                    else:
                        q.append((nx, ny, cost + 1))
        return -1

class Solution2:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        r, c = len(grid), len(grid[0])
        dist = [[int(1e10) for _ in range(c)] for _ in range(r)]
        dist[0][0] = 0
        q = deque([(0, 0)])
        d = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        while q:
            x, y = q.popleft()
            if x == r - 1 and y == c - 1:
                return dist[x][y]
             
            for dx, dy in d:
                nx, ny = x + dx, y + dy
                if 0 <= nx < r and 0 <= ny < c:
                    if dist[x][y] + grid[nx][ny] < dist[nx][ny]:
                        dist[nx][ny] = dist[x][y] + grid[nx][ny]
                        if grid[nx][ny] == 0:
                            q.appendleft((nx, ny))
                        else:
                            q.append((nx, ny))
        return dist[r - 1][c - 1]