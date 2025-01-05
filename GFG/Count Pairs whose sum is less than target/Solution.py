class Solution:
    def countPairs(self, arr, target):
        arr.sort()
        n = len(arr)
        one, two = 0, n - 1
        ans = 0
        
        while one < two:
            if arr[one] + arr[two] >= target:
                two -= 1
            else:
                ans += (two - one)
                one += 1
        return ans