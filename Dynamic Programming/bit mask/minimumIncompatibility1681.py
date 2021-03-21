'''
bit mask O(n*n 2^n)
'''
class Solution:
    def minimumIncompatibility(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if k == n: return 0
        dp = [[float("inf")] * n for _ in range(1<<n)] 
        nums.sort()
        for i in range(n): dp[1<<i][i] = 0

        for mask in range(1<<n):
            n_z_bits = [j for j in range(n) if mask&(1<<j)]
            if len(n_z_bits)%(n//k) == 1:
                for j, l in permutations(n_z_bits, 2):
                    dp[mask][l] = min(dp[mask][l], dp[mask^(1<<l)][j])
            else:
                for j, l in combinations(n_z_bits, 2):
                    if nums[j] != nums[l]:
                        dp[mask][j] = min(dp[mask][j], dp[mask^(1<<j)][l] + nums[l] - nums[j])
                        
        return min(dp[-1]) if min(dp[-1]) != float("inf") else -1
        
        
        # TLE for top down
        n = len(nums)
        size = n // k
        
        @lru_cache(None)
        def dfs(mask):
            # 1111 -> 0000
            if mask == 0: return 0
            
            res = float('inf')
            cand = [i for i in range(n) if (1 << i) & mask] # unvisited ones
            combs = combinations(cand, size)
            for comb in combs:
                comb_nums = [nums[idx] for idx in comb]
                if len(set(comb_nums)) != size:
                    continue
                nxt_mask = mask
                for i in comb:
                    nxt_mask ^= 1 << i
                incomp = max(comb_nums) - min(comb_nums)
                res = min(res, incomp + dfs(nxt_mask))
            return res
        
        return dfs((1<<n) - 1) if dfs((1<<n) - 1) != float('inf') else -1
        
        
        
        
        d = len(nums) // k # the length of each partition
        
        @lru_cache(None)
        def dfs(nums):
            if not nums:
                return 0
            ret = float('inf')
            for a in combinations(nums, d): # choose a as a partition
                if len(set(a)) < d: # no two equal elements in the same subset
                    continue
                left = list(nums) # numbers left after removing partition a
                for v in a:
                    left.remove(v)
                ret = min(ret, max(a) - min(a) + dfs(tuple(left)))
            return ret
        
        ans = dfs(tuple(nums)) # turn the input into a tuple so the function can be cached
        return ans if ans != float('inf') else -1