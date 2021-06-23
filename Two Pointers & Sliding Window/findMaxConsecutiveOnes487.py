class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        i, n = 0, len(nums)
        res, zero = 0, 0
        for j, num in enumerate(nums):
            if not num:
                zero += 1
            while zero > 1:
                if nums[i] == 0:
                    zero -= 1
                i += 1
            res = max(res, j - i + 1)
        
        return res