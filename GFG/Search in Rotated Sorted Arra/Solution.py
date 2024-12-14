class Solution:
    def search(self,arr,key):
        lo, hi = 0, len(arr) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if arr[mid] == key:
                return mid
            
            if arr[lo] <= arr[mid]:
                if key >= arr[lo] and key < arr[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1
            else:
                if key <= arr[hi] and key > arr[mid]:
                    lo = mid + 1
                else:
                    hi = mid - 1
        return -1