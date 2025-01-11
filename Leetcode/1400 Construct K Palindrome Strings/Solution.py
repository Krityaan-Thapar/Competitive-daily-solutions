from collections import Counter
class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        n = len(s)
        if k == n:
            return True
        
        if k > n:
            return False
        
        freq = Counter(s)
        s = 0
        for i in freq:
            if freq[i] % 2 == 1:
                s += 1
        
        return s <= k