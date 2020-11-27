class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        # Same as 52, but this is circular
        # so we want to split the circle into 2 subarrays, to max one or min the other one
        total, maxSum, curMax, minSum, curMin = sum(A), A[0], 0, A[0], 0
        for a in A:
            curMax = max(curMax + a, a)
            maxSum = max(maxSum, curMax)
            curMin = min(curMin + a, a)
            minSum = min(minSum, curMin)
        return max(maxSum, total - minSum) if maxSum > 0 else maxSum