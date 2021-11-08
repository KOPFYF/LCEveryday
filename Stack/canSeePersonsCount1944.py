class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        '''
        [10,6,8,5,11,9]
        
        i.  h.   stack.    res
        0.  10.   [0]      [0, 0, 0, 0, 0, 0]
        1   6.    [0,1]    [1, 0, 0, 0, 0, 0]
        2.  8.    [0,2]    [2, 1, 0, 0, 0, 0]
        3.  5.    [0,2,3]  [2, 1, 1, 0, 0, 0]
        4.  11.   [4]      [3, 1, 2, 1, 0, 0]
        5.  9.    [4,5]    [3, 1, 2, 1, 1, 0]
        
        
        '''
        
        res = [0] * len(heights)
        stack = [] # mono-dec stack
        
        for i, h in enumerate(heights):
            while stack and h > heights[stack[-1]]:
                res[stack.pop()] += 1
            # now it's a dec stack, like 10-8-5
            print(stack, res)
            if stack:
                res[stack[-1]] += 1
            stack.append(i)
            print(i, h, stack, res)
        return res