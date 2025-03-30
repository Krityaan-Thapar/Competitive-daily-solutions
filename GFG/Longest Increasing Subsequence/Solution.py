class Solution:
    def lis(self, arr):
        n = len(arr)
        bleh = [1 for _ in range(n)]
        for i in range(n):
            for j in range(i):
                if arr[i] > arr[j]:
                    bleh[i] = max(bleh[i], bleh[j] + 1)
        return max(bleh)