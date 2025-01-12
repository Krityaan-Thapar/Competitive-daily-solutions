class Solution:
    def maxWater(self, arr):
        n = len(arr)
        if n < 3:
            return 0
        
        lMax, rMax = arr[0], arr[n - 1]
        l, r = 1, n - 2
        ans = 0
        
        while l <= r:
            if lMax <= rMax:
                ans += max(0, lMax - arr[l])
                lMax = max(lMax, arr[l])
                l += 1
            else:
                ans += max(0, rMax - arr[r])
                rMax = max(rMax, arr[r])
                r -= 1
        return ans