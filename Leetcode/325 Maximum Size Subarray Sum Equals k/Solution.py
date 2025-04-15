from functools import accumulate
from typing import List
from collections import defaultdict

class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        pref = accumulate(nums)
        seen = defaultdict(int)
        ans = 0
        
        for idx, val in enumerate(pref):
            if val == k:
                ans = idx + 1
            
            if val - k in seen:
                ans = max(ans, idx - seen[val - k])
            
            if val not in seen:
                seen[val] = idx
        return ans