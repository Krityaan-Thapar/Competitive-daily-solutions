class Solution:
    def countTriangles(self, arr):
        arr.sort()
        n = len(arr)
        ans = 0
        
        for i in range(n - 1, 1, -1):
            l, h = 0, i - 1
            while h > l:
                if arr[l] + arr[h] > arr[i]:
                    ans += h - l
                    h -= 1
                else:
                    l += 1
        return ans