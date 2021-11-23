class Solution:
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        stack, res = [], [-1] * n
        # Push the index on the stack. If the current number b is bigger than the last number a in the stack(found by index), then we find the next great element for a.
        # Process it twice as it is a circular array to make sure that we can reread the next greater element after every element.
        # use i or i % n, they point to the same element
        A = nums + nums
        for i in range(n * 2):
            while stack and A[stack[-1]] < A[i % n]:
                res[stack.pop()] = A[i % n]
            stack.append(i % n)
        return res