from typing import List

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        seen = set()
        seen2 = set()
        for i in arr:
            if i in seen2 or 2 * i in seen:
                return True
            seen.add(i)
            seen2.add(2 * i)
        return False