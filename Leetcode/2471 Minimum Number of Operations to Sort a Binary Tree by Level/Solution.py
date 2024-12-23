from typing import Optional
from collections import defaultdict, deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        ans = 0

        while q:
            next_level = deque([])
            level_vals = []
            q_len = len(q)
            
            for _ in range(q_len):
                curr = q.popleft()
                level_vals.append(curr.val)

                if curr.left is not None:
                    next_level.append(curr.left)
                
                if curr.right is not None:
                    next_level.append(curr.right)
            
            tmp = [i for i in level_vals]
            level_vals.sort()

            m = defaultdict(int)
            for idx, i in enumerate(tmp):
                m[i] = idx

            for i in range(q_len):
                if tmp[i] != level_vals[i]:
                    ans += 1
                    pos = m[level_vals[i]]
                    m[tmp[i]] = pos
                    tmp[pos] = tmp[i]
            q = next_level
        return ans