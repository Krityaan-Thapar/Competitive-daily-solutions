from typing import List

class Solution:
    def encode(self, strs: List[str]) -> str:
        ret = []
        for i in strs:
            l = '{:4}'.format(len(i))
            ret.append(l + i)
        return ''.join(ret)
    
    def decode(self, s: str) -> List[str]:
        ret = []
        i, n = 0, len(s)

        while i < n:
            size = int(s[i: i + 4])
            i += 4
            ret.append(s[i: i + size])
            i += size
        return ret