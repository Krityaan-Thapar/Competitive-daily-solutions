from collections import deque

class Solution:
    def bfs(self, adj):
        ans = []
        q = deque([0])
        visited = set()
        visited.add(0)
        
        while q:
            curr = q.popleft()
            ans.append(curr)
            for nei in adj[curr]:
                if nei not in visited:
                    q.append(nei)
                    visited.add(nei)
        return ans