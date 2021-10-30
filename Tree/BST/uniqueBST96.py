class Solution:
    def numTrees(self, n: int) -> int:
        '''
        G(n): the number of unique BST for a sequence of length n.
        F(i,n): the number of unique BST, where the number i is served as the root of BST (1 <= i <= n).

        G(n): # of unique BST for a seq of n
        F(n, i): # of unique BST for a seq of n using i as root
        G(n) = F(n, 1) + F(n, 2) + ... + F(n, n)
        F(n, i) = G(i - 1) * G(n - i)
        
        => G(n) = G(1 - 1) * G(n - 1) + G(2 - 1) * G(n - 2) + ... + G(n - 1) * G(0)
        '''
        G = [0] * (n + 1)
        G[0] = G[1] = 1
        for i in range(2, n + 1):
            for j in range(1, i + 1):
                G[i] += G[j - 1] * G[i - j]
        return G[n]