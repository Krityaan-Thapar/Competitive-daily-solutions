from typing import List
from collections import defaultdict

class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        m = defaultdict(int)
        tot = 0
        ans = -1 * int(1e7)
        
        for i in nums:
            tot += i
            m[i] += 1
        
        for i in nums:
            left = tot - i
            m[i] -= 1
            if left % 2 == 0 and m[left // 2] != 0:
                ans = max(ans, i)
            m[i] += 1
        return ans