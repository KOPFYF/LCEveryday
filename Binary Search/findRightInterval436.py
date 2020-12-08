class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        if n <= 1: return [-1]
        
        idx_sort = sorted(range(n), key=lambda i:intervals[i][0])
        start_sort = [intervals[i][0] for i in idx_sort]
        
        res = []
        for start, end in intervals:
            idx = bisect.bisect_left(start_sort, end)
            if idx == n:
                res.append(-1)
            else:
                res.append(idx_sort[idx])
            # print(end, idx, idx_sort)
        return res