from functools import cache, lru_cache
from itertools import product

class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        # no two adjacent cells having the same color
        # 1 <= m <= 5
        # 1 <= n <= 1000
        mod = 10**9 + 7
        
        def check(pos):
            return all(a != b for a, b in zip(pos, pos[1:]))
        
        def neighs(pos1, pos2):
            return all(a != b for a, b in zip(pos1, pos2))
        
        states = {''.join(pos) for pos in product('RGB', repeat=m) if check(pos)} # all possible cols
        adj = {}
        for state in states:
            adj[state] = [next_state for next_state in states if neighs(next_state, state)]
            
        @cache
        def dfs(state, n):
            if n == 0:
                return 1
            res = 0
            for next_state in adj[state]:
                res =  (res + dfs(next_state,  n - 1)) % mod
            return res
        
        return sum(dfs(state, n - 1) for state in states) % mod


'''
Since M <= 5, we can fill colors of matrix column by column. To store previous column state in DP, we can use BitMask, each 2 bits store a color (1=Red, 2=Green, 3=Blue, 0=White), so there is total 4^M column states.

'''
class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        # no two adjacent cells having the same color
        # 1 <= m <= 5
        # 1 <= n <= 1000
        def getColor(mask, pos):  # Get color of the `mask` at `pos`, use 2 bits to store a color
            return (mask >> (2 * pos)) & 3
        
        def setColor(mask, pos, color):  # Set `color` to the `mask` at `pos`, use 2 bits to store a color
            return mask | (color << (2 * pos))

        def dfs(r, curColMask, prevColMask, out):
            if r == m:  # Filled full color for this column
                out.append(curColMask)
                return
            for i in [1, 2, 3]:  # Try colors i in [1=RED, 2=GREEN, 3=BLUE]
                if getColor(prevColMask, r) != i and (r == 0 or getColor(curColMask, r - 1) != i):
                    dfs(r + 1, setColor(curColMask, r, i), prevColMask, out)

        @lru_cache(None)
        def neighbor(prevColMask):  # Generate all possible columns we can draw, if the previous col is `prevColMask`
            out = []
            dfs(0, 0, prevColMask, out)
            return out

        @lru_cache(None)
        def dp(c, prevColMask):
            if c == n: return 1  # Found a valid way
            ans = 0
            for nei in neighbor(prevColMask):
                ans = (ans + dp(c + 1, nei)) % 1_000_000_007
            return ans

        return dp(0, 0)