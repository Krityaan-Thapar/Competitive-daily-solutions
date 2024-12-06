from typing import List

class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        ans, s = 0, 0
        b = set(banned)
        for i in range(1, n + 1):
            if i in b:
                continue
            s += i
            if s > maxSum:
                break
            ans += 1
        return ans