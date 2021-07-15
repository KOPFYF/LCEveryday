class Solution0:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # a + b + c close to target, aka, b + c close to target - a
        def twoSumClosest(nums, i, cur):
            nonlocal res
            j = len(nums) - 1
            while i < j:
                tmp = nums[i] + nums[j] + cur
                if abs(tmp - target) < abs(res - target):
                    res = tmp
                if tmp < target:
                    i += 1
                else:
                    j -= 1
        
        nums.sort()
        res = float('inf')
        for i, num in enumerate(nums):
            twoSumClosest(nums, i + 1, num)
            if res == target: 
                break
        return res


class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        res = nums[0] + nums[1] + nums[2]
        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                num = nums[i] + nums[j] + nums[k]
                if abs(num - target) < abs(res - target): 
                    res = num
                if num < target:
                    j += 1
                else:
                    k -= 1
        return res