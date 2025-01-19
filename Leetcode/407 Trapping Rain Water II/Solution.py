'''
I don't like this question

The amount of water stored in a tile = max(0, influence_level - heightMap[i][j])
influence_level = min(height of all neighbor cells)

This works perfect for a 1x1 water pool, but a larger pool cannot determine influence_level simply from its 4 neighbors, since that could also be influenced from its neighbors

In any case, influence_level needs to start propagating inwards from the borders. Min-Heapify this, since the trapped water is bounded by the minimum influencing tile height, else the water will flow out

We can process the grid by popping from the heap and adding the neighbors to the heap again. Influenced_level propagates as max(popped_height, neighbour_height)

Proving this? lol good luck
'''
from typing import List
import heapq

class Solution:
    def trapRainWater(self, hM: List[List[int]]) -> int:
        r, c = len(hM), len(hM[0])
        if r < 3 or c < 3: # edge case bounds
            return 0
        
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        heap = []
        for i in range(r):
            for j in range(c):
                if i in [0, r - 1] or j in [0, c - 1]:
                    heapq.heappush(heap, (hM[i][j], i, j)) # influenced_level , coords
                    hM[i][j] = -1 # mark visited
        
        ans = 0
        curr_inf_level = 0
        while heap:
            inf_level, x, y = heapq.heappop(heap)
            curr_inf_level = max(inf_level, curr_inf_level) 
            # given this property it looks like 0-1 BFS is possible?
            # Atleast not 0-1, but 1-K => Dial's algo
            
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < r and 0 <= ny < c and hM[nx][ny] != -1:
                    ans += max(0, curr_inf_level - hM[nx][ny])
                    heapq.heappush(heap, (hM[nx][ny], nx, ny))
                    hM[nx][ny] = -1
        return ans