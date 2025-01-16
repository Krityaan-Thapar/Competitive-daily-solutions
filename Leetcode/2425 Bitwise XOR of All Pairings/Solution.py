from collections import defaultdict
from typing import List

class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        ans = 0
        l1, l2 = len(nums1), len(nums2)
        f = defaultdict(int)
        
        for i in nums1:
            f[i] += l2
        for i in nums2:
            f[i] += l1
        
        for i in f:
            if f[i] % 2 != 0:
                ans = ans ^ i
        return ans

class Solution2:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        l1, l2 = len(nums1), len(nums2)
        a,b = 0, 0

        if l2 % 2 != 0:
            for i in nums1:
                a = a ^ i

        if l1 % 2 != 0:
            for i in nums2:
                b = b ^ i
        return a ^ b