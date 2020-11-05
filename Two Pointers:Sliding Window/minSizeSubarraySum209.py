class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        # Sliding Window, time O(n) space O(1)
        i, res = 0, len(nums) + 1 # if not into the loop, will return 0
        
        for j in range(len(nums)):
            s -= nums[j]
            while s <= 0: 
                # if s <= 0, it means the total sum of A[i] + ... + A[j] >= sum that we want.
                # s = 0 is also a good soln
                res = min(res, j - i + 1)
                s += nums[i]
                i += 1
                
        return res % (len(nums) + 1)