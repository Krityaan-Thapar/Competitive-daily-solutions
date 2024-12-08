class Solution:
    def mergeOverlap(self, arr):
        arr.sort(key = lambda x: x[0])
        ans = []
        ans.append(arr[0])
        
        for i in range(1, len(arr)):
            prev_start, prev_end = ans[-1]
            curr_start, curr_end = arr[i]
            
            if curr_start <= prev_end:
                ans.pop()
                ans.append([prev_start, max(curr_end, prev_end)])
            else:
                ans.append(arr[i])
        return ans