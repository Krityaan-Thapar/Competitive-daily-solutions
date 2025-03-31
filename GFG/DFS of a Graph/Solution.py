class Solution:
    def dfs(self, adj):
        if not adj:
            return []
        
        visited = set()
        ans = []
        def solver(curr):
            if curr in visited:
                return
            
            ans.append(curr)
            visited.add(curr)
            for i in adj[curr]:
                solver(i)
        solver(0)
        return ans