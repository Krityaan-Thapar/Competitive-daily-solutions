from typing import List
import heapq

class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        l = 0
        ans = 0
        win_len = 0
        win_max = 0
        win_min = int(1e10)

        for r in range(len(nums)):
            win_max = max(win_max, nums[r])
            win_min = min(win_min, nums[r])

            if win_max - win_min > 2:
                win_len = r - l
                ans += (win_len * (win_len + 1)) // 2

                l = r
                win_min = win_max = nums[r]

                while l > 0 and abs(nums[r] - nums[l - 1]) <= 2:
                    l -= 1
                    win_min = min(win_min, nums[l])
                    win_max = max(win_max, nums[l])
                
                if l < r:
                    win_len = r - l
                    ans -= (win_len * (win_len + 1)) // 2
        
        win_len = r - l + 1
        ans += (win_len * (win_len + 1)) // 2
        return ans

class Solution2:
    def continuousSubarrays(self, nums: List[int]) -> int:
        max_heap = []
        min_heap = []
        l = 0
        ans = 0

        for r in range(len(nums)):
            heapq.heappush(min_heap, (nums[r], r))
            heapq.heappush(max_heap, (-nums[r], r))

            while l < r and -max_heap[0][0] - min_heap[0][0] > 2:
                l += 1

                while min_heap and min_heap[0][1] < l:
                    heapq.heappop(min_heap)
                while max_heap and max_heap[0][1] < l:
                    heapq.heappop(max_heap)
            ans += r - l + 1
        return ans 