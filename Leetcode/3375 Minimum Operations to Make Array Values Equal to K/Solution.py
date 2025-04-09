from typing import List

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        if k > nums[0]:
            return -1
        S = set(nums)
        
        if k == nums[0]:
            return len(S) - 1
        return len(S)

class Solution2:
    def minOperations(self, nums: List[int], k: int) -> int:
        M = min(nums)
        S = set(nums)
        if k > M:
            return -1
        elif k == M:
            return len(S) - 1
        return len(S)