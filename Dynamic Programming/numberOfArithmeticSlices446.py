'''
dp[i][j] stores the number of arithmetic slices (including those with only length 2) whose constant difference is j ending at i. The key is basically to store all 2+-length arithmetic slices (which is helps to build up the solution from its sub-problems) while only adding valid 3+-length slices to the total.

The we iterate over all pairs in the array. Each (A[j], A[i]) is a 2-length slice with constant difference A[i] - A[j] that we've never encountered before, so increment dp[i][A[i] - A[j]] by 1 (but leave the total as is, because its not length 3 or more).

If there are any slices with A[i] - A[j] length that finish at index j (if A[i]-A[j] in dp[j]:), we 'extend' them to index i and add to the total, since any slice that terminated at index j would now have at least length 3 terminating at i.
'''
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        dp = [defaultdict(int) for _ in range(n)]
        for i in range(n):
            for j in range(i):
                dp[i][nums[i] - nums[j]] += 1 # still count weak Arithmetic(len=2)
                if nums[i] - nums[j] in dp[j]:
                    dp[i][nums[i] - nums[j]] += dp[j][nums[i] - nums[j]] 
                    res += dp[j][nums[i] - nums[j]] 
        return res