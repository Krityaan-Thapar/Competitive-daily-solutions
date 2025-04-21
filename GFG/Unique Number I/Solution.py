from operator import xor
from functools import reduce

class Solution:
    def findUnique(self, arr):
        return reduce(xor, arr)