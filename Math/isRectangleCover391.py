'''
1. the external corners must appear only once, and the ones inside have to be an even number (we filter them with xor).
2. the total area of all the rectangles together, has to be equal to the area created by the external corners
'''

class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        corner = set()
        a, b, c, d, area = float('inf'), float('inf'), float('-inf'), float('-inf'), 0
        for x1, y1, x2, y2 in rectangles:
            if x1 <= a and y1 <= b: 
                a, b = x1, y1
            if x2 >= c and y2 >= d: 
                c, d = x2, y2
            area += (x2 - x1) * (y2 - y1)
            corner ^= {(x1, y1), (x2, y2), (x1, y2), (x2, y1)} # set xor
        return corner == {(a, b), (c, d), (a, d), (c, b)} and area == (c - a) * (d - b)