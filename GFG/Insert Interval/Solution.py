class Solution:
    def insertInterval(self, intervals, newInterval):
        new_start, new_end = newInterval
        ans = []
        
        if new_end < intervals[0][0]:
            return [newInterval] + intervals
        
        if intervals[-1][1] < new_start:
            return intervals + [newInterval]
        
        for idx, i in enumerate(intervals):
            curr_start, curr_end = i
            
            if new_end < curr_start:
                ans.append([new_start, new_end])
                ans = ans + intervals[idx:]
                break
            elif curr_end < new_start:
                ans.append(i)
            else:
                new_start = min(new_start, curr_start)
                new_end = max(new_end, curr_end)
        
        if not ans or ans[-1][1] < new_start:
            ans.append([new_start, new_end])
        return ans