class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        # 2 pointers, O(n^2)
        res = 0
        nums.sort()
        n = len(nums)
        for k in range(2, n):
            i, j = 0, k-1
            while i < j:
                if nums[i] + nums[j] > nums[k]:
                    res += j - i
                    j -= 1
                else:
                    i += 1
        return res