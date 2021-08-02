'''
https://leetcode.com/problems/trapping-rain-water/discuss/178028/Stack-with-Explanation-(Java-Python-Scala)

        __     __rightUpper2
leftUpper |  _|
          |_| rightUpper1
           ^
      lowerHeight
rightUpper1 traps 1 x 1(width x height) units of water.
rightUpper2 traps 2 x 1(width x height) units of water.

Stack store decreasing heights that can be possible leftUpper .
Whenever we meet a rightUpper, we should accumulate water trapped.

How much water is trapped because of the rightUpper?
water trapped = width * height
The width of water trapped depends on distance from leftUpper to rightUpper, so we save index rather than height
The height of water trapped depends on min(leftUpper, rightUpper) - lowerHeight.
'''
class Solution:
    def trap(self, height: List[int]) -> int:
        # mono dec stack, when inc, pop out
        stack, res = [], 0 # stack stores index
        
        for j, h in enumerate(height):
            # process when you see a valley pattern, like 312 or 213
            while stack and h > height[stack[-1]]:
                bottom = height[stack.pop()]
                if not stack:
                    break
                i = stack[-1]
                diff = min(height[i], h) - bottom
                width = j - i - 1
                res += diff * width
            stack.append(j)
        return res
        
            
        
        
        # 2 pointers
        n = len(height)
        if n < 3:
            return 0
        
        l, r = 0, n - 1
        lmax, rmax, res = 0, 0, 0
        while l < r:
            lmax = max(lmax, height[l])
            rmax = max(rmax, height[r])
            if lmax < rmax:
                # check left
                res += (lmax - height[l])
                l += 1
            else:
                res += (rmax - height[r])
                r -= 1
        return res
            