from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        
        def dfs(curr, level):
            if curr is None:
                return
            
            if level > len(ans):
                ans.append(curr.val)
            
            ans[level - 1] = max(ans[level - 1], curr.val)
            dfs(curr.left, level + 1)
            dfs(curr.right, level + 1)
        dfs(root, 1)
        return ans