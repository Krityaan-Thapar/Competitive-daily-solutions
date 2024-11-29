class Solution:
    def addBinary(self, s1, s2):
	    return bin(int(s1, 2) + int(s2, 2))[2:]

class Solution2:
    def addBinary(self, s1, s2):
        idx1 = 0
        while idx1 < len(s1) and s1[idx1] == '0':
            idx1 += 1
        idx2 = 0
        while idx2 < len(s2) and s2[idx2] == '0':
            idx2 += 1
        
        if idx1 == len(s1) and idx2 == len(s2):
            return '0'
        elif idx1 == len(s1):
            return s2[idx2:]
        elif idx2 == len(s2):
            return s1[idx1:]
        else:
            s1 = s1[idx1:]
            s2 = s2[idx2:]
        
        s1 = s1[::-1]
        s2 = s2[::-1]
        l1, l2 = len(s1), len(s2)
        
        ans = []
        carry = 0
        idx = 0
        while idx < l1 and idx < l2:
            val = carry + int(s1[idx]) + int(s2[idx])
            ans.append(str(val % 2))
            carry = val // 2
            idx += 1
        
        left = None
        if idx < l1:
            left = s1[idx:]
        else:
            left = s2[idx:]
        
        idx = 0
        while left and idx < len(left):
            val = carry + int(left[idx])
            ans.append(str(val % 2))
            carry = val // 2
            idx += 1
        
        if carry:
            ans.append('1')
        return ''.join(ans[::-1])