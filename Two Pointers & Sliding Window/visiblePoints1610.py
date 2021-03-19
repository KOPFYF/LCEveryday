'''
convert all coordinates to radians
sort the array
use sliding window to find the longest window that satisfies arr[r] - arr[l] <= angle.


Assume you divide the plane into 4 quadrants (the top right being the first and the bottom right being the 4th). Now assume you have a bunch of points right above the x-axis in the 1st quadrant(your array of points starts with these) and a bunch of them right below the x-axis in the 4th quadrant(your array of points ends with these). If you have a sufficiently large angle of view, the only way you'll be able to include both these sets of points(that your array starts and ends with) in your solution is by converting your array into a circular array and that's what this line does.
'''

import math
class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        # sliding win, O(nlogn)/O(n)
        rads = []
        sameLoc = 0
        for x, y in points:
            if x == location[0] and y == location[1]:
                sameLoc += 1
                continue
            rads.append(math.atan2(y - location[1], x - location[0]))
        
        rads.sort()
        rads = rads + [x + 2.0 * math.pi for x in rads] # for circular array
        angle = angle * math.pi / 180 # turn to rads
        
        i = res = 0
        for j in range(len(rads)):
            while rads[j] - rads[i] > angle:
                i += 1
            res = max(res, j - i + 1)
        
        return res + sameLoc