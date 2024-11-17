# https://www.geeksforgeeks.org/problems/rotate-array-by-n-elements-1587115621/1

class Solution: 
    def rotateArr(self, arr, d):
        l = len(arr)
        d = d % l
        
        def reverse(start, end):
            while start < end:
                arr[start], arr[end] = arr[end], arr[start]
                start += 1
                end -= 1
        
        reverse(0, d - 1)
        reverse(d, l - 1)
        reverse(0, l - 1)