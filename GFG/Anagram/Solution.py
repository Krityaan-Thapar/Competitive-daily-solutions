from collections import Counter

class Solution:
    def areAnagrams(self, s1, s2):
        if len(s1) != len(s2):
            return False
        
        d1 = Counter(s1)
        d2 = Counter(s2)
        
        for k, v in d1.items():
            if d2[k] != v:
                return False
        return True