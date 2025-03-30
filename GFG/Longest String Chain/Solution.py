class Solution:
    def longestStringChain(self, words):
        alpha = "abcdefghijklmnopqrstuvwxyz"
        bleh = {}
        for i in words:
            if len(i) not in bleh:
                bleh[len(i)] = set()
            bleh[len(i)].add(i)
        
        cache = {}
        def solver(word):
            x = len(word)
            if x + 1 not in bleh:
                return 1
            
            if word in cache:
                return cache[word]
            
            ans = 1
            for i in range(x + 1):
                pref = word[:i]
                suff = word[i:]
                for split in alpha:
                    cand = pref + split + suff
                    if cand in bleh[x + 1]:
                        ans = max(ans, solver(cand) + 1)
            
            cache[word] = ans
            return ans
        
        result = 0
        for i in bleh:
            for w in bleh[i]:
                result = max(result, solver(w))
        return result