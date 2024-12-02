from typing import List
from collections import defaultdict, deque

class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        n, m = len(edges1) + 1, len(edges2) + 1
        adj1, adj2 = defaultdict(list), defaultdict(list)
        for src, dst in edges1:
            adj1[src].append(dst)
            adj1[dst].append(src)
        for src, dst in edges2:
            adj2[src].append(dst)
            adj2[dst].append(src)
        
        def bfs(src, adj, k):
            c = 0
            q = deque([(src, k)])
            visited = set()
            visited.add(src)
            
            while q:
                curr, dist = q.popleft()
                if dist == -1:
                    break
                c += 1
                
                for nei in adj[curr]:
                    if nei not in visited:
                        visited.add(nei)
                        q.append((nei, dist - 1))
            return c

        t2_contr = -1
        for i in adj2:
            x = bfs(i, adj2, k - 1)
            t2_contr = max(x, t2_contr)
        
        ans = []
        for i in range(n):
            ans.append(bfs(i, adj1, k) + t2_contr)
        return ans