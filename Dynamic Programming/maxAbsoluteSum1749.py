class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        def maxSum(nums):
            curSum = res = nums[0]
            for num in nums[1:]:
                # It's a DP. curSum is dp[i], if it's negative, we abandon
                curSum = max(num, curSum + num)
                res = max(res, curSum)
            return res
        
        def minSum(nums):
            curSum = res = nums[0]
            for num in nums[1:]:
                # It's a DP. curSum is dp[i], if it's positive, we abandon
                curSum = min(num, curSum + num)
                res = min(res, curSum)
            return res
        
        a, b = maxSum(nums), minSum(nums)
        return max(abs(a), abs(b))