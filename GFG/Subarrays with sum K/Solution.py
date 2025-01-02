from collections import defaultdict
class Solution:
    def countSubarrays(self, arr, k):
        m = defaultdict(int)
        m[0] = 1
        ans, s = 0, 0
        for i in range(len(arr)):
            s += arr[i]
            ans += m[s - k]
            m[s] += 1
        return ans