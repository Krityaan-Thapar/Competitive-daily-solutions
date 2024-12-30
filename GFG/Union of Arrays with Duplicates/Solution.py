class Solution:
    def findUnion(self, a, b):
        return len(set(a).union(set(b)))

class Solution2:    
    def findUnion(self, a, b):
        ans = set()
        for i in a:
            ans.add(i)
        for i in b:
            ans.add(i)
        return len(ans)