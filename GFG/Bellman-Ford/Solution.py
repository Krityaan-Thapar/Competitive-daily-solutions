class Solution:
    def bellmanFord(self, V, edges, src):
        INF = int(1e8)
        dist = [INF for _ in range(V)]
        dist[src] = 0
        
        for i in range(V):
            for s, d, w in edges:
                if dist[s] != INF and dist[s] + w < dist[d]:
                    if i == V - 1:
                        return [-1]
                    dist[d] = dist[s] + w
        return dist