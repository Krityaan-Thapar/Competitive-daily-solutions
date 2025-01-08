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

class Solution3:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        def create_Zarr(string, z):
            n = len(string)
            left, right, k = 0, 0, 0
            for i in range(1, n):
                if i > right:
                    left, right = i, i
                    while right < n and string[right - left] == string[right]:
                        right += 1
                    z[i] = right - left
                    right -= 1
                else:
                    k = i - left
                    if z[k] < right - i + 1:
                        z[i] = z[k]
                    else:
                        left = i
                        while right < n and string[right - left] == string[right]:
                            right += 1
                        z[i] = right - left
                        right -= 1
        
        answer = 0
        
        for i in range(len(words) - 1):
            for j in range(i + 1, len(words), 1):
                if len(words[i]) > len(words[j]):
                    continue
                concat = words[i] + "$" + words[j]
                left = len(concat)
                z = [0] * left
                create_Zarr(concat, z)
                
                if z[len(words[i]) + 1] == len(words[i]) and z[left - len(words[i])] == len(words[i]):
                    answer += 1
        return answer