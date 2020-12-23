class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        i = 0
        cum = 0
        s = set()
        res = 0
        for j, num in enumerate(nums):
            while num in s:
                cum -= nums[i]
                s.remove(nums[i])
                i += 1
            cum += num
            res = max(res, cum)
            s.add(num)
                
        return res