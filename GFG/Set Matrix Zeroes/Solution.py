class Solution:
    def setMatrixZeroes(self, mat):
        firstRowFlag = False 
        firstColFlag = False
        r, c = len(mat), len(mat[0])
        
        for i in range(r):
            if mat[i][0] == 0:
                firstColFlag = True
        
        for i in range(c):
            if mat[0][i] == 0:
                firstRowFlag = True
        
        for i in range(1, r):
            for j in range(1, c):
                if mat[i][j] == 0:
                    mat[0][j] = 0
                    mat[i][0] = 0
        
        for i in range(1, r):
            for j in range(1, c):
                if mat[0][j] == 0 or mat[i][0] == 0:
                    mat[i][j] = 0
        
        if firstColFlag:
            for i in range(r):
                mat[i][0] = 0
        
        if firstRowFlag:
            for i in range(c):
                mat[0][i] = 0