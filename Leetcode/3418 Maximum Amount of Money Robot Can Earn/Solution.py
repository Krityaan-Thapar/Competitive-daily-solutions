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
            
            right = solver(i, j + 1, k) if j + 1 < c else -int(1e15)
            down = solver(i + 1, j, k) if i + 1 < r else -int(1e15)
            right_neut = -int(1e15)
            down_neut = -int(1e15)
            if coins[i][j] < 0 and k > 0:
                right_neut = solver(i, j + 1, k - 1) if j + 1 < c else -int(1e15)
                down_neut = solver(i + 1, j, k - 1) if i + 1 < r else -int(1e15)       
            
            curr = coins[i][j]
            ans = max(right + curr, down + curr, right_neut, down_neut)
            has_cache[i][j][k] = True
            cache[i][j][k] = ans
            return cache[i][j][k]

        return solver(0, 0, 2)

coins = [[-16, 4, 1, -1],[11, 9, 3, 3],[-6, 17, -19, 9],[14, -17, -19, -13]]
obj = Solution()
print(obj.maximumAmount(coins))