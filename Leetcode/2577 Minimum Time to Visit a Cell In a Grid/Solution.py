from typing import List
import heapq

class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        r, c = len(grid), len(grid[0])
        d = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        dist = [[int(1e7) for _ in range(c)] for _ in range(r)]
        dist[0][0] = 0
        heap = [(0, 0, 0)]

        if grid[0][1] > 1 and grid[1][0] > 1:
            return -1
        
        while heap:
            time, x, y = heapq.heappop(heap)
            if x == r - 1 and y == c - 1:
                return time
            
            if time > dist[x][y]:
                continue
            
            time += 1
            for dx, dy in d:
                nx, ny = x + dx, y + dy
                temp = None
                if 0 <= nx < r and 0 <= ny < c:
                    if time >= grid[nx][ny]:
                        temp = time
                    elif (grid[nx][ny] - time) % 2 == 0:
                        temp = grid[nx][ny]
                    else:
                        temp = grid[nx][ny] + 1
                
                    if temp < dist[nx][ny]:
                        dist[nx][ny] = temp
                        heapq.heappush(heap, (temp, nx, ny))
        return -1