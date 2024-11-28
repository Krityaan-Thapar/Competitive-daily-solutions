class Solution:
    def myAtoi(self, s):
        sign = 1
        parse_start = False
        ans = 0
        
        for i in s:
            if not parse_start and i == " ":
                continue
            
            if not parse_start and i == '-':
                sign = -1
                parse_start = True
                continue
            
            if not i.isnumeric():
                break
            
            parse_start = True
            ans *= 10
            ans += int(i)
            
            if sign == -1 and ans > 1 << 31:
                return -1 * (1 << 31)
            
            if sign == 1 and ans > (1 << 31) - 1:
                return (1 << 31) - 1
        return ans * sign
