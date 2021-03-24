'''
1. the external corners must appear only once, and the ones inside have to be an even number (we filter them with xor).
2. the total area of all the rectangles together, has to be equal to the area created by the external corners
'''

class Solution(object):
    def isRectangleCover(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: bool
        """
        corner, area = set(), 0
        a, b, c, d = float('inf'), float('inf'), float('-inf'), float('-inf')
    
        for x1, y1, x2, y2 in rectangles:
            if x1 <= a and y1 <= b: # left up
                a, b = x1, y1
            if x2 >= c and y2 >= d: # right down
                c, d = x2, y2
            corner ^= {(x1, y1), (x2, y2), (x1, y2), (x2, y1)} # set xor
            area += (x2 - x1) * (y2 - y1)
        return corner == {(a, b), (c, d), (a, d), (c, b)} and area == (c - a) * (d - b)
            