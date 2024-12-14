class Solution:   
    def peakElement(self,arr):
        n = len(arr)
        
        if n == 1 or arr[0] > arr[1]:
            return 0
        if arr[-1] > arr[-2]:
            return n - 1
        
        lo, hi = 1, n - 2
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            
            if arr[mid - 1] < arr[mid] and arr[mid] > arr[mid + 1]:
                return mid
            
            if arr[mid] < arr[mid + 1]:
                lo = mid + 1
            else:
                hi = mid - 1
        return -1