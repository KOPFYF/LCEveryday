class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        res = [0] * len(heights)
        stack = []
        for i, h in enumerate(heights):
            # print(stack, res)
            while stack and heights[stack[-1]] <= h:
                # print('while', stack)
                res[stack.pop()] += 1 
            if stack:
                res[stack[-1]] += 1 # 
            stack.append(i)
        return res