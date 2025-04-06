from collections import deque

class Solution:
    def topoSort(self, V, edges):
        adj = [[] for _ in range(V)]
        indegrees = [0 for _ in range(V)]
        for src, dst in edges:
            adj[src].append(dst)
            indegrees[dst] += 1
        
        q = deque()
        for idx, i in enumerate(indegrees):
            if i == 0:
                q.append(idx)
        
        ans = []
        while q:
            curr = q.popleft()
            ans.append(curr)
            for nei in adj[curr]:
                indegrees[nei] -= 1
                if indegrees[nei] == 0:
                    q.append(nei)
        return ans