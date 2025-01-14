class Solution:
    def findEquilibrium(self, arr):
        s = sum(arr)
        p = 0
        for idx, i in enumerate(arr):
            s -= i
            if s == p:
                return idx
            p += i
        return -1