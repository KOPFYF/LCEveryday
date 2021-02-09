class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        # https://leetcode.com/problems/largest-rectangle-in-histogram/discuss/28917/AC-Python-clean-solution-using-stack-76ms
        # https://abhinandandubey.github.io/posts/2019/12/15/Largest-Rectangle-In-Histogram.html
        # keep a mono-inc stack
        heights.append(0)
        stack = [-1]
        ans = 0
        for i in range(len(heights)):
            while heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i - stack[-1] - 1
                ans = max(ans, h * w)
            stack.append(i)
        heights.pop()
        return ans
    
        heights.append(0)
        stack, res = [-1], 0 # init with last index
        for i, height in enumerate(heights):
            while stack and heights[stack[-1]] >= height: 
                h = heights[stack.pop()]
                w = i - 1 - stack[-1] if stack else i
                res = max(res, h * w)
            stack.append(i)
        return res