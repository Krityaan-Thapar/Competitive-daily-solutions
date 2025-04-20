class Solution:
    def findDuplicate(self, arr):
        xor = 0
        N = len(arr)
        for i in range(1, N):
            xor = xor ^ i
        
        for i in arr:
            xor = xor ^ i
        return xor

class Solution2:
    def findDuplicate(self, arr):
        for i in arr:
            arr[abs(i) - 1] *= -1
        
        for idx, i in enumerate(arr):
            if i > 0:
                return idx + 1