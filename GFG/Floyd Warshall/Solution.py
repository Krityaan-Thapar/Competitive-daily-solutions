class Solution:
	def floydWarshall(self, dist):
		INF = int(1e8)
		V = len(dist)
		
		for k in range(V):
			for i in range(V):
				for j in range(V):
					dist[i][j] = min(dist[i][k] + dist[k][j], dist[i][j])
		return dist