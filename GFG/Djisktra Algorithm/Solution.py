import heapq

class Solution:
    def dijkstra(self, V, edges, src):
        adj = [[] for _ in range(V)]
        dist = [int(1e10) for _ in range(V)]
        dist[src] = 0
        heap = [(src, 0)]
        
        for src, dst, wt in edges:
            adj[src].append((dst, wt))
        
        while heap:
            curr, cost = heapq.heappop(heap)
            if cost > dist[curr]:
                continue
            
            for nei, wt in adj[curr]:
                if dist[nei] >= cost + wt:
                    heapq.heappush(heap, (nei, cost + wt))
                    dist[nei] = cost + wt
        return dist