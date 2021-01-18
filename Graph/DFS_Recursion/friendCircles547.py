class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        n = len(M)
        if not n: 
            return 0
        count = 0
        def dfs(M, cur, n): # grid, i, all other friends
            for i in range(n):
                if M[cur][i]:
                    M[cur][i] = M[i][cur] = 0 # reset to 0
                    dfs(M, i, n)
        for i in range(n):
            if M[i][i]:
                dfs(M, i, n)
                count += 1       
        return count