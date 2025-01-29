class Solution:
    def power(self, b: float, e: int) -> float:
        MOD = int(1e9) + 7
        
        n = -e if e < 0 else e
        x = b
        ans = 1.0
        while n:
            if n & 1:
                ans *= x
                n -= 1
            else:
                x *= x
                n = n >> 1
        if e < 0:
            ans = 1.0 / ans
        return ans