from itertools import permutations
class Solution:
    def findPermutation(self, s):
        seen = set()
        ans = []
        for it in permutations(s):
            if it in seen:
                continue
            seen.add(it)
            
            perm = [i for i in it]
            ans.append("".join(perm))
        return ans
