class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        # sort by start inc, end dec
        # only previous ones are possible to cover current one
        # Loop through the intervals, whenever current right most bound < next interval's right bound, 
        # it means current interval can NOT cover next interval, update right most bound and increase counter by 1.
        intervals.sort(key=lambda x: (x[0], -x[1]))
        # print(intervals) # [[1, 4], [2, 8], [3, 6]]
        cnt, cur = 0, 0
        for s, e in intervals:
            if cur < e: # cmp end time
                cur = e
                cnt += 1
                # print(s, e, cur, cnt)
        return cnt