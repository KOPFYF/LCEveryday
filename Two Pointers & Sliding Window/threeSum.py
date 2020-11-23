class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 2 pointers, fix i and reduce to 2 sum
        # nums[j] + nums[k] = - nums[i],  0 <= i < j < k < n
        res = []
        nums.sort()
        if len(nums) < 3:
            return res

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]: 
                continue # dedup i
            l, r = i + 1, len(nums) - 1
            while l < r :
                s = nums[i] + nums[l] + nums[r]
                if s == 0:
                    res.append([nums[i] ,nums[l] ,nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]: 
                        l += 1 # dedup j
                    while l < r and nums[r] == nums[r + 1]: 
                        r -= 1 # dedup k
                elif s < 0 :
                    l += 1
                else:
                    r -= 1
        return res  
        