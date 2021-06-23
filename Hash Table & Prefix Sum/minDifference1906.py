class Solution:
    def minDifference(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        res, dp = [], [[0] * (max(nums) + 1)]
        
        for num in nums:
            t = dp[-1][:]
            t[num] += 1
            dp.append(t)
            
        for i, j in queries:
            diff = [idx for idx, (x, y) in enumerate(zip(dp[j+1], dp[i])) if x != y]
            # print(diff)
            res.append(min([b - a for a, b in zip(diff, diff[1:])] or [-1]))
            
        return res