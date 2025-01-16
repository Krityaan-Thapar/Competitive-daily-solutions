from typing import List

class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        r, c = len(coins), len(coins[0])
        cache = [[[0 for _ in range(3)] for _ in range(c)] for _ in range(r)]
        has_cache = [[[False for _ in range(3)] for _ in range(c)] for _ in range(r)]

        for k in range(3):   
            has_cache[r - 1][c - 1][k] = True
            if coins[r - 1][c - 1] < 0 and k > 0:
                cache[r - 1][c - 1][k] = 0
            else:
                cache[r - 1][c - 1][k] = coins[r - 1][c - 1]

        def solver(i, j, k):
            if has_cache[i][j][k]:
                return cache[i][j][k]
            
            right = coins[i][j] + solver(i, j + 1, k) if j + 1 < c else -int(1e15)
            down = coins[i][j] + solver(i + 1, j, k) if i + 1 < r else -int(1e15)
            if coins[i][j] < 0 and k > 0:
                right = max(solver(i, j + 1, k - 1), right) if j + 1 < c else -int(1e15)
                down = max(solver(i + 1, j, k - 1), down) if i + 1 < r else -int(1e15)
            
            has_cache[i][j][k] = True
            cache[i][j][k] = max(right, down)
            return cache[i][j][k]

        return solver(0, 0, 2)

class Solution2:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        r, c = len(coins), len(coins[0])
        cache = [[[0 for _ in range(3)] for _ in range(c)] for _ in range(r)]
        
        for k in range(3):
            cache[r - 1][c - 1][k] = coins[r - 1][c - 1]
            if coins[r - 1][c - 1] < 0 and k > 0:
                cache[r - 1][c - 1][k] = 0

        for i in range(r - 1, -1, -1):
            for j in range(c - 1, -1, -1):
                if i == r - 1 and j == c - 1:
                    continue
                
                for k in range(3):
                    right = coins[i][j] + cache[i][j + 1][k] if j + 1 < c else -int(1e15)
                    down = coins[i][j] + cache[i + 1][j][k] if i + 1 < r else -int(1e15)
                    if coins[i][j] < 0 and k > 0:
                        right = max(cache[i][j + 1][k - 1], right) if j + 1 < c else -int(1e15)
                        down = max(cache[i + 1][j][k - 1], down) if i + 1 < r else -int(1e15)
                    cache[i][j][k] = max(right, down)
        return cache[0][0][2]