class Solution:
    def countFreq(self, arr, target):
        lo1 = 0
        hi1 = len(arr)
        while lo1 < hi1:
            mid = (lo1 + hi1) // 2
            if target < arr[mid]:
                hi1 = mid
            else:
                lo1 = mid + 1
        
        lo2 = 0
        hi2 = len(arr)
        while lo2 < hi2:
            mid = (lo2 + hi2) // 2
            if arr[mid] < target:
                lo2 = mid + 1
            else:
                hi2 = mid
        return lo1 - lo2
