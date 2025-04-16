from typing import List
from collections import defaultdict

class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        # eg 2 makes it seem that we can't decide whether to grow or shrink
        # but a valid subarray is good for the whole array to its right

        N = len(nums)
        left = curr_pairs = ans = 0
        freq = defaultdict(int)

        for right in range(N):
            curr_pairs += freq[nums[right]]
            freq[nums[right]] += 1

            while curr_pairs >= k:
                ans += N - right
                curr_pairs -= (freq[nums[left]] - 1)
                freq[nums[left]] -= 1
                left += 1
        
        return ans