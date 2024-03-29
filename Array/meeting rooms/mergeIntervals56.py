# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [intervals[0]]
        for s, e in intervals[1:]:
            if s <= res[-1][1] and e > res[-1][1]:
                res[-1][1] = e
            elif s > res[-1][1]:
                res.append([s, e])
        return res

        
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if (intervals is None or len(intervals) == 0): 
            return []
        intervals = sorted(intervals, key = lambda x: x.start) # sort by start time
        merged = [intervals[0]]
        counter = 0
        for i in range(1, len(intervals)): 
            previous = merged[counter]
            if (previous.end >= intervals[i].start):
                # merge
                mInt = Interval(previous.start, max(previous.end, intervals[i].end))
                merged[counter] = mInt
            else:
                # append directly cuz no overlap
                merged.append(intervals[i])
                counter += 1
        return merged