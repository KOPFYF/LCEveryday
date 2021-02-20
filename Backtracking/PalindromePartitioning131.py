class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # DP bottom up
        dp = [[] for _ in range(len(s) + 1)]
        dp[-1] = [[]]
        for i in range(len(s) - 1, -1, -1):
            for j in range(i + 1, len(s) + 1):
                if s[i:j] == s[i:j][::-1]:
                    for each in dp[j]:
                        dp[i].append([s[i:j]] + each)
        # print(dp)
        return dp[0]
    
    
        # backtracking O(n*(2^n)) -> dp, top down O(n^3+2^n)
        res = []
        @lru_cache(None)
        def dfs(s, path):
            if not s:
                res.append(path)
                return
            for i in range(1, len(s) + 1):
                cur = s[:i]
                if cur == cur[::-1]:
                    dfs(s[i:], tuple(path) + tuple([cur]))
        dfs(s, tuple([]))
        return res
    
        
        
        # backtracking O(2^n)
        res = []
        def dfs(s, path):
            if not s:
                res.append(path)
                return
            for i in range(1, len(s) + 1):
                cur = s[:i]
                if cur == cur[::-1]:
                    dfs(s[i:], path + [cur])
        dfs(s, [])
        return res
    
    
        # top down DP, O(n^2)
        def dfs(path, start):
            # print(path)
            if start >= len(s):
                res.append(path[:])
            for end in range(start, len(s)):
                if s[start] == s[end] and (end-start <= 2 or dp[start+1][end-1]):
                    dp[start][end] = True
                    path.append(s[start:end+1])
                    dfs(path, end+1)
                    path.pop()
        
        res = []
        dp = [[False] * len(s) for _ in range(len(s))] # memo
        dfs([], 0)
        return res
    
        