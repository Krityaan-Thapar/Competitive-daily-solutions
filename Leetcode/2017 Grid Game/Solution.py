from typing import List

class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        l = len(grid[0])
        p = [0, 0]
        s = [sum(grid[0]), sum(grid[1])]

        ans = max(s)
        for i in range(l):
            # if p1 dives at i, what's the max that p2 can take
            # ans = max(p[1], s[0])
            s[0] -= grid[0][i]
            s[1] -= grid[1][i]
            dive_now_ans = max(p[1], s[0])
            ans = min(ans, dive_now_ans)
            p[0] += grid[0][i]
            p[1] += grid[1][i]
        return ans