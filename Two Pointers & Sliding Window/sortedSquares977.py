class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # O(n)
        n = len(nums)
        res = [0] * n
        l, r = 0, n - 1
        i = n - 1
        while i >= 0:
            if abs(nums[l]) > abs(nums[r]):
                res[i] = nums[l] ** 2
                l += 1
            else:
                res[i] = nums[r] ** 2
                r -= 1
            i -= 1
        return res