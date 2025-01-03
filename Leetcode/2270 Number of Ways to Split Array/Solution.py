from itertools import accumulate
from typing import List

class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        prefix = list(accumulate(nums, initial = 0))
        suffix = list(accumulate(nums[::-1], initial = 0))[::-1]
        ans = 0

        for i in range(1, len(nums)):
            if prefix[i] >= suffix[i]:
                ans += 1
        return ans

class Solution2:
    def waysToSplitArray(self, nums: List[int]) -> int:
        l, r = 0, sum(nums)
        ans = 0
        for i in range(len(nums) - 1):
            l += nums[i]
            r -= nums[i]
            if l >= r:
                ans += 1
        return ans