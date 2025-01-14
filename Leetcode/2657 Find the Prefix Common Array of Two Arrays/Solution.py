from typing import List

class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        ans = []
        n = len(A)
        seen = set([i for i in range(1, n + 1)])

        for i in range(n - 1, -1, -1):
            ans.append(len(seen))
            if A[i] in seen:
                seen.remove(A[i])
            if B[i] in seen:
                seen.remove(B[i])
        return ans[::-1]