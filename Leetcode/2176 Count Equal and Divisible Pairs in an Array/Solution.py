from typing import List

class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        N = len(nums)
        ans = 0

        for j in range(N):
            for i in range(j):
                if nums[i] == nums[j] and (i * j) % k == 0:
                    ans += 1
        return ans