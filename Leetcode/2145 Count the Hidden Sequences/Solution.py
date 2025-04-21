from typing import List

class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        hidden = [0]
        for i in differences:
            hidden.append(hidden[-1] + i)
        
        mi, ma = min(hidden), max(hidden)
        lowest_start = lower - mi
        highest_start = upper - ma
        
        if highest_start < lowest_start:
            return 0
        return highest_start - lowest_start + 1