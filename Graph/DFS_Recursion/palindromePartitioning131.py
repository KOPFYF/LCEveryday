class Solution:
    def partition(self, s: str) -> List[List[str]]:
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
    
        # backtracking O(2^n)
        res = []
        def dfs(s, path, res):
            if not s:
                res.append(path)
                return
            for i in range(1, len(s) + 1):
                cur = s[:i]
                if cur == cur[::-1]:
                    dfs(s[i:], path + [cur], res)
        dfs(s, [], res)
        return res