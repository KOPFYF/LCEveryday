class Solution(object):
    def minOperations(self, nums, x):
        n = len(nums)
        if x < nums[0] and x < nums[-1] or x > sum(nums):
            return -1
        i, res = 0, -1
        target = sum(nums) - x
        for j in range(n):
            target -= nums[j]
            while target < 0:
                target += nums[i]
                i += 1
            if target == 0:
                res = max(res, j - i + 1)
        if res != -1:
            return n - res
        else:
            return -1