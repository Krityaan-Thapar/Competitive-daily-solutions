from typing import List

class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        ans = -int(1e15)
        n = len(nums)
        for i in range(n):
            ans = max(ans, abs(nums[i] - nums[(i + 1) % n]))
        return ans