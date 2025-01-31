from typing import List
from collections import deque, defaultdict

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        curr = 2
        r, c = len(grid), len(grid[0])
        area_map = defaultdict(int)
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def search(x, y):
            grid[x][y] = curr
            area = 1
            q = deque([(x, y)])

            while q:
                cx, cy = q.popleft()
                for dx, dy in dirs:
                    nx, ny = cx + dx, cy + dy
                    if 0 <= nx < r and 0 <= ny < c and grid[nx][ny] == 1:
                        grid[nx][ny] = curr
                        area += 1
                        q.append((nx, ny))
            return area

        area_map[0] = 0
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1:
                    area_map[curr] = search(i, j)
                    curr += 1
        
        ans = 0
        all_ones_map = True
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 0:
                    all_ones_map = False
                    local = 1
                    visited = set()

                    for dx, dy in dirs:
                        nx, ny = i + dx, j + dy
                        if 0 <= nx < r and 0 <= ny < c and grid[nx][ny] not in visited:
                            local += area_map[grid[nx][ny]]
                            visited.add(grid[nx][ny])
                    ans = max(local, ans)
        
        if all_ones_map:
            return r * c
        return ans