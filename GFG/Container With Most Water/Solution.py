class Solution:
    def maxWater(self, arr):
        l, r = 0, len(arr) - 1
        ans = 0
        
        while l < r:
            ans = max(ans, (r - l) * min(arr[l], arr[r]))
            if arr[l] <= arr[r]:
                l += 1
            else:
                r -= 1
        return ans