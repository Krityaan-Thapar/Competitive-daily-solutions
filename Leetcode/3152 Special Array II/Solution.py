from typing import List

class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        ans = []
        dp = []
        dp.append(1)
        subarray_sum = 1
        
        for i in range(len(nums) - 1):
            j = i + 1
            par_i = nums[i] % 2
            par_j = nums[j] % 2
            if par_i != par_j:
                subarray_sum += 1
            dp.append(subarray_sum)
        
        for q in queries:
            s, e = q[0], q[1]
            if s == e:
                ans.append(True)
                continue

            ql = e - s
            if q != (dp[e] - dp[s]):
                ans.append(False)
                continue
            ans.append(True)
        return ans