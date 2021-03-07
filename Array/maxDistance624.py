class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        # soln 1, one scan
        res = 0
        curmin, curmax = float('inf'), float('-inf')
        for a in arrays:
            res = max(res, max(a[-1] - curmin, curmax - a[0]))
            curmin, curmax = min(curmin, a[0]), max(curmax, a[-1])
        return res
        
        # soln 2
        m = len(arrays)
        MAX, max_i = max([(arrays[i][-1], i) for i in range(m)])
        MIN, min_i = min([(arrays[i][0], i) for i in range(m)])
        a = max(abs(arrays[i][0] - MAX) for i in range(m) if i != max_i)
        b = max(abs(arrays[i][-1] - MIN) for i in range(m) if i != min_i)
        return max(a, b)