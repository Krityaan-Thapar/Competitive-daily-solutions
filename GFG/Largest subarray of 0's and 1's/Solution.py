class Solution:
    def maxLen(self, arr):
        seen = {}
        local = 0
        ans = 0
        
        for i in range(len(arr)):
            if arr[i] == 0:
                local -= 1
            else:
                local += 1
            
            if local == 0:
                ans = i + 1
            
            if local in seen:
                ans = ans(max, i - seen[local])
            else:
                seen[local] = i
            
        return ans