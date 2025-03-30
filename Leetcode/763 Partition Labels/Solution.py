from typing import List

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        ans = []
        lasts = [-1 for _ in range(26)]
        for idx, i in enumerate(s):
            lasts[ord(i) - ord('a')] = idx

        part_end = 0
        curr = 0
        for idx, i in enumerate(s):
            if idx > part_end:
                ans.append(curr)
                curr = 0
            part_end = max(part_end, lasts[ord(i) - ord('a')])
            curr += 1
        ans.append(curr)
        return ans