class Solution:
    def findPages(self, arr, k):
        num_books = len(arr)
        if num_books < k:
            return -1
        
        if num_books == k:
            return max(arr)
        
        def check(bound):
            count = 1
            local = 0
            for i in arr:
                if local + i > bound:
                    local = i
                    count += 1
                else:
                    local += i
            
            return count <= k
            
        ans = 0
        lo, hi = max(arr), sum(arr)
        while lo <= hi:    
            mid = lo + (hi - lo) // 2
            if check(mid):
                ans = mid
                hi = mid - 1
            else:
                lo = mid + 1
        return ans