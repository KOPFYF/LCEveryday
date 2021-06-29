'''
What we want is to find the next smaller element in the array(which is similar as: 
https://leetcode.com/problems/next-greater-element-i/), 
the index of next smaller element minus current index is the number of target array we can form
(which is equal to the longest target arr we can form start with current index).

For example: given [2,3,4,5,1], the next smaller element of 2 is 1. index(2) = 0, index(1) = 4. 
And the number of target array we can form is 4: [[2,3,4,5],[2,3,4],[2,3],[2]].

And we can always assume there is a smallest element at the end of the array. 
o for those element which we can't find a smaller element in the array, 
we can use len(arr) as the index of its next smaller element.

'''

class Solution:
    def validSubarrays(self, nums: List[int]) -> int:
        stack = [] # mono inc stack, next smaller element
        nums.append(-1) # to automatically pop out the left over
        res = 0
        for i, num in enumerate(nums):
            while stack and nums[stack[-1]] > num:
                res += i - stack.pop()
            stack.append(i)
        
        # print(nums, stack)
        return res


class Solution1:
    # a stupid version without append -1
    def validSubarrays(self, nums: List[int]) -> int:
        stack = [] # mono inc stack, next smaller element
        # nums.append(-1) # to automatically pop out the left over
        res = 0
        for i, num in enumerate(nums):
            while stack and nums[stack[-1]] > num:
                res += i - stack.pop()
            stack.append(i)
        
        while stack:
            res += len(nums) - stack.pop()

        return res

