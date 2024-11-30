class Solution:
    def nextPermutation(self, arr):
        n = len(arr)
        i, j = n - 2, n - 1
        
        while i >= 0 and arr[i] >= arr[i + 1]:
            i -= 1
        
        if i >= 0:
            while arr[j] <= arr[i]:
                j -= 1
            arr[i], arr[j] = arr[j], arr[i]
        
        arr[i + 1:] = reversed(arr[i + 1:])