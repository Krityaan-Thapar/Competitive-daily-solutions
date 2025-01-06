class Solution:
    def hasMatch(self, s: str, p: str) -> bool:
        n = len(s)
        cands = p.split('*')
        l1, l2 = len(cands[0]), len(cands[1])
        
        if cands[0] == "":
            x = s.find(cands[1])
            if x == -1:
                return False
            return True
        
        if cands[1] == "":
            x = s.find(cands[0])
            if x == -1:
                return False
            return True

        earliest1 = -1
        for i in range(n - l1):
            if s[i:i + l1] == cands[0]:
                earliest1 = i
                break
        
        if earliest1 == -1:
            return False
        
        latest2 = -1
        for i in range(n, l2, -1):
            if s[i - l2: i] == cands[1]:
                latest2 = i - l2
                break
        
        if latest2 == -1:
            return False
        
        if earliest1 + l1 <= latest2:
            return True
        return False