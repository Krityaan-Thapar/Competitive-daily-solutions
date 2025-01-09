from typing import List

class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        l = len(pref)
        ans = 0
        for w in words:
            if l <= len(w) and w[:l] == pref:
                ans += 1
        return ans

class Solution2:
    def prefixCount(self, words: List[str], pref: str) -> int:
        return sum(1 if i.startswith(pref) else 0 for i in words)

class Solution3:
    def prefixCount(self, words: List[str], pref: str) -> int:
        def hash(s):
            p, m, h, p_pow = 31, int(1e9) + 7, 0, 1
            for i in s:
                h = (h + (ord(i) - ord('a') + 1) * p_pow) % m
                p_pow = (p_pow * p) % m
            return h

        hash_pref = hash(pref)
        L = len(pref)
        ans = 0
        for w in words:
            if L <= len(w) and hash(w[:L]) == hash_pref:
                ans += 1
        return ans 

class Solution4:
    def prefixCount(self, words: List[str], pref: str) -> int:
        def sw(a, b):
            ptr1, ptr2 = 0, 0
            l_a = len(a)
            l_b = len(b)
            if l_a > l_b:
                return False
            
            while ptr1 < l_a and a[ptr1] == b[ptr2]:
                ptr1 += 1
                ptr2 += 1
            return ptr1 == len(a)
        
        return sum(sw(pref, w) for w in words) 