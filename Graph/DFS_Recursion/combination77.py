class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # soln 0
        res = []
        def dfs(pos, k, path):
            if k == 0:
                res.append(path)
            for i in range(pos, n + 1):
                # take i, where pos <= i <= n
                dfs(i + 1, k - 1, path + [i]) # pass path by creating another copy, memory usage here
        dfs(1, k, [])
        return res
    
        # soln 1
        res = []
        def dfs(pos, path):
            if len(path) == k:
                res.append(path[:]) # append a copy, use with path.append()/path.pop()
            for i in range(pos, n + 1):
                path.append(i)
                dfs(i + 1, path) # path address wont change
                path.pop()
        dfs(1, [])
        return res
        
        # soln 2, take/no-take
        res = []
        def dfs(pos, k, path):
            if k == 0:
                res.append(path)
                return
            if pos == n: return # pos == n but k still not 0
            dfs(pos + 1, k - 1, path + [pos + 1]) # take current pos
            dfs(pos + 1, k, path) # no take
        
        dfs(0, k, [])
        return res