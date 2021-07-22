class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return n
        
        i = 2 # index of output array
        for num in nums[2:]: # loop all rest
            if num != nums[i - 2]: # if find a new num
                nums[i] = num # replace i
                i += 1 # i++
        return i