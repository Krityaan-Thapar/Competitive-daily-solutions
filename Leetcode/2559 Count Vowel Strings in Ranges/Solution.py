from typing import List

class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        acc = [0]
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        for i in words:
            if i[0] in vowels and i[-1] in vowels:
                acc.append(acc[-1] + 1)
            else:
                acc.append(acc[-1])
        
        ans = []
        for l, r in queries:
            ans.append(acc[r + 1] - acc[l])
        return ans