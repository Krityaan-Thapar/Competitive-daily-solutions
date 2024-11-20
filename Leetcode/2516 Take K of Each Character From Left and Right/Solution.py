class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        n = len(s)
        count = [0 for _ in range(3)]
        
        for i in s:
            count[ord(i) - ord('a')] += 1
        
        if any(i < k for i in count):
            return -1
        
        m = 0
        l = 0
        for r in range(n):
            idx = ord(s[r]) - ord('a')
            count[idx] -= 1
            while count[idx] < k:
                count[ord(s[l]) - ord('a')] += 1
                l += 1
            m = max(m, r - l + 1)
        return n - m