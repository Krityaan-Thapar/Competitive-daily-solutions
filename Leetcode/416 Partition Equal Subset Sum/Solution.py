from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        S, N = sum(nums), len(nums)
        if S % 2 != 0:
            return False
        target = S // 2
        
        cache = [[None for _ in range(target + 1)] for _ in range(N)]
        for i in range(N):
            cache[i][0] = True
        
        def solver(idx, target):
            if idx == N or target < 0:
                return False

            if cache[idx][target] is not None:
                return cache[idx][target]

            take = solver(idx + 1, target - nums[idx])
            no_take = solver(idx + 1, target)
            cache[idx][target] = take or no_take
            return cache[idx][target]
        return solver(0, target)

class Solution2:
    def canPartition(self, nums: List[int]) -> bool:
        S, N = sum(nums), len(nums)
        if S % 2 != 0:
            return False
        target = S // 2
        
        cache = [False for _ in range(target + 1)]
        cache[0] = True
        for i in range(N):
            for j in range(target, nums[i] - 1, -1):
                cache[j] = cache[j] or cache[j - nums[i]]
        return cache[target]