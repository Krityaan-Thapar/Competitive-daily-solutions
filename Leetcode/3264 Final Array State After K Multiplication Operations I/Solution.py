from typing import List
class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        while k > 0:
            bleh = min(nums)
            idx = nums.index(bleh)
            nums[idx] *= multiplier
            k -= 1
        
        return nums

import heapq
class Solution2:
    def getFinalState(self, nums: List[int], k: int, multiplier: int):
        pq = [(val, i) for i, val in enumerate(nums)]
        heapq.heapify(pq)

        for _ in range(k):
            _, i = heapq.heappop(pq)
            nums[i] *= multiplier
            heapq.heappush(pq, (nums[i], i))

        return nums