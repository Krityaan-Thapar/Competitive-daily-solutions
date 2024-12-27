from typing import List

class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        ans = 0
        curr = None
        
        for idx, i in enumerate(values):
            if curr is None:
                curr = i
                continue
            
            local = i - idx
            ans = max(ans, curr + local)
            curr = max(curr, i + idx)
        return ans