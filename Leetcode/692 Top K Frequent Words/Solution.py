from typing import List
from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq = Counter(words)
        heap = []
        for key, val in freq.items():
            heapq.heappush(heap, (-val, key))
        return [heapq.heappop(heap)[1] for i in range(k)] 

# k log n
class Solution2:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq = Counter(words) # O(n)
        heap = [(-v, k) for k, v in freq.items()] # O(n)
        heapq.heapify(heap) # O(n)
        return [heapq.heappop(heap)[1] for i in range(k)]