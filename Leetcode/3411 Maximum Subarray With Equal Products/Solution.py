from typing import List
from math import gcd

class Solution:
    def maxLength(self, nums: List[int]) -> int:
        def lcm_of_array(arr):
            lcm = arr[0]
            for i in range(1, len(arr)):
                num1 = lcm
                num2 = arr[i]
                gd = gcd(num1, num2)
                lcm = (lcm * arr[i]) // gd
            return lcm
        
        def gcd_of_array(arr):
            gd = 0
            for i in range(len(arr)):
                gd = gcd(gd, arr[i])
            return gd
        
        def prod_of_array(arr):
            prod = 1
            for i in arr:
                prod *= i
            return prod

        n = len(nums)
        ans = 0
        for i in range(n):
            for j in range(i + 1, n + 1):
                p = prod_of_array(nums[i:j])
                g = gcd_of_array(nums[i:j])
                l = lcm_of_array(nums[i:j])
                if p == g * l:
                    ans = max(ans, j - i)
        return ans