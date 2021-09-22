class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        # dp, O(n)/O(n)
        # dp[i]: # end with i, excluding prev
        # input: [1,3,5,7,9,15,20,25,28,29]
        # dp:    [0,0,1,2,3,0 ,0, 1, 0, 0 ]
        n = len(nums)
        dp = [0] * n
        res = 0
        for i in range(2, n):
            if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
                # check each subarray with len = 3
                dp[i] = dp[i-1] + 1
                res += dp[i]
        return res