class Solution:
    def aggressiveCows(self, stalls, k):
        stalls.sort()
        lo = 0
        hi = stalls[-1]
        
        def check(target):
        
            prev = None
            for i in stalls:
                if prev is None:
                    prev = i
                    continue
                
                if i - prev >= target:
                    prev = i
                    num += 1
                
                if num >= k:
                    return True
            return num >= k
        
        ans = -1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if check(mid):
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1
        return ans