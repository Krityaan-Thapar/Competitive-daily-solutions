from sortedcontainers import SortedList
from typing import List

class Solution:
    def goodTriplets(self, A: List[int], B: List[int]) -> int:
        # Index of a (from A) in B.
        pos = [0] * len(A)               
        for idx, b in enumerate(B):
            pos[b] = idx
        
        # Build pre_a[i]: number of elements on a[i]'s left in both A and B.
        # pos_in_b: sorted indexes (in B) of all the visited elements in A.
        pos_in_b, pre_a = SortedList([pos[A[0]]]), [0]      
        for a in A[1:]:       
            pos_in_b.add(pos[a])
            pre_a.append(pos_in_b.bisect_left(pos[a]))
    
        # Build suf_a[i]: number of elements on a[i]'s right in both A and B.
        pos_in_b, suf_a = SortedList([pos[A[-1]]]), [0]
        for a in reversed(A[:len(A)-1]):
            idx = pos_in_b.bisect(pos[a])
            suf_a.append(len(pos_in_b) - idx)
            pos_in_b.add(pos[a])
        suf_a.reverse()
        
        # Sum up all unique triplets centered on A[i].
        ans = 0
        for x, y in zip(pre_a, suf_a):
            ans += x * y
        return ans

class FenwickTree:
    def __init__(self, size):
        self.tree = [0] * (size + 1)

    def update(self, index, delta):
        index += 1
        while index <= len(self.tree) - 1:
            self.tree[index] += delta
            index += index & -index

    def query(self, index):
        index += 1
        res = 0
        while index > 0:
            res += self.tree[index]
            index -= index & -index
        return res


class Solution2:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        pos2, reversedIndexMapping = [0] * n, [0] * n
        for i, num2 in enumerate(nums2):
            pos2[num2] = i
        for i, num1 in enumerate(nums1):
            reversedIndexMapping[pos2[num1]] = i
        tree = FenwickTree(n)
        res = 0
        for value in range(n):
            pos = reversedIndexMapping[value]
            left = tree.query(pos)
            tree.update(pos, 1)
            right = (n - 1 - pos) - (value - left)
            res += left * right
        return res