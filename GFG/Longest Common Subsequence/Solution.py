class Solution:
    def lcs(self, s1, s2):
        l1, l2 = len(s1), len(s2)
        dp = [0 for _ in range(l2 + 1)]
        for i in range(1, l1 + 1):
            nex = [0 for _ in range(l2 + 1)]
            for j in range(1, l2 + 1):
                if s1[i - 1] == s2[j - 1]:
                    nex[j] = dp[j - 1] + 1
                else:
                    nex[j] = max(dp[j], nex[j - 1])
            dp = nex
        return dp[-1]