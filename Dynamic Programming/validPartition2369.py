'''
For the current element, dp[i] indicates if the array can be partitioned up to that element.

For element dp[i + 1], the partition is valid if:

dp[i - 1] == true and we have a partition of two elements, or,
dp[i - 2] == true and we have a partition of three elements.
Since we only need to look 3 elements back, we can use a rolling dp array for constant memory complexity.

'''
class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        @cache
        def dfs(i: int) -> bool:
            if i >= n - 1:
                return i == n
            
            case1 = nums[i] == nums[i + 1]
            case2 = i < n - 2 and nums[i] == nums[i + 1] == nums[i + 2]
            case3 = i < n - 2 and nums[i] + 1 == nums[i + 1] == nums[i + 2] - 1
            return case1 and dfs(i + 2) or ((case2 or case3) and dfs(i + 3) )
            
        
        return dfs(0)