class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        l1, l2 = len(str1), len(str2)
        if l1 < l2:
            return False
        
        ptr1, ptr2 = 0, 0
        while ptr2 < l2:
            flag = False
            while ptr1 < l1:
                orig = str1[ptr1]
                cycled = chr((ord(orig) - ord('a') + 1) % 26 + ord('a'))
                if orig == str2[ptr2] or cycled == str2[ptr2]:
                    flag = True
                    ptr1 += 1
                    break
                ptr1 += 1
            
            if not flag:
                return False
            ptr2 += 1
        return True