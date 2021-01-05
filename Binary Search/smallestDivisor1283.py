class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def check(divisor):
            return sum((num - 1) // divisor + 1 for num in nums) <= threshold

        l, r = 1, max(nums)
        while l < r:
            m = l + (r - l) // 2
            if check(m):
                r = m
            else:
                l = m + 1
        return l