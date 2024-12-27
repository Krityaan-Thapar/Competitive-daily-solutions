from collections import defaultdict

class Solution:
    def countPairs(self, arr, target):
        freq = defaultdict(int)
        ans = 0
        
        for i in arr:
            ans += freq[i]
            freq[target - i] += 1
        
        return ans