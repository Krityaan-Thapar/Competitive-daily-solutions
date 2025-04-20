class Solution:
    def missingNum(self, arr):
        N = len(arr)
        xor = 0
        for i in range(1, N + 2):
            xor ^= i
        
        for i in arr:
            xor ^= i
        return xor

class Solution2:
    def missingNum(self, arr):
        n = len(arr) + 1
        exp = (n * (n + 1)) // 2
        return exp - sum(arr)