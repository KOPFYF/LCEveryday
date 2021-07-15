class Solution0:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def twoSum(nums, i, target):
            j = len(nums) - 1
            while i < j:
                if nums[i] + nums[j] + target == 0:
                    res.append([target, nums[i], nums[j]])
                    # must not contain duplicate triplets
                    while i < j and nums[i + 1] == nums[i]:
                        i += 1
                    while i < j and nums[j - 1] == nums[j]:
                        j -= 1
                    i += 1
                    j -= 1
                elif nums[i] + nums[j] + target < 0:
                    i += 1
                else:
                    j -= 1
        
        res = []
        nums.sort()
        for i, num in enumerate(nums):
            if num > 0:
                # current num is pos, no way
                return res
            if i > 0 and nums[i - 1] == num:
                continue
            twoSum(nums, i + 1, num)
        return res


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 2 pointers, O(n^2) fix i and reduce to 2 sum
        # nums[j] + nums[k] = - nums[i],  0 <= i < j < k < n
        nums.sort()
        res, n, target = [], len(nums), 0
        if n < 3: return []
        
        for i in range(n - 2):
            if i and nums[i] == nums[i - 1]:
                continue
            j, k = i + 1, n - 1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if s == target:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j - 1]: 
                        j += 1 # dedup j
                    while j < k and nums[k] == nums[k + 1]: 
                        k -= 1 # dedup k
                elif s < target:
                    j += 1
                else:
                    k -= 1
        return res 
        