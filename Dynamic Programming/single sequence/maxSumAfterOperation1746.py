class Solution:
    def maxSumAfterOperation(self, nums: List[int]) -> int:
        # DP O(n)
        normal = nums[0]
        op = nums[0]**2
        res = max(normal, op)
        
        for i in range(1, len(nums)):
            prev_normal = normal
            prev_op = op
            normal = max(nums[i], nums[i] + prev_normal) # no square
            op = max(prev_op + nums[i], nums[i]**2, prev_normal + nums[i]**2)
            
            res = max(res, normal, op)
        
        return res