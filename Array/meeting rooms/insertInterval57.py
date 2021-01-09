class Solution(object):
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
            elif s > new[1]:
                i -= 1 # back one step and append all after
                break
            else:
                # merge zone
                new[1] = max(new[1], e)
                new[0] = min(new[0], s)
        # print(new, i, intervals[i+1:]) 
        return res + [new] + intervals[i + 1:]