from typing import List
from collections import defaultdict, deque

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        '''
        Invert the graph.
        Then terminal nodes are nodes with no incoming edges.
        And every node reachable from only terminal nodes is a safe node
        '''

        n = len(graph)
        indegrees = [0 for _ in range(n)]
        adj = defaultdict(list)

        for idx, i in enumerate(graph):
            for j in i:
                adj[j].append(idx)
                indegrees[idx] += 1

        # Seed the queue with terminal states
        q = deque([])
        for idx, i in enumerate(indegrees):
            if i == 0:
                q.append(idx)
        
        ans = []
        while q:
            curr = q.popleft()
            for nei in adj[curr]:
                indegrees[nei] -= 1
                if indegrees[nei] == 0:
                    q.append(nei)
            ans.append(curr)
        return sorted(ans)