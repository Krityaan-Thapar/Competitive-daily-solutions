from typing import List

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
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = DSU(n)
        for src, dst in edges:
            dsu.union(src, dst)
        parents = set()
        for i in range(n):
            parents.add(dsu.find(i))
        return len(parents)