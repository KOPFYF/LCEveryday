class Solution:
    def canDistribute(self, nums: List[int], quantity: List[int]) -> bool:  
        # DP O(50*3^m)
        # Iterating through all masks with their submasks. Complexity O(3n)
        # https://cp-algorithms.com/algebra/all-submasks.html
        d = Counter(nums)
        cnt = sorted(d.values())  
        n, m = len(cnt), len(quantity)  
        sums = defaultdict(int)
        
        # get sum for a subset of consumers
        for mask in range(1, 1 << m):
            for i in range(m):
                if (1 << i) & mask:
                    sums[mask] += quantity[i]   
            # print(mask, sums[mask], bin(sums[mask])[2:])
            
        dp = [[0] * (n + 1) for _ in range(1 << m)]
        dp[0][0] = 1
        for mask in range(1 << m):
            for i in range(n):
                dp[mask][i + 1] |= dp[mask][i]
                cur = mask
                while cur:
                    if (sums[cur] <= cnt[i] and dp[mask ^ cur][i]):
                        dp[mask][i + 1] = 1
                    cur = (cur - 1) & mask
        return dp[-1][n]

class Solution2:
    def canDistribute(self, nums: List[int], quantity: List[int]) -> bool:  
        # DP O(50*3^m)
        # Iterating through all masks with their submasks. Complexity O(3n)
        # https://cp-algorithms.com/algebra/all-submasks.html
        d = Counter(nums)
        cnt = sorted(d.values())  
        n, m = len(cnt), len(quantity)  
        sums = defaultdict(int)
        
        # get sum for a subset of consumers
        for mask in range(1, 1 << m):
            for i in range(m):
                if (1 << i) & mask:
                    sums[mask] += quantity[i]   
            # print(mask, sums[mask], bin(sums[mask])[2:])
        
        # dp[mask][i]: if we can satisfy customers mask using first i numbers
        @lru_cache(None)
        def dfs(i, mask):      
            if not mask: return True  
            if i == n: return False  
            
            submask = mask      
            while submask:          
                if sums[submask] <= cnt[i] and dfs(i + 1, mask ^ submask):
                    return True           
                submask = (submask-1) & mask
            return dfs(i + 1, mask)
                
        return dfs(0, (1 << m) - 1)


class Solution1(object):
    def canDistribute(self, nums, quantity):
        """
        :type nums: List[int]
        :type quantity: List[int]
        :rtype: bool
        """
        c = Counter(nums)
        m = len(quantity)
		# we only need at most m different numbers, so we choose the ones which are most abundant
        left = sorted(c.values())[-m:]
        # print(c.values(), left)  
		# If the customer with most quantity required can't be fulfilled, we don't need to go further and answer will be false
        quantity.sort(reverse=True)
        
        def dfs(left, quantity, pos):
            if pos == len(quantity):
                return True
            
            for i in range(len(left)):
                # loop each requirement
                if left[i] >= quantity[pos]:
                    left[i] -= quantity[pos]
                    if dfs(left, quantity, pos + 1):
                        return True
                    left[i] += quantity[pos]
            return False
        
        return dfs(left, quantity, 0)