class Solution:
    def solveSudoku(self, mat):
        def check(entry, x, y):
            for i in range(9):
                if mat[i][y] == entry or mat[x][i] == entry:
                    return False
            
            grid_x, grid_y = 3 * (x // 3), 3 *  (y // 3)
            for dx in range(3):
                for dy in range(3):
                    if mat[grid_x + dx][grid_y + dy] == entry:
                        return False
            return True
        
        def backtrack(x, y):
            if x == 9:
                return True
            
            nx, ny = x, y + 1
            if y == 8:
                nx = x + 1
                ny = 0
            
            if mat[x][y] != 0:
                return backtrack(nx, ny)
            
            for i in range(1, 10):
                if check(i, x, y):
                    mat[x][y] = i
                    if backtrack(nx, ny):
                        return True
                    mat[x][y] = 0
        
        backtrack(0, 0)