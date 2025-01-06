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

class Solution2:
    def maxLength(self, nums: List[int]) -> int:
        i, twos, threes, fives, sevens = 0, 0, 0, 0, 0
        for j, x in enumerate(nums):
            twos += x % 2 < 1
            threes += x % 3 < 1
            fives += x % 5 < 1
            sevens += x == 7
            if max(twos, threes, fives, sevens) > 1:
                twos -= nums[i] % 2 < 1
                threes -= nums[i] % 3 < 1
                fives -= nums[i] % 5 < 1
                sevens -= nums[i] == 7
                i += 1
        return max(2, len(nums) - i)

class Solution3:
    def maxLength(self, A: List[int]) -> int:
        N = len(A)
        ans = 2
        last = {}
        i = 0
        for j, x in enumerate(A):
            for p in prime_divisors(x):
                i = max(i, last.get(p, -1) + 1)
                last[p] = j
            ans = max(ans, j - i + 1)
        
        return ans

def prime_divisors(x):
    d = 2
    while d * d <= x:
        if x % d == 0:
            x //= d
            while x % d == 0:
                x //= d
            yield d
        d += 1 + d & 1
    
    if x > 1:
        yield x