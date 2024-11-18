from typing import List
from itertools import accumulate

class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        L = len(code)
        if k == 0:
            return [0 for _ in range(L)]
        
        ans = []
        if k < 0:
            v = abs(k)
            for i in range(L):
                local = 0
                for x in range(i - v, i):
                    local += code[x %  L]
                ans.append(local)
        else:
            for i in range(L):
                local = 0
                for x in range(i + 1, i + k + 1):
                    local += code[x % L]
                ans.append(local)
        return ans

class Solution2:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n, code = len(code), list(accumulate(code+code))
        if k < 0:
            return [code[i] - code[i+k] for i in range(n-1, 2*n-1)]
        if k > 0:
            return [code[i+k] - code[i] for i in range(n)]
        return [0] * n