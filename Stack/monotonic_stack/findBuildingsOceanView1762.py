class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        '''
        heights = [4,2,3,1]
        mono dec stack = [4,3,1], 2 is poped out
        stack stores index
        
        '''
        stack = []
        res = []
        for i, height in enumerate(heights):
            while stack and height >= heights[stack[-1]]:
                stack.pop()
            stack.append(i)
        return stack