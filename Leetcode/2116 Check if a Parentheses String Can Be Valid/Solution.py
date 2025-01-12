class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        n = len(s)
        if n % 2 == 1: 
            return False
        
        wilds, o, c = 0, 0, 0
        for i in range(n - 1, -1, -1):
            if locked[i] == '0': 
                wilds += 1
            elif s[i] == '(': 
                o += 1
            elif s[i] == ')': 
                c += 1
            
            if wilds - o + c < 0: 
                return False
        
        wilds, o, c = 0, 0, 0
        for i in range(n):
            if locked[i] == '0': 
                wilds += 1
            elif s[i] == '(': 
                o += 1
            elif s[i] == ')': 
                c += 1
            
            if wilds + o - c < 0: 
                return False 
        return True