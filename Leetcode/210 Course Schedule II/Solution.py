from typing import List
from collections import defaultdict, deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegrees = [0 for _ in range(numCourses)]
        adj = defaultdict(list)
        
        for d, s in prerequisites:
            indegrees[d] += 1
            adj[s].append(d)
        
        q = deque([])
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

        if len(ans) != numCourses:
            return [] 
        return ans