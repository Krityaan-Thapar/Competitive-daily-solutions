from collections import defaultdict
from typing import List

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0
        freq = defaultdict(int)
        l = 0
        rolling = 0

        for r in range(n):
            rolling += nums[r]
            freq[nums[r]] += 1
            if r - l == k - 1:
                if len(freq) == k:
                    ans = max(ans, rolling)
                
                freq[nums[l]] -= 1
                rolling -= nums[l]
                if freq[nums[l]] == 0:
                    del freq[nums[l]]

                l += 1
        return ans