class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        if set(target).difference(set(source)):
            return -1
        
        S, T = len(source), len(target)
        s_ptr, t_ptr = 0, 0
        ans = 1
        while t_ptr < T:
            while s_ptr < S:
                if source[s_ptr] == target[t_ptr]:
                    break
                s_ptr += 1
            
            if s_ptr == S:
                s_ptr = 0
                ans += 1
                continue
            s_ptr += 1
            t_ptr += 1
        return ans