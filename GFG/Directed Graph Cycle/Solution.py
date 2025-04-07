class Solution:
    def isCycle(self, V, edges):
        adj = [[] for _ in range(V)]
        indegrees = [0 for _ in range(V)]
        for src, dst in edges:
            indegrees[dst] += 1
            adj[src].append(dst)
        
        from collections import deque
        q = deque()
        for idx, i in enumerate(indegrees):
            if i == 0:
                q.append(idx)
        
        bleh = 0
        while q:
            curr = q.popleft()
            bleh += 1
            for nei in adj[curr]:
                indegrees[nei] -= 1
                if indegrees[nei] == 0:
                    q.append(nei)
        return bleh != V