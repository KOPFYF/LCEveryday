class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        max_ = 0
        for i in range(n):
            if i <= max_:
                max_ = max(max_, i + nums[i])
        return max_ >= n - 1
    
    
        n = len(nums)
        max_ = 0
        for i in range(n):
            if max_ < i:
                return False
            max_ = max(max_, i + nums[i])
        return True