class Solution:
    def maxPartitions(self , s):
        ans = 0
        lasts = [-1 for _ in range(26)]
        for idx, i in enumerate(s):
            lasts[ord(i) - ord('a')] = idx
        
        part_end = 0
        for idx, i in enumerate(s):
            if idx > part_end:
                ans += 1
            
            part_end = max(part_end, lasts[ord(i) - ord('a')])
        return ans + 1