class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        dp = [0 for _ in range(n)]

        for i in range(n):
            local = 0
            for j in range(0, i):
                if nums[i] % nums[j] == 0:
                    local = max(local, dp[j])
            dp[i] = local + 1
        
        ans = []
        bleh = [-1, -1]
        for idx, i in enumerate(dp):
            if i > bleh[0]:
                bleh = [i, idx]
        
        l, start = bleh[0], nums[bleh[1]]
        for i in range(bleh[1], -1, -1):
            if l == dp[i] and start % nums[i] == 0:
                ans.append(nums[i])
                l -= 1
                start = nums[i]
        return ans[::-1]