from itertools import reduce
import operator
from typing import List

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        return reduce(operator.__or__, nums) * (1 << (len(nums) - 1))