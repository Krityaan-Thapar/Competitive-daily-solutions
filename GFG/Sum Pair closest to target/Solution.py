class Solution:
    def sumClosest(self, arr, target):
        n = len(arr)
        arr.sort()
        res = []
        minDiff = float('inf')
    
        left = 0
        right = n - 1
    
        while left < right:
            currSum = arr[left] + arr[right]
            
            if abs(target - currSum) < minDiff:
                minDiff = abs(target - currSum)
                res = [arr[left], arr[right]]
            
            if currSum < target:
                left += 1
            elif currSum > target:
                right -= 1
            else:
                return res
        return res
