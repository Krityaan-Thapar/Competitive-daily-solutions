import heapq
from typing import List

class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        heap = []
        for p, t in classes:
            orig_ratio = p / t
            added_ratio = (p + 1) / (t + 1)
            diff = added_ratio - orig_ratio
            heap.append((-diff, p, t))
        
        heapq.heapify(heap)
        for _ in range(extraStudents):
            d, p, t = heapq.heappop(heap)
            new_p = p + 1
            new_t = t + 1
            orig_ratio = new_p / new_t
            added_ratio = (new_p + 1) / (new_t + 1)
            diff = added_ratio - orig_ratio
            heapq.heappush(heap, (-diff, new_p, new_t))
        
        s = 0
        for d, p, t in heap:
            s += (p / t)
        return s / len(heap)