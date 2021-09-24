'''
The naive solution is to check all possible subsequences. This works in O(2^n).
Split into 2 halfs and solve with two Sum Closest

'''

class Solution:
    def minAbsDifference(self, nums: List[int], goal: int) -> int:
        def dfs(i, nums, cur, res):
            # cur: current sum, res: final set of sum
            if i == len(nums):
                res.add(cur)
                return
            dfs(i+1, nums, cur+nums[i], res) # take i-th
            dfs(i+1, nums, cur, res) # no take
            
        sum1, sum2 = set(), set()
        dfs(0, nums[:len(nums)//2], 0, sum1)
        dfs(0, nums[len(nums)//2:], 0, sum2)
        
        # sort and binary search the second half
        sum2 = sorted(sum2)
        res = float('inf')
        for s in sum1:
            left = goal - s
            i2 = bisect.bisect_left(sum2, left)
            # choose one of two, left or right
            # for example, goal = 5, s = 3, left = 2, sum2 = [1, >insert<  3,4]
            if i2 < len(sum2):
                res = min(res, abs(left - sum2[i2])) # check right, 3
            if i2 > 0:
                res = min(res, abs(left - sum2[i2-1])) # check left, 1
        return res
            