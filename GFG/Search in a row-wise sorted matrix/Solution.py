class Solution:
    def searchRowMatrix(self, mat, x):
        r, c = len(mat), len(mat[0])
        for i in range(r):
            lo, hi = 0, c - 1
            while lo <= hi:
                j = (lo + hi) // 2
                
                if mat[i][j] == x:
                    return True
                elif x < mat[i][j]:
                    hi = j - 1
                else:
                    lo = j + 1
        return False