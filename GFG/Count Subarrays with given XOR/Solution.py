from collections import defaultdict

class Solution:
    def subarrayXor(self, arr, k):
        ans = 0
        local = 0
        m = defaultdict(int)
        
        for i in arr:
            local = local ^ i
            if local == k:
                ans += 1
            
            if local ^ k in m:
                ans += m[local ^ k]
            
            m[local] += 1
        return ans