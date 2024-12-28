from collections import defaultdict

class Solution:
    def findTriplets(self, arr):
        ans = []
        n = len(arr)
        for i in range(n - 2):
            target = -1 * arr[i]
            seen = defaultdict(list)
            for j in range(i + 1, n):
                curr = arr[j]
                if curr in seen:
                    for x in seen[curr]:
                        ans.append([i, x, j])
                seen[target - curr].append(j)
        return ans