class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # 2 Pointers, time O(n), space O(1)
        # Keep track of the max height from forward & backward directions, call them leftmax and rightmax.
        if not height or len(height) < 3:
            return 0
    
        i, j = 0, len(height) - 1
        res = 0
        lmax, rmax = 0, 0
        while i < j:
            lmax = max(lmax, height[i])
            rmax = max(rmax, height[j])
            if lmax < rmax:
                # lmax is smaller than rightmax, so the (lmax-height[i]) water can be stored
                res += (lmax - height[i])
                i += 1
            else:
                res += (rmax - height[j])
                j -= 1
        return res