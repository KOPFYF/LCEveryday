'''
Backtracking is O(n!)
dp O(n*2^n) 

Start From Position 1 - N
Check which values are not yet assigned( By the field Bitmask) , ```if(getBit(mask,i)==0)
Check if this position is beautiful. ```if((i+1)%(pos+1)==0 ||(pos+1)%(i+1)==0)
If Yes, call next position with updated mask.
'''

class Solution:
    def countArrangement(self, N: int) -> int:
        # dp bit mask
        n = N
        @lru_cache(None)
        def dfs(pos, mask):
            # convert 0000 to 1111
            if pos == n:
                return 1
            
            res = 0
            for i in range(n):
                if mask & (1 << i):
                    continue # skip used bit
                if (i + 1) % (pos + 1) == 0 or (pos + 1) % (i + 1) == 0:
                    res += dfs(pos + 1, mask ^ (1 << i))
            return res
        
        return dfs(0, 0)


'''
Backtracking is O(n!)
dp O(n*2^n) 
'''

class Solution:
    def countArrangement(self, N: int) -> int:
        # backtracking -> dp
        res = 0
        nums = tuple(range(1, N+1))
        
        @lru_cache(None)
        def dfs(nums, i):
            if i == N+1: # to the end
                return 1
            res = 0
            for j, num in enumerate(nums):
                if not num % i or not i % num:
                    res += dfs(tuple(nums[:j] + nums[j+1:]), i+1)
            return res
        
        return dfs(nums, 1)     
        

        # dp bitmask, 1 <= N <= 15, subset, O(n*2^n)/O(2^n)
        # mask: full -> zero, i: 1->n
        # if mask has n, 1100, say n = 4, flip it to 0 -> 0100
        @lru_cache(None)
        def dfs(mask, i):
            if i == N + 1: return 1
            if not mask: return 0 # base case, mask = 0000
            
            res = 0
            for n in range(1, N+1): # try from 1 to N for index i
                if mask & (1 << (n-1)) and (not i % n or not n % i):
                    res += dfs(mask ^ (1 << (n-1)), i+1)
            return res

        return dfs((1 << N) - 1, 1)
    

        # dp subset
        @lru_cache(None)
        def dfs(nums):
            l = len(nums)
            if l == 1: # Any integer can be divide by 1
                return 1
            res = 0
            for j in range(l):
                if nums[j] % l == 0 or l % nums[j] == 0:
                    # print(nums[j], l)
                    res += dfs(nums[:j] + nums[j+1:])
            return res
        
        return dfs(tuple(range(1, n+1)))
            