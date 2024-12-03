from typing import List

class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        splits  = []
        prev = 0
        for i in spaces:
            splits.append(s[prev : i])
            prev = i
        splits.append(s[prev:])
        return ' '.join(splits)