from collections import defaultdict
from typing import List
from bisect import bisect_left, bisect_right

class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        sweep = defaultdict(int)
        for i in nums:
            sweep[i - k] += 1
            sweep[i + k + 1] -= 1
        
        arr = [(k, v) for k, v in sweep.items()]
        arr.sort()
        ans, local = 0, 0
        for k, v in arr:
            local += v
            ans = max(ans, local)
        return ans

class Solution2:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        res = 0
        nums.sort()
        for x in range(max(nums) + 1):
            l = bisect_left(nums,x - k) 
            r = bisect_right(nums,x + k)
            res = max(res, r - l)
        return res

class Solution3:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()
        max_beauty = left = 0
        for right in range(len(nums)):
            while nums[left] + k < nums[right] - k:
                left += 1
            max_beauty = max(max_beauty, right - left + 1)
        return max_beauty

class Solution4:
    def maximumBeauty(self, nums: list[int], k: int) -> int:
        if len(nums) == 1:
            return 1

        max_value = max(nums)
        count = [0] * (max_value + 1)

        for num in nums:
            count[max(num - k, 0)] += 1
            if num + k + 1 <= max_value:
                count[num + k + 1] -= 1

        max_beauty = 0
        current_sum = 0
        for val in count:
            current_sum += val
            max_beauty = max(max_beauty, current_sum)
        return max_beauty