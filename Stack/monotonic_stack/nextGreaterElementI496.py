class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        # go through nums, if first satisfied, store into dict. 
        # stack[-1] is the next number we want to check
        n = len(nums)
        res = {}
        stack = []
        for num in nums:
            while stack and stack[-1] < num:
                res[stack.pop()] = num
            stack.append(num)
        return [res[x] if x in res else -1 for x in findNums]
    
        # what if we store index in stack?
        n = len(nums)
        res = {}
        stack = []
        for i, num in enumerate(nums):
            while stack and nums[stack[-1]] < num:
                res[nums[stack.pop()]] = num
            stack.append(i)
        return [res[x] if x in res else -1 for x in findNums]