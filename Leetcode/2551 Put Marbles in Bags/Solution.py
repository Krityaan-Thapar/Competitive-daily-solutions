import heapq
from typing import List

class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        W = len(weights)
        adj = [weights[i] + weights[i + 1] for i in range(W - 1)]
        adj_max = [-i for i in adj]
        heapq.heapify(adj)
        heapq.heapify(adj_max)

        max_score, min_score = 0, 0
        for i in range(k - 1):
            max_score += -1 * heapq.heappop(adj_max)
            min_score += heapq.heappop(adj)
        
        return max_score - min_score

class Solution2:
    def putMarbles(self, weights: List[int], k: int) -> int:
        adj = sorted([weights[i] + weights[i + 1] for i in range(len(weights) - 1)])
        return sum(adj[len(weights) - 2 - i] - adj[i] for i in range(k - 1))