class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        
        def intersect(p_left, p_right, q_left, q_right):
            return min(p_right, q_right) > max(p_left, q_left)
        
        return (intersect(rec1[0], rec1[2], rec2[0], rec2[2]) and # width > 0
                intersect(rec1[1], rec1[3], rec2[1], rec2[3]))    # height > 0


# https://stackoverflow.com/questions/306316/determine-if-two-rectangles-overlap-each-other
'''

if (RectA.Left < RectB.Right && RectA.Right > RectB.Left &&
     RectA.Top > RectB.Bottom && RectA.Bottom < RectB.Top ) 

    In summary:
    1. all left < right
    2. all bottom < top
'''
class Rect:
    def __init__(self, x1, y1, x2, y2):
        # (x1, y1) is left upper, (x2, y2) is bottom down
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

class Check:
    def check_overlap(self, rect1, rect2):

        check1 = min(rect1.x2, rect2.x2) > max(rect1.x1, rect2.x1) # width > 0
        check2 = min(rect1.y2, rect2.y2) > max(rect1.y1, rect2.y1) # height > 0

        return check1 and check2
