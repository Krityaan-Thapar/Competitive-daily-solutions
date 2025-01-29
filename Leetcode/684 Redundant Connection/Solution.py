from typing import List

class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        stk = []
        ans = [0 for _ in range(n)]
        prev = 0

        for i in logs:
            pid, op, time = i.split(":")
            pid = int(pid)
            time = int(time)
            
            if op == "end":
                ans[stk.pop()] += time - prev + 1
                prev = time + 1
            else:
                if stk:
                    ans[stk[-1]] += time - prev
                stk.append(pid)
                prev = time
        return ans