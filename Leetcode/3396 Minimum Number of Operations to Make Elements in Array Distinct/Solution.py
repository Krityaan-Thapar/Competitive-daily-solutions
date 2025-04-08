from typing import List

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        N = len(nums)
        seen = set()
        for idx in range(N - 1, -1, -1):
            if nums[idx] in seen:
                break
            seen.add(nums[idx])
        
        if idx == 0 and len(seen) == N:
            return 0
        
        idx += 1
        if idx % 3 == 0:
            return idx // 3
        return idx // 3 + 1

class Solution2:
    def minimumOperations(self, nums: List[int]) -> int:
        N = len(nums)
        seen = set()
        for idx in range(N - 1, -1, -1):
            if nums[idx] in seen:
                return idx // 3 + 1
            seen.add(nums[idx])
        return 0