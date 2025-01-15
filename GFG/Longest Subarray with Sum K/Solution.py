from itertools import accumulate
from collections import defaultdict
class Solution:
    def longestSubarray(self, arr, k):  
        prefix = [0]
        for i in arr:
            prefix.append(prefix[-1] + i)
        seen = defaultdict(int)
        ans = 0
        
        for idx, curr in enumerate(prefix):
            target = curr - k
            if target in seen:
                ans = max(ans, idx - seen[target])
            
            if curr not in seen:
                seen[curr] = idx
        return ans