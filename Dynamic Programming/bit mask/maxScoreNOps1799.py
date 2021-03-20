class Solution:
    def maxScore(self, nums: List[int]) -> int:
        # dp bit mask, O(2^m * m^2)
        m = len(nums)
        n = m // 2
        gcd_map = {}
        for i in range(m):
            for j in range(m):
                if i == j: continue
                gcd_map[(i, j)] = math.gcd(nums[i], nums[j])
        gcds = gcd_map
        
        full_mask = (1 << m) - 1
        
        @lru_cache(None)
        def dfs(mask):
            # convert 1111 1111 to 0000 0000, 1 is available
            if mask == 0:
                return 0
            res = 0
            cands = [i for i in range(m) if mask & (1 << i)]
            for x, y in combinations(cands, 2):
                nxt_mask = mask ^ (1 << x) ^ (1 << y)
                ones = len(cands)
                res = max(res, dfs(nxt_mask) + gcd_map[(x, y)] * (m + 2 - ones) // 2)
            return res
        
        return dfs(full_mask)


class Solution1:
    def maxScore(self, nums: List[int]) -> int:
        @lru_cache(None)
        def dp(op, mask):
            # convert 0000 0000 to 1111 1111
            if op == n + 1:  # Reach to n operations
                return 0

            ans = 0
            for i in range(2 * n):
                if mask & (1 << i): 
                    continue # i-th bit already visited
                for j in range(i + 1, 2 * n):
                    if mask & (1 << j): 
                        continue
                    newMask = mask ^ (1 << i) ^ (1 << j)  # Mark as used i and j elements
                    ans = max(ans, dp(op + 1, newMask) + op * gcd(nums[i], nums[j]))
            return ans

        n = len(nums) // 2
        return dp(1, 0)


class Solution2:
    def maxScore(self, nums: List[int]) -> int:
        @cache
        def fn(nums, k): 
            """Return max score from nums at kth step."""
            if not nums: return 0 # boundary condition 
            ans = 0 
            for i in range(len(nums)):
                for j in range(i+1, len(nums)): 
                    rest = nums[:i] + nums[i+1:j] + nums[j+1:]
                    ans = max(ans, k*gcd(nums[i], nums[j]) + fn(tuple(rest), k+1))
            return ans
        
        return fn(tuple(nums), 1)