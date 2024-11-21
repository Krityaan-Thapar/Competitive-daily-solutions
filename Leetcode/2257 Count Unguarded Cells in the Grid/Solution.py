from typing import List

class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        matrix = [[0 for _ in range(n)] for _ in range(m)]
        for x, y in walls:
            matrix[x][y] = 2
        for x,y in guards:
            matrix[x][y] = 1
        
        for i in range(m):
            convert = 0
            for j in range(n):
                if matrix[i][j] == 2:
                    convert = 0
                elif matrix[i][j] == 1:
                    convert = 3
                elif matrix[i][j] == 0:
                    matrix[i][j] = convert

            convert = 0
            for j in range(n - 1, -1, -1):
                if matrix[i][j] == 2:
                    convert = 0
                elif matrix[i][j] == 1:
                    convert = 3
                elif matrix[i][j] == 0:
                    matrix[i][j] = convert
        
        for j in range(n):
            convert = 0
            for i in range(m):
                if matrix[i][j] == 2:
                    convert = 0
                elif matrix[i][j] == 1:
                    convert = 3
                elif matrix[i][j] == 0:
                    matrix[i][j] = convert
            
            convert = 0
            for i in range(m - 1, -1, -1):
                if matrix[i][j] == 2:
                    convert = 0
                elif matrix[i][j] == 1:
                    convert = 3
                elif matrix[i][j] == 0:
                    matrix[i][j] = convert
        ans = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    ans += 1
        return ans