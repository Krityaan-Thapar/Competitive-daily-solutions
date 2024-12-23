class Solution:
    def searchMatrix(self, mat, x):
        r, c = len(mat), len(mat[0])
        lo, hi = 0, r * c - 1
        
        while lo <= hi:
            mid = (lo + hi) // 2
            ci, cj = mid // c, mid % c
            
            if x == mat[ci][cj]:
                return True
            elif x < mat[ci][cj]:
                hi = mid - 1
            else:
                lo = mid + 1
        return False