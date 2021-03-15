class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        left, right = [], []
        l, r = newInterval[0], newInterval[1]
        for s, e in intervals:
            if e < l: 
                left.append([s, e])
            elif s > r:
                right.append([s, e])
            else:
                l = min(l, s)
                r = max(r, e)
        return left + [[l, r]] + right


class Solution1(object):
    def insert(self, intervals, new):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        res = []
        i = -1
        # print(intervals[1:], intervals[i+1:], [[4,6]] + [])
        for i, (s, e) in enumerate(intervals):
            if e < new[0]:
                # before
                res.append([s, e])
            elif s > new[1]: # overshoot
                i -= 1 # back one step and append all after
                break
            else:
                # merge zone
                new[1] = max(new[1], e)
                new[0] = min(new[0], s)
        # print(new, i, intervals[i+1:]) 
        return res + [new] + intervals[i + 1:]