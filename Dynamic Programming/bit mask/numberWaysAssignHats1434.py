"""
n = 8
1010 0000 (brute force n^40)
hat assign to ppl is better, so that mask can transform

hat 1: 
1000 0000
0010 0000
"""

class Solution:
    def numberWays(self, hats: List[List[int]]) -> int: 
        # bit mask DP
        n, mod = len(hats), 10**9 + 7
        full_mask = (1 << n) - 1
        hat2ppl = defaultdict(set) # mapping hat to people
        for p, hats_i in enumerate(hats):
            for h in hats_i: 
                hat2ppl[h].add(p)     
        
        @lru_cache(None)
        def dfs(i, mask):
            # i: index of hat, mask: current bit state
            if mask == full_mask: return 1 # *
            if i == 41: return 0
            
            res = dfs(i + 1, mask) # no take, skip this hat
            for p in hat2ppl[i]: # try to assign hat_i to all people
                if mask & (1 << p):
                    continue # current people already has a hat
                res += dfs(i + 1, mask | (1 << p))
            return res % mod
               
        return dfs(0, 0) 
   
     
class Solution2:
    def numberWays(self, hats: List[List[int]]) -> int:         
        # Bottom up DP
        mod, N = 10 ** 9 + 7, 1 << len(hats)
        hat2ppl = defaultdict(set)    
        for p, hats_i in enumerate(hats):
            for h in hats_i: 
                hat2ppl[h].add(p)     
        # print(hat2ppl) # defaultdict(<class 'set'>, {3: {0}, 4: {0, 1}, 5: {1, 2}})
        
        dp = [0] * N
        dp[0] = 1
        for h in hat2ppl:
            # assign hat h to people
            for state in range(N - 1, -1, -1):
                for p in hat2ppl[h]: 
                    # loop all people applicable to that hat h
                    if state & (1 << p) == 0:  
                        # if current person can be added to the state
                        dp[state ^ (1 << p)] = (dp[state ^ (1 << p)] + dp[state]) % mod                        
        return dp[-1]