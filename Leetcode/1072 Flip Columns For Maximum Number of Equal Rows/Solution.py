import collections
from typing import List

class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        patterns = collections.Counter()
        for row in matrix:
            if row[0] == 1:
                normalized_row = tuple(1-x for x in row)
            else:
                normalized_row = tuple(row)
            patterns[normalized_row] = patterns[normalized_row] + 1
        return max(patterns.values())