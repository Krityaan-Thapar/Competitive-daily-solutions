class Solution:
    def intersectionWithDuplicates(self, a, b):
        return list(set(a).intersection(set(b)))

class Solution2:
    def intersectionWithDuplicates(self, a, b):
        m = {}
        for i in a:
            m[i] = 1
        
        ans = []
        for i in b:
            if i in m and m[i] == 1:
                ans.append(i)
                m[i] += 1
        return ans