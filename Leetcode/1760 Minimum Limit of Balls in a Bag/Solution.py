from typing import List
from math import ceil

class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        def check(target):
            ops_needed = 0
            for i in nums:
                ops_needed += (ceil(i / target) - 1)
            return ops_needed <= maxOperations
        
        hi = max(nums)
        lo = 1

        ans = -1
        while lo <= hi:
            mid = (lo + hi) // 2

            if check(mid):
                ans = mid
                hi = mid - 1
            else:
                lo = mid + 1
        return ans