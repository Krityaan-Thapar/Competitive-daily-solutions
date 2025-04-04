from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        store = []
        path = []
        def backtrack_check_paths(node):
            nonlocal store
            if node is None:
                return
            
            path.append(node)
            if node.left is None and node.right is None:
                d = len(path)
                if store and len(store[0]) < d:
                    store = []
                
                if not store or len(store[0]) == d:
                    store.append(path[:])
                path.pop()
                return

            backtrack_check_paths(node.left)
            backtrack_check_paths(node.right)
            path.pop()
        
        backtrack_check_paths(root)
        p, d = len(store), len(store[0]) - 1
        if p == 1:
            return store[0][d]
        while any(store[i][d].val != store[0][d].val for i in range(p)):
            d -= 1
        return store[0][d]