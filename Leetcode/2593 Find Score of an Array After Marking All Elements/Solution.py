import heapq
from typing import List

class Solution:
    def findScore(self, nums: List[int]) -> int:
        heap = [(i, idx) for idx, i in enumerate(nums)]
        heapq.heapify(heap)
        marked = set()
        ans = 0

        while heap:
            curr, curr_idx = heapq.heappop(heap)
            if curr_idx in marked:
                continue

            ans += curr
            marked.add(curr_idx)
            marked.add(curr_idx - 1)
            marked.add(curr_idx + 1)
        return ans   