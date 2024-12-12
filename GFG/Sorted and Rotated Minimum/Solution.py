class Solution:
    def findMin(self, arr):
        lo = 0
        hi = len(arr) - 1
        
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if arr[mid] > arr[-1]:
                lo = mid + 1
            else:
                hi = mid - 1
        return arr[lo]