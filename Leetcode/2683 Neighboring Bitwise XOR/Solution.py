from typing import List
from functools import reduce
from operator import xor

class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        os0 = [0] 
        os1 = [1]
        for i in derived:
            os0.append(os0[-1] ^ i)
            os1.append(os1[-1] ^ i)
        return os0[-1] == os0[0] or os1[-1] == os1[0]

class Solution2:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        return reduce(xor, derived) == 0

'''
d0 = o0 ^ o1, d1 = o1 ^ o2, d2 = o2 ^ o3...
o1 = o0 ^ d0, o2 = o1 ^ d1 = o0 ^ d0 ^ d1, o3 = o2 ^ d2 = o0 ^ d0 ^ d1 ^ d2

On = O0 ^ XOR(derived)
XOR(derived) = On ^ O0 = Dn 
''' 