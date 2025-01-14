from typing import List
class Solution:
    def zigzagTraversal(self, grid: List[List[int]]) -> List[int]:
        ans = []
        r, c = len(grid), len(grid[0])
        parity = 1

        for i in range(r):
            for j in range(c):
                x = j
                if i % 2 != 0:
                    x = c - 1 - j
                
                if parity:
                    ans.append(grid[i][x])
                parity ^= 1
        return ans
    
class Solution2:
    def zigzagTraversal(self, grid: List[List[int]]) -> List[int]:
        res = []
        for i, r in enumerate(grid):
            res += r[::-1] if i % 2 else r
        return res[::2]