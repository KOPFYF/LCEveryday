class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        n = len(s)
        
        def dfs(s, path):
            if not s: 
                return 0
            res = 0
            for i in range(1, len(s) + 1):
                cand = s[:i]
                if cand not in path: # and len(s) - i + 1 > res: # pruning
                    path.add(cand)
                    res = max(res, 1 + dfs(s[i:], path))
                    path.remove(cand)
            return res
        
        return dfs(s, set())    


class Solution1:
    def maxUniqueSplit(self, s: str) -> int:        
        def dfs1(pos, path):
            # return maximum number of unique substrings for s[:pos]
            # call dfs(i, new_path) with candidate s[i:pos]
            if pos == 0:
                return 0
            
            res = 0
            for i in range(0, pos):
                cand = s[i:pos]
                if cand in path:
                    continue
                path.add(cand)
                res = max(res, 1 + dfs1(i, path))
                path.remove(cand)
            return res
        
        return dfs1(n, set())