class Solution:
    def numTrees(self, n: int) -> int:
        # F(i, n) = G(i-1) * G(n-i)	1 <= i <= n 
        # G(n) = F(1, n) + F(2, n) + ... + F(n, n). 
        # G(n) = G(0) * G(n-1) + G(1) * G(n-2) + … + G(n-1) * G(0) 
        G = [0] * (n + 1)
        G[0] = G[1] = 1
        for i in range(2, n + 1):
            for j in range(1, i + 1):
                G[i] += G[j - 1] * G[i - j]
        return G[n]