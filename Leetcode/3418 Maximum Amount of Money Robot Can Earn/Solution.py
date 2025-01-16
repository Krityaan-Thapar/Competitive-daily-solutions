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

class Solution3:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        r, c = len(coins), len(coins[0])
        curr = [[-int(1e15) for _ in range(3)] for _ in range(c)]

        for k in range(3):
            curr[0][k] = coins[0][0]
        if coins[0][0] < 0:
            curr[0][0] = 0
            curr[0][1] = 0
        
        for j in range(1, c):
            for k in range(3):
                curr[j][k] = max(curr[j][k], curr[j - 1][k] + coins[0][j])
                if coins[0][j] < 0 and k > 0:
                    curr[j][k - 1] = max(curr[j][k - 1], curr[j - 1][k])
        
        for i in range(1, r):
            prev = [row[:] for row in curr]
            curr = [[-int(1e15) for _ in range(3)] for _ in range(c)]
            for k in range(3):
                curr[0][k] = max(curr[0][k], prev[0][k] + coins[i][0])
                if coins[i][0] < 0 and k > 0:
                    curr[0][k - 1] = max(curr[0][k - 1], prev[0][k])
            
            for j in range(1, c):
                for k in range(3):
                    curr[j][k] = max(curr[j][k], curr[j - 1][k] + coins[i][j], prev[j][k] + coins[i][j])
                    if coins[i][j] < 0 and k > 0:
                        curr[j][k - 1] = max(curr[j][k - 1], curr[j - 1][k], prev[j][k])
        return max(curr[-1])