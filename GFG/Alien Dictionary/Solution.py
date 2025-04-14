class Solution:
    def findOrder(words):
        letters = set()
        for word in words:
            for ch in word:
                letters.add(ch)
        
        V = len(letters)
        adj, ind = {}, {}
        for i in letters:
            adj[i] = []
            ind[i] = 0
        
        def mapper(str1, str2):
            l1, l2 = len(str1), len(str2)
            ptr1, ptr2 = 0, 0
            
            while ptr1 < l1 and ptr2 < l2 and str1[ptr1] == str2[ptr2]:
                ptr1 += 1
                ptr2 += 1
            
            if ptr1 == l1:
                return
            
            if ptr2 == l2:
                return "longer string before shorter string" # what a troll edge case
            
            adj[str1[ptr1]].append(str2[ptr2])
            ind[str2[ptr2]] += 1
            # print(str1, str2, ":", str1[ptr1], "->", str2[ptr2])
        
        N = len(words)
        for i in range(N - 1):
            ret = mapper(words[i], words[i + 1])
            if ret is not None:
                return ""
        
        from collections import deque
        q = deque()
        for i in ind:
            if ind[i] == 0:
                q.append(i)
        
        ans = []
        while q:
            curr = q.popleft()
            ans.append(curr)
            for nei in adj[curr]:
                ind[nei] -= 1
                if ind[nei] == 0:
                    q.append(nei)
        
        if len(ans) != V:
            return ""
        return "".join(ans)