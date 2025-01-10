from collections import defaultdict
class Solution:
    def countDistinct(self, arr, k):
        freq = defaultdict(int)
        l = 0 
        ans = []
        for r in range(len(arr)):
            freq[arr[r]] += 1
            if r - l + 1 == k:
                ans.append(len(freq))
                freq[arr[l]] -= 1
                
                if freq[arr[l]] == 0:
                    freq.pop(arr[l])
                l += 1
        return ans