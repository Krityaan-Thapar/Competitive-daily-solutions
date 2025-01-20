from typing import List

class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        r, c = len(mat), len(mat[0])
        row_paints = [0 for _ in range(r)]
        col_paints = [0 for _ in range(c)]
        arr_mx = [[] for _ in range(len(arr))]
        
        for i in range(r):
            for j in range(c):
                arr_mx[mat[i][j] - 1] = [i, j]

        for idx, val in enumerate(arr):
            x, y = arr_mx[val - 1]
            row_paints[x] += 1
            col_paints[y] += 1
            if row_paints[x] == c or col_paints[y] == r:
                return idx
        return -1 