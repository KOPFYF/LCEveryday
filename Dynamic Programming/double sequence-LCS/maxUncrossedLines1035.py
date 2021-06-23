class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        m, n = len(A), len(B)
        
        @lru_cache(None)
        def dfs(i, j):
            if i == 0 or j == 0: return 0
            
            if A[i - 1] == B[j - 1]:
                return dfs(i - 1, j - 1) + 1
            else:
                return max(dfs(i - 1, j), dfs(i, j - 1))
        
        return dfs(m, n)