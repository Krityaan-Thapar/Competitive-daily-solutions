class Solution:
    def sort012(self, arr):
        n = len(arr)
        zero, two = -1, n
        
        for i in arr:
            if i == 0:
                zero += 1
            elif i == 2:
                two -= 1
        
        for i in range(n):
            if i <= zero:
                arr[i] = 0
            elif i >= two:
                arr[i] = 2
            else:
                arr[i] = 1