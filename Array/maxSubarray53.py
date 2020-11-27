class Solution(object):
    def maxSubArray(self, A):
        """
        :type nums: List[int]
        :rtype: int
        """
        # DP, O(n)
        # a circular one: 918, then record min is needed as well
        curSum = res = A[0]
        for num in A[1:]:
            # It's a DP. curSum is dp[i], if it's negative, we abandon
            curSum = max(num, curSum + num)
            res = max(res, curSum)

        return res