class Solution:
    def subarraySum(self, arr, target):
        l = 1
        local = 0
        
        for r in range(1, len(arr) + 1):
            local += arr[r - 1]
            
            while local > target:
                local -= arr[l - 1]
                l += 1
            
            if local == target:
                return [l, r]
        return [-1]