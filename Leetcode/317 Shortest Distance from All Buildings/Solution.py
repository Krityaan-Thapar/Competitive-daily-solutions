from typing import List
from collections import deque

class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        marks = [[[0, 0] for _ in range(C)] for _ in range(R)] # dist, num
        sources, dirs = [], [(0, 1), (1, 0), (-1, 0), (0, -1)]
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 1:
                    sources.append((i, j))
        target = len(sources)

        for x, y in sources:
            q = deque([(x, y, 0)])
            visited = set()
            while q:
                cx, cy, dist = q.popleft()
                for dx, dy in dirs:
                    nx, ny = cx + dx, cy + dy
                    if 0 <= nx < R and 0 <= ny < C and (nx, ny) not in visited and grid[nx][ny] == 0:
                        visited.add((nx, ny))
                        marks[nx][ny][1] += 1
                        marks[nx][ny][0] += dist + 1
                        q.append((nx, ny, dist + 1))
        
        ans = int(1e5)
        for i in range(R):
            for j in range(C):
                if marks[i][j][1] == target:
                    ans = min(ans, marks[i][j][0])
        return ans if ans != int(1e5) else -1