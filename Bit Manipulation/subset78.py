class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # bit mask, time O(n * 2 ^ n)
        n = len(nums)
        res = []
        for mask in range(1 << n):
            s = []
            for j in range(n):
                if (mask & (1 << j) != 0):
                    s.append(nums[j])
            res.append(s)
        return res