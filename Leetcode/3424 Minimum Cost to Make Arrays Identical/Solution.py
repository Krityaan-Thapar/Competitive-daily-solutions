from typing import List

class Solution:
    def minCost(self, arr: List[int], brr: List[int], k: int) -> int:
        tmp_a = sorted(arr)
        tmp_b = sorted(brr)
        rearranged = k
        same = 0
        
        for i in range(len(arr)):
            rearranged += abs(tmp_a[i] - tmp_b[i])
            same += abs(arr[i] - brr[i])
        return min(rearranged, same)