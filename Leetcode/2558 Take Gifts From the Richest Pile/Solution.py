import heapq
from typing import List
from math import floor

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        ans = sum(gifts)
        bleh = [-i for i in gifts]
        heapq.heapify(bleh)

        for _ in range(k):
            curr = -1 * heapq.heappop(bleh)
            leave = floor(curr ** 0.5)
            heapq.heappush(bleh, -1 * leave)
            ans = ans - curr + leave
        return ans