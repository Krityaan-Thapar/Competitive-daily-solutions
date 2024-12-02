from typing import List
from collections import deque, defaultdict

class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        n, m = len(edges1) + 1, len(edges2) + 1
        tree1, tree2 = defaultdict(list), defaultdict(list)
        
        def tree_construct(tree, edges):
            for src, dst in edges:
                tree[src].append(dst)
                tree[dst].append(src)
        
        tree_construct(tree1, edges1)
        tree_construct(tree2, edges2)

        colour1, colour2 = [0 for _ in range(2)], [0 for _ in range(2)]
        nodes1, nodes2 = [0 for _ in range(n)], [0 for _ in range(m)]

        def bfs(adj, colour, nodes):
            q = deque([(0, 0)])
            visited = set()
            visited.add(0)

            while q:
                curr, col = q.popleft()
                nodes[curr] = col
                colour[col] += 1

                for nei in adj[curr]:
                    if nei not in visited:
                        visited.add(nei)
                        q.append((nei, (col + 1) % 2))
        
        bfs(tree1, colour1, nodes1)
        bfs(tree2, colour2, nodes2)
        
        ans = []
        t2_contr = max(colour2[0], colour2[1])
        for i in range(n):
            ans.append(colour1[nodes1[i]] + t2_contr)
        return ans