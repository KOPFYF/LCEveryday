class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # greedy: the interval with the earliest end time produces the maximal capacity to hold rest intervals.
        # if conflict, remove prev and leave more space for later
        # https://leetcode.com/problems/non-overlapping-intervals/discuss/276056/Python-Greedy-Interval-Scheduling
        # sort by end time
        end, cnt = float('-inf'), 0
        for s, e in sorted(intervals, key=lambda x: x[1]):
            if s >= end: 
                end = e
            else: 
                cnt += 1
        return cnt
        
        # sort by start time
        intervals.sort()
        end, cnt = float('-inf'), 0
        for s, e in intervals:
            if s >= end:
                end = e
            else:
                end = min(e, end)
                cnt += 1
        return cnt
                
        
        
        