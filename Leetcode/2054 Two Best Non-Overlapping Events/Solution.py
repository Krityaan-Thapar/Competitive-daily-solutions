from typing import List

class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        sweep = []
        for start, end, val in events:
            sweep.append((start, True, val))
            sweep.append((end + 1, False, val))
        sweep.sort()

        ans = 0
        m = 0
        for t, is_start, val in sweep:
            if is_start:
                ans = max(ans, val + m)
            else:
                m = max(m, val)
        return ans