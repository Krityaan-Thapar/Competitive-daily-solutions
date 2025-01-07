from typing import List

class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        n = len(words)
        ans = []
        for i in range(n):
            for j in range(n):
                if j == i:
                    continue
                if words[i] in words[j]:
                    ans.append(words[i])
                    break
        return ans

class Solution2:
    def stringMatching(self, words: List[str]) -> List[str]:
        r = ' '.join(words)
        s = [i for i in words if r.count(i)>1]
        return s