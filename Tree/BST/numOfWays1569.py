'''
We separate all the elements into two lists, depending on whether they are less than or more than the root. Then we recurse on those left and right sublists. The combination is for the macro ordering between left and right, and the recursive factors are for the internal ordering of left and right themselves. I minus 1 from the result because we don't count the original ordering.
'''
class Solution:
    def numOfWays(self, nums: List[int]) -> int:

        def dfs(nums):
            if len(nums) <= 2: 
                return 1
            left = [v for v in nums if v < nums[0]]
            right = [v for v in nums if v > nums[0]]
            # comb: # of ways to create a combined list with order preserved from left&right
            res = comb(len(left) + len(right), len(right))
            return res * dfs(left) * dfs(right)
        return (dfs(nums) - 1) % (10**9 + 7)