class Solution:
    def maximumProfit(self, prices):
        ans = 0
        l = 0
        for r in range(len(prices)):
            if prices[r] < prices[l]:
                l = r
            else:
                ans = max(ans, prices[r] - prices[l])
        return ans