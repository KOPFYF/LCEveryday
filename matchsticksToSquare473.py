class Solution1(object):
    def makesquare(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # time O(2^n), space O(n^2), 1528 ms
        if len(nums) < 4 : 
            return False
        s = sum(nums)
        if s % 4 != 0:
            return False
        target = [s / 4] * 4
        nums.sort(reverse=True) # without this line it would pop TLE
        
        def dfs(target, pos):
            if pos == len(nums): 
                return True
            for i in range(4):
                if target[i] >= nums[pos]:
                    target[i] -= nums[pos]
                    if dfs(target, pos + 1):
                        return True
                    else:
                        target[i] += nums[pos]
            return False
        return dfs(target, 0)


class Solution2(object):
    def makesquare(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # time O(2^n), space O(n^2), 48 ms
        if len(nums) < 4 : 
            return False
        s = sum(nums)
        if s % 4 != 0:
            return False
        target = [s / 4] * 4
        nums.sort(reverse=True) # without this line it would pop TLE
        
        def dfs(target, pos):
            if pos == len(nums): 
                return True
            seen = set() # add memo to dedup
            for i in range(4):
                if target[i] >= nums[pos] and target[i] not in seen:
                    target[i] -= nums[pos]
                    if dfs(target, pos + 1):
                        return True
                    else:
                        target[i] += nums[pos]
                        seen.add(target[i]) # pruning
            return False
        return dfs(target, 0)


class Solution3(object):
    def makesquare(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # time O(2^n), space O(n^2), 48 ms
        if len(nums) < 4 : 
            return False
        s = sum(nums)
        if s % 4 != 0:
            return False
        target = [s / 4] * 4
        nums.sort(reverse=True) # without this line it would pop TLE
        
        def dfs(target, pos):
            if pos == len(nums): 
                return True
            for i in range(4):
                if target[i] >= nums[pos]:
                    target[i] -= nums[pos]
                    if dfs(target, pos + 1):
                        return True
                    target[i] += nums[pos]
                    if target[i] == s / 4: # game changer
                        # if nums[pos] does not fit this bucket, it will not fit into the others
                        break       
            return False
        return dfs(target, 0)
                
        
