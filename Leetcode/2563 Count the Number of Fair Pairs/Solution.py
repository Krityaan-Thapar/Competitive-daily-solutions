from typing import List
from bisect import bisect_right

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        
        def bleh(val):
            ans = 0
            for idx, i in enumerate(nums):
                ans += bisect_right(nums, val - i, hi = idx)
            return ans
        
        return bleh(upper) - bleh(lower - 1)

class Solution2:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        
        def pairs_less_than_bound(bound):
            l, r, ans = 0, len(nums) - 1, 0
            while l < r:
                x = nums[l] + nums[r]
                if x < bound:
                    ans += r - l
                    l += 1
                else:
                    r -= 1
            return ans
        return pairs_less_than_bound(upper + 1) - pairs_less_than_bound(lower)