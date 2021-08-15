
class Solution:
    def maxSumAfterOperation(self, nums: List[int]) -> int:
        # DP O(n)/O(1)
        prev_square = prev_no_square = 0
        res = 0
        for num in nums:
            no_square = max(num, num + prev_no_square)
            square = max(num*num, num*num + prev_no_square, num + prev_square)
            res = max(res, square)
            prev_square, prev_no_square = square, no_square
        
        return res

        # prefix sum to get subarray sum
        # DP O(n)/O(1)
        normal = nums[0]
        op = nums[0]**2
        res = max(normal, op)
        
        for i in range(1, len(nums)):
            prev_normal = normal
            prev_op = op
            normal = max(nums[i], nums[i] + prev_normal) # no square
            # 3 cases, prev op + current, just current op, normal + current op
            op = max(prev_op + nums[i], nums[i]**2, prev_normal + nums[i]**2)
            res = max(res, normal, op)
        return res
  
        