import heapq

class Solution:
    def findMinCycle(self, V, edges):
        def shortestPath(V, adj, src, dest):
            dist = [int(1e10)] * V
            dist[src] = 0
            pq = [(0, src)]
            
            while pq:
                d, u = heapq.heappop(pq)
                if d > dist[u]:
                    continue
                
                for v, w in adj[u]:
                    if (u == src and v == dest) or (u == dest and v == src):
                        continue
                    
                    if dist[v] > dist[u] + w:
                        dist[v] = dist[u] + w
                        heapq.heappush(pq, (dist[v], v))
            return dist[dest]
        
        adj = [[] for _ in range(V)]
        for edge in edges:
            u, v, w = edge
            adj[u].append((v, w))
            adj[v].append((u, w))
        minCycle = int(1e10)
        
        for edge in edges:
            u, v, w = edge
            dist = shortestPath(V, adj, u, v)
            
            if dist != int(1e10):
                minCycle = min(minCycle, dist + w)
        return minCycle