from typing import List
from collections import defaultdict, deque

class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        ins = defaultdict(int)
        outs = defaultdict(int)
        adj = {}
        for src, dst in pairs:
            if src in adj:
                adj[src].append(dst)
            else:
                adj[src] = deque([dst])
            ins[dst] += 1
            outs[src] += 1
        
        start = None
        for i in outs:
            if outs[i] == ins[i] + 1:
                start = i
                break
        if start is None:
            start = pairs[0][0]
        
        ans = []
        stk = [start]
        while stk:
            if stk[-1] in adj and len(adj[stk[-1]]) > 0:
                stk.append(adj[stk[-1]].popleft())
            else:
                ans.append(stk.pop())
        
        ans = ans[::-1]
        res = []
        for i in range(1, len(ans)):
            res.append([ans[i - 1], ans[i]])
        return res