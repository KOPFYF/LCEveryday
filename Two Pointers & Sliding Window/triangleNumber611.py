class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        # 2 ptrs
        # a <= b <= c
        # then one condition a + b > c will do

        res = 0
        nums.sort()
        n = len(nums)
        for k in range(n-1, 1, -1):
            c = nums[k]
            i = 0
            j = k - 1
            while i < j:
                if nums[i] + nums[j] > c:
                    res += j - i
                    j -= 1
                else:
                    i += 1
        return res