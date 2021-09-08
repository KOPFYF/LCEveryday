'''
1. Consider only the numbers which have a good prime factorization.
2. Use brute force to find all possible good subsets and then calculate its frequency in nums.

1 <= nums.length <= 105
1 <= nums[i] <= 30


'''
class Solution:
    def numberOfGoodSubsets(self, nums: List[int]) -> int:
        P = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        cnt = Counter(nums)
        bm = [sum(1<<i for i, p in enumerate(P) if x % p == 0) for x in range(31)]
        bad = set([4, 8, 9, 12, 16, 18, 20, 24, 25, 27, 28])
        M = 10**9 + 7
        
        @lru_cache(None)
        def dp(mask, num):
            if num == 1: return 1
            # case 1, do not take num and continue to the smaller one
            ans = dp(mask, num - 1)
            # case 2, take num, which should not be in bad list
            if num not in bad and mask | bm[num] == mask:
                ans += dp(mask ^ bm[num], num - 1) * cnt[num]
            return ans % M

        return ((dp(1023, 30) - 1) * pow(2, cnt[1], M)) % M
    
        # has bugs!!
        mod = 10**9 + 7
        cnt = collections.Counter(nums)
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        # create bitmask corresponding to this number from 2 to 30
        masks = [sum(1<<i for i, p in enumerate(primes) if x % p == 0) for x in range(31)]
        # print([bin(mask)[2:] for mask in masks])
        bads = set([4, 8, 9, 12, 16, 18, 20, 24, 25, 27, 28])
              
        @cache
        def dfs(mask, num):
            # from 1111 to 0000
            if num == 1:
                return 1
            # case 1, do not take num and continue to the smaller one
            res = dfs(mask, num - 1)
            # case 2, take num, which should not be in bad list
            if num not in bads and mask | masks[num] == mask:
                res += dfs(mask ^ masks[num], num - 1) * cnt[num]
            return res % mod
          
        return dfs((1<<10)-1, 30) * pow(2, cnt[1], mod) % mod # num 1 fits into all good subsets
                
            
            