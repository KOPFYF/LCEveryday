class Solution0:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        return self.kSum(nums, target, 4)
        
    def twoSum(self, nums, target):
        l, r = 0, len(nums) - 1
        res = []
        while l < r:
            if nums[l] + nums[r] < target:
                l += 1
            elif nums[l] + nums[r] > target:
                r -= 1
            else:
                res.append([nums[l], nums[r]])
                while l < r and nums[l + 1] == nums[l]:
                    l += 1
                while l < r and nums[r - 1] == nums[r]:
                    r -= 1
                l += 1
                r -= 1    
        return res
    
    # def twoSum(self, nums, target):
    #     res, i, j = [], 0, len(nums) - 1
    #     while i < j:
    #         s = nums[i] + nums[j]
    #         if s < target or (i > 0 and nums[i] == nums[i - 1]):
    #             i += 1
    #         elif s > target or (j < len(nums) - 1 and nums[j] == nums[j + 1]):
    #             j -= 1
    #         else:
    #             res.append([nums[i], nums[j]])
    #             i += 1
    #             j -= 1
    #     return res
        
    def kSum(self, nums, target, k):
        if not nums or nums[0] * k > target or nums[-1] * k < target:
            return []
        if k == 2:
            return self.twoSum(nums, target)
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            paths = self.kSum(nums[i+1:], target - nums[i], k - 1)
            for path in paths:
                res.append([nums[i]] + path)
        return res


class Solution(object):
    def fourSum(self, nums, target):
        nums.sort()
        results = []
        self.findNsum(nums, target, 4, [], results)
        return results

    def findNsum(self, nums, target, N, result, results):
        if len(nums) < N or N < 2: 
            return

        # base case, solve 2-sum
        if N == 2:
            l, r = 0, len(nums)-1
            while l < r:
                if nums[l] + nums[r] == target:
                    results.append(result + [nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1 # dedup left pointer
                    while r > l and nums[r] == nums[r + 1]:
                        r -= 1 # dedup right pointer
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    r -= 1
        # recursion
        else:
            for i in range(0, len(nums) - N + 1):   
                if target < nums[i] * N or target > nums[-1] * N:  
                    break # take advantages of sorted list
                if i == 0 or i > 0 and nums[i] != nums[i - 1]:  
                    # recursively reduce N
                    self.findNsum(nums[i + 1:], target - nums[i], N - 1, result + [nums[i]], results)
        return