class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        b1 = num1.bit_count()
        b2 = num2.bit_count()
        if b1 == b2:
            return num1
        
        ans = num1
        target = b2 - b1
        for i in range(30):
            raiser = 1 << i
            if num1 & raiser > 0:
                if target < 0:
                    ans = ans ^ raiser
                    target += 1
            else:
                if target > 0:
                    ans = ans ^ raiser
                    target -= 1
        return ans