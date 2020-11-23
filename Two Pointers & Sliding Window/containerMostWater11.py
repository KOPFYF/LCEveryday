class Solution(object):
    def maxArea(self, h):
        """
        :type height: List[int]
        :rtype: int
        """
        #   1 2 3 4 5 6
        # 1 x ------- o
        # 2 x x - o o o
        # 3 x x x o | |
        # 4 x x x x | |
        # 5 x x x x x |
        # 6 x x x x x x
        i, j = 0, len(h) - 1
        vol = 0
        while i < j:
            vol = max(vol, (j - i) * min(h[i], h[j]))
            if h[i] < h[j]:
                i += 1
            else:
                j -= 1
            # print(i, j, vol)
        return vol