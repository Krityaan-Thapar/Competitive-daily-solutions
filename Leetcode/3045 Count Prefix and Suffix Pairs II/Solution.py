from typing import List
from collections import defaultdict

class Trie:
    def __init__(self):
        self.root = {}
    def insert(self, w, reverse=False):
        cur = self.root
        indices = set()
        for c in w:
            if c in cur:
                cur = cur[c]
            else:
                cur[c] = {}
                cur = cur[c]
            if 'end' in cur:
                indices.add(cur['end'])
        cur['end'] = w[::-1] if reverse else w
        return indices

class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        pref = Trie()
        suf = Trie()
        ct = defaultdict(int)
        res = 0
        for w in words:
            indices1 = pref.insert(w)
            rw = w[::-1]
            indices2 = suf.insert(rw, True)
            
            for j in indices1:
                if j in indices2:
                    res += ct[j]
            ct[w] += 1
        return res

class Solution2:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        ans = 0
        freq = defaultdict(int)
        for i in words:
            for j in freq:
                if len(j) >= len(i):
                    continue
                if i.startswith(j) and i.endswith(j):
                    ans += freq[j]
            ans += freq[i]
            freq[i] += 1 
        return ans