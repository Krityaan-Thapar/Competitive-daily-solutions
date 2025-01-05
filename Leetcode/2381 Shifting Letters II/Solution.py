from typing import List

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        line = [0 for _ in range(n + 1)]
        target = list(s)

        for s, e, d in shifts:
            if d == 0:
                line[s] -= 1
                line[e + 1] += 1
            else:
                line[s] += 1
                line[e + 1] -= 1
        
        offset = 0
        for i in range(n):
            offset += line[i]
            tmp = ord(target[i]) - ord('a')
            target[i] = chr((tmp + offset) % 26 + ord('a'))
        return ''.join(target)