class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        res = []
        for s, e in intervals:
            if e <= toBeRemoved[0] or s >= toBeRemoved[1]:
                res.append([s, e])
            else:
                if s < toBeRemoved[0]:
                    res.append([s, toBeRemoved[0]])
                if e > toBeRemoved[1]:
                    res.append([toBeRemoved[1], e])
        return res
        