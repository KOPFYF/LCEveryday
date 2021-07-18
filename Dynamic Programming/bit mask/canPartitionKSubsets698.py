'''
bitmask O(n 2^n)
backtracking O(4^n)
dp[mask | (1<<i)] = (dp[mask] + nums[i]) % tar

'''

class Solution_bitmask_top_down:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        s, n = sum(nums), len(nums)
        if s < k or n < k or s % k != 0 :
            return False
        nums.sort(reverse=True)
        
        @lru_cache(None)
        def dfs(mask, target):
            # convert 1111 to 0000
            # print(bin(mask)[2:], target)
            if mask == 0:
                return target == 0 # to the end, judge target sum == 0
            if target == 0:
                return dfs(mask, s // k) # reset target for others
                # while target is 0 and mask is not 0, we found an equal subset. 
                # But we need to keep doing this to find k equal subset.
            res = False
            for i in range(n):
                if mask & (1 << i):
                    if nums[i] > target: 
                        continue
                    if dfs(mask ^ (1 << i), target - nums[i]):
                        res = True
                        break
            return res

        @lru_cache(None)
        def dfs1(mask, target):
            if target < 0:
                return False
            if mask == 0:
                return target == 0
            if target == 0:
                return dfs1(mask, s // k) # reset
            
            for i in range(n):
                if mask & (1 << i): # i is not taken
                    if dfs1(mask ^ (1 << i), target - nums[i]):
                        return True
            return False
        
        return dfs((1 << n) - 1, s // k)


class Solution_bitmask_bottom_up:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        # dp[mask|(1<<i)] = (dp[mask]+nums[i]) % target
        s, n = sum(nums), len(nums)
        if s < k or n < k or s % k != 0 :
            return False
        nums.sort(reverse=True)
        target = s // k
        
        full_mask = (1 << n) - 1
        dp = [0] + [-1] * full_mask
        for mask in range(1 << n):
            if dp[mask] == -1: 
                continue
            for i in range(n):
                if not mask & (1<<i) and dp[mask] + nums[i] <= target:
                    dp[mask ^ (1<<i)] = (dp[mask] + nums[i]) % target 
        return dp[(1<<n) - 1] == 0 


class Solution_bitmask_short:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        target = sum(nums) // k
        
        @lru_cache(None)
        def dp(total,mask):
            if mask == 0: return total == 0
            return any(mask&(1<<i) and dp(total-nums[i],mask ^ (1<<i)) 
                            for i in range(len(nums)) 
                                if (total-1)%target >= nums[i]-1)
        
        return dp(sum(nums),(1<<len(nums))-1)


class Solution_bt(object):
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        s, n = sum(nums), len(nums)
        if s < k or n < k or s % k != 0 :
            return False
        nums.sort(reverse=True)
        target = [s / k] * k
        
        def dfs(target, pos):
            if pos == n:
                return True
            # seen = set() # pruning
            for i in range(k):
                if target[i] >= nums[pos]:
                # if target[i] >= nums[pos] and target[i] not in seen:
                    target[i] -= nums[pos]
                    if dfs(target, pos + 1):
                        return True
                    target[i] += nums[pos]
                    # seen.add(target[i]) # pruning
                    
                    # If a single number couldn't fit into one bucket, it is a waste of time to put it into the other bucket.
                    if target[i] == s / k: break # another game changer pruning
            return False
        
        return dfs(target, 0)
        