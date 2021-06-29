"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        # similar to merging intervals (https://leetcode.com/problems/merge-intervals/description/)
        # it doesn't matter which employee an interval belongs to, so just flatten
        intervals = sorted([ints for ppl in schedule for ints in ppl], key=lambda x:x.start)
        res = []
        prev = intervals[0]
        for interval in intervals[1:]:
            if interval.start <= prev.end and interval.end > prev.end:
                # overlapped, merge them
                prev.end = interval.end
            elif interval.start > prev.end:
                res.append(Interval(prev.end, interval.start))
                prev = interval
        
        return res