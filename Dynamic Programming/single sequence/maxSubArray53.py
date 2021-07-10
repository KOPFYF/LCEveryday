class Solution(object):
    def maxSubArray(self, A):
        """
        :type nums: List[int]
        :rtype: int
        """
        # DP, O(n)/O(1)， kadan's algorithm
        curSum = res = A[0]
        for num in A[1:]:
            # It's a DP. curSum is dp[i], if it's negative, we abandon
            curSum = max(num, curSum + num)
            res = max(res, curSum)

        return res


'''

Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
'''

class Solution1:
    def maxSubArray(self, nums: List[int]) -> int:
        # dp[i]: max subarray ending with nums[i]
        # O(n)/O(n)
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        
        for i in range(1, n):
            # if dp[i - 1] >= 0:
            #     dp[i] = dp[i - 1] + nums[i]
            # else:
            #     dp[i] = nums[i]
            dp[i] = max(0, dp[i - 1]) + nums[i]
        return max(dp)
        

            
        