class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """        
        l = len(nums)
        if l < 2:
            return l
        i = 2
        for num in nums[2:]:
            if num != nums[i-2]:
                nums[i] = num
                i += 1
        return i