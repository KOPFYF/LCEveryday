class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        1,1,2,3,4,5
        target = 5
        
        '''
        nums.sort()
        n = len(nums)
        
        def twoSum(i, j, target):
            res = []
            l, r = i, j
            while l < r:
                if nums[l] + nums[r] < target or (l > i and nums[l - 1] == nums[l]):
                    l += 1
                elif nums[l] + nums[r] > target or (r + 1 < j and nums[r] == nums[r + 1]):
                    r -= 1
                else:
                    res.append([nums[l], nums[r]])
                    l += 1
                    r -= 1
            return res
        
        res = []
        for i in range(n - 2):
            # i < j < k
            # target: nums[j] + nums[k] = -nums[i]
            if nums[i] > 0:
                break
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            j, k = i + 1, n - 1
            for path in twoSum(j, k, -nums[i]):
                res.append([nums[i]] + path)
        return res
        

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


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        1,1,2,3,4,5
        target = 5
        
        '''
        nums.sort()
        
        def twoSum(nums, target):
            l, r = 0, len(nums) - 1
            res = []
            while l < r:
                if nums[l] + nums[r] < target or (l > 0 and nums[l - 1] == nums[l]):
                    l += 1
                elif nums[l] + nums[r] > target or (r + 1 < len(nums) and nums[r] == nums[r + 1]):
                    r -= 1
                else:
                    res.append([nums[l], nums[r]])
                    l += 1
                    r -= 1
            return res
        
        res = []
        for i in range(len(nums) - 2):
            # i < j < k
            # target: nums[j] + nums[k] = -nums[i]
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            for path in twoSum(nums[i+1:], -nums[i]):
                res.append([nums[i]] + path)
        return res
        