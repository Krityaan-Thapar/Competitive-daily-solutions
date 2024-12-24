from typing import List
from collections import defaultdict, deque
from math import ceil

class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        def diameter(adj, arbit):
            n1, _ = bfs(adj, arbit)
            n2, d = bfs(adj, n1)
            return d
        
        def bfs(adj, src):
            ans = [src, 0]
            q = deque([(src, 0, -1)])
            
            while q:
                curr, dist, parent = q.popleft()
                if dist > ans[1]:
                    ans = [curr, dist]
                
                for nei in adj[curr]:
                    if nei == parent:
                        continue
                    
                    q.append((nei, dist + 1, curr))
            return tuple(ans)
        
        adj1 = defaultdict(list)
        adj2 = defaultdict(list)
        for u, v in edges1:
            adj1[u].append(v)
            adj1[v].append(u)
        for u, v in edges2:
            adj2[u].append(v)
            adj2[v].append(u)
        
        d1, d2 = 0, 0
        if edges1:
            d1 = diameter(adj1, edges1[0][0])
        if edges2:
            d2 = diameter(adj2, edges2[0][0])
        return max(d1, d2, ceil(d1 / 2) + ceil(d2 / 2) + 1)