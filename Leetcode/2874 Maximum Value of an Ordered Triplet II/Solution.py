from typing import List

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        highest, diff = 0, 0
        ans = 0

        for i in range(n):
            local = nums[i] * diff
            if local > ans:
                ans = local
            
            val = highest - nums[i]
            if val > diff:
                diff = val
            if nums[i] > highest:
                highest = nums[i]
        
        return ans