from math import log2

class Solution:
    def smallestNumber(self, n: int) -> int:
        if n == 1:
            return 1
        a = int(log2(n))
        return (1 << (a + 1)) - 1

class Solution2:
    def smallestNumber(self, n: int) -> int:
        return (1 << n.bit_length()) - 1