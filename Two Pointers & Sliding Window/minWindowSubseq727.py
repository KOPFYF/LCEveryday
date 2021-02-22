class Solution:
    def minWindow(self, S: str, T: str) -> str:
        # sliding window
        m, n = len(S), len(T)
        j, cnt, res = 0, 0, ""
        while j < m:
            if S[j] == T[cnt]:
                cnt += 1
                if cnt == n: # answer found!, shrink left
                    end = j + 1
                    while cnt > 0:
                        if T[cnt - 1] == S[j]: 
                            cnt -= 1
                        j -= 1
                    j += 1
                    if len(res) == 0 or end - j < len(res):
                        res = S[j:end]  
            j += 1   
        return res
        
        # DP LCS botton up, O(mn)
        m, n = len(S), len(T)
        if m == 0 or n == 0:
            return ""
        
        dp = [[float('inf')] * (m + 1) for _ in range(n + 1)]
        for j in range(1, m + 1):
            for i in range(1, n + 1):
                if S[j-1] == T[i-1]:
                    if i == 1:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + dp[i][j-1]
        
        res_len = min(dp[n])
        if res_len == float('inf'):
            return ""
        for j in range(1, m + 1):
            if dp[n][j] == res_len:
                return S[j-res_len:j]
        
        
        # DP top down, O(mn)
        @lru_cache(None)
        def dfs(i, j): 
            # LCS, 
            # T[j:] in S[i:] => find the index in S such that T[j+1:] is in S[index:]
            if j == len(T): return i
            
            idx = S.find(T[j], i + 1)
            return float('inf') if idx == -1 else dfs(idx, j + 1)
        
        l, res = float('inf'), ''
        for i, s in enumerate(S):
            if s == T[0]:
                idx = dfs(i, 1)
                if idx - i < l:
                    l, res = idx - i, S[i:idx+1]
        return res
            