from typing import List

class UnionFind:
    def __init__(self):
        self.id = {}
        self.rank = {}
    
    def find(self, x):
        y = self.id.get(x, x)
        if y != x:
            self.id[x] = y = self.find(y)
        return y
    
    def union(self, x, y):
        if self.find(x) not in self.rank:
            self.rank[self.find(x)] = 0
        
        if self.find(y) not in self.rank:
            self.rank[self.find(y)] = 0
        
        if self.rank[self.find(x)] < self.rank[self.find(y)]:
            self.id[self.find(x)] = self.find(y)
        else:
            self.id[self.find(y)] = self.find(x)
            if self.rank[self.find(x)] == self.rank[self.find(y)]:
                self.rank[self.find(x)] = self.rank[self.find(x)] + 1

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        dsu = UnionFind()
        ans = None

        for s, e in edges:
            if dsu.find(e) == dsu.find(s):
                ans = [s, e]
            else:
                dsu.union(s, e)
        return ans