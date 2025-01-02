from typing import List
from collections import defaultdict
from math import gcd

class Solution:
    def numberOfSubsequences(self, nums: List[int]) -> int:
        freq = defaultdict(int)
        ans = 0
        n = len(nums)
        for r in range(4, n):
            p = 0
            q = r - 2
            while p < q - 1:
                g = gcd(nums[p], nums[q])
                key = (nums[p] // g, nums[q] // g)
                freq[key] += 1
                p += 1
            
            for s in range(r + 2, n):
                g = gcd(nums[s], nums[r])
                key = (nums[s] // g, nums[r] // g)
                ans += freq[key]
        return ans