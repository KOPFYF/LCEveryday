class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        s = sum(nums)
        left, right = 0, s - nums[0]
        if left == right:
            return 0
        for i in range(1, len(nums)):
            left += nums[i - 1]
            right -= nums[i]
            if left == right:
                return i
        return -1


        s, p_sum = sum(nums), 0
        for i, num in enumerate(nums):
            if p_sum == (s - num) / 2.0:
                return i
            p_sum += num
        return -1