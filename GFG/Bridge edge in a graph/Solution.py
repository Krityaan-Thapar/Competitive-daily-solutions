class DSU:
    def __init__(self, size):
        self.parents = [i for i in range(size)]
    
    def find(self, x):
        y = self.parents[x]
        if y != x:
            y = self.parents[x] = self.find(y)
        return y
    
    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        self.parents[x_root] = y_root

class Solution:
    def isBridge(self, V, edges, c, d):
        dsu = DSU(V)
        for src, dst in edges:
            if src in (c, d) and dst in (c, d):
                continue
            dsu.union(src, dst)
        return dsu.find(c) != dsu.find(d)