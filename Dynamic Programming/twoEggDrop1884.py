class Solution:
    def twoEggDrop(self, n: int) -> int:
        @lru_cache(None)
        def dfs(n, eggs):
            if eggs == 1 or n <= 1: # try floors one by one
                return n
            res = float('inf')
            
            for f in range(1, n + 1): # recursion, max(fail, not fail)
                # If the egg breaks, the problem is reduced to x-1 eggs and i - 1 floors
                # If the eggs does not break, the problem is reduced to x eggs and n - i floors
                res = min(res, 1 + max(dfs(f - 1, eggs - 1), dfs(n - f, eggs)))
            return res
        
        return dfs(n, 2)


class Solution2:
    def twoEggDrop(self, n: int) -> int:
        # math
        # Sum of all increments <= n
        # or, x + (x - 1) + (x - 2)...1 <= n
        # or, x * (x + 1)/2 <= n
        # or, x^2 + x - 2n <= 0
        a = 1
        b = 1
        c = - 2 * n
    
        x = (-b + (b * b - 4 * a * c)**0.5) / 2.0
        
        if x - int(x) == 0:
            return int(x)
        return int(x) + 1