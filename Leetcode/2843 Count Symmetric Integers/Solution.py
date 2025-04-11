class Solution:
    # brute force + stupid optimisations
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        num = max(low, 10)
        ans = 0
        while num <= high:
            if 100 <= num <= 999:
                num = 1000
                continue
            
            if 10 <= num <= 99:
                if num % 10 == num // 10:
                    ans += 1
                    num += 11
                    continue
            
            s1 = num % 10 + (num % 100) // 10
            s2 = num // 1000 + (num // 100) % 10
            if s1 == s2:
                ans += 1
            num += 1
        return ans