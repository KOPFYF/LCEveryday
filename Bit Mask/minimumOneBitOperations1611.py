class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        if n <= 1:
            return n
        bit = 0
        while (1 << bit) <= n:
            bit += 1
        return (1 << bit) - 1 - self.minimumOneBitOperations(n - (1 << (bit - 1)))
        
        
        
        # Gray code
        # bto0(k) = 2 * bto0(k-1) + 1， bto0(0) = 1 => bto0(k) = 2^(k+1)-1
        @lru_cache(None)
        def bto0(b): 
            # change 2^b to 0
            return (1 << (b + 1)) - 1
        
        @lru_cache(None)
        def dfs(n):
            # change integer n into 0
            # 1XXX XXXX -> 1100 0000 -> 1000 0000 -> 0
            # consider this integer n is just in the middle of the first step of changing 2^b1 into 0.
            if n == 0: return 0
            leftmost = int(log2(n))
            return bto0(leftmost) - dfs(n - (1 << leftmost))
        
        return dfs(n)