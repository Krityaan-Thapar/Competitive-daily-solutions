# Using DSU
from collections import defaultdict

class DSU:
    def __init__(self):    
        self.parents = defaultdict(int)
    
    def find(self, x):
        y = self.parents.get(x, x)
        if y != x:
            self.parents[x] = y = self.find(y)
        return y
    
    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        self.parents[x_root] = y_root

class Solution:
    def isCycle(self, V, edges):
        bleh = DSU()
        
        for src, dst in edges:
            if src not in bleh.parents:
                bleh.find(src)
            
            if dst not in bleh.parents:
                bleh.find(dst)
            
            src_root, dst_root = bleh.find(src), bleh.find(dst)
            if src_root == dst_root:
                return True
            
            bleh.union(src, dst)
        return False