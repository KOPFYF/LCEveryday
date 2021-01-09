class Solution(object):
    def numEnclaves(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        m, n = len(A), len(A[0])
        
        def dfs(A, i, j):
            if i < 0 or j < 0 or i >= m or j >= n or A[i][j] != 1:
                return
            A[i][j] = 0
            dfs(A, i-1, j)
            dfs(A, i+1, j)
            dfs(A, i, j-1)
            dfs(A, i, j+1)
            
        for i in range(m):
            for j in range(n):
                if A[i][j] == 1 and (i == 0 or j == 0 or i == m-1 or j ==n-1):
                    dfs(A, i, j)  
        
        return sum(sum(A[i]) for i in range(m))