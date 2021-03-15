class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        res = []
        l, r = toBeRemoved[0], toBeRemoved[1]
        for s, e in intervals:
            if e <= l or s >= r:
                res.append([s, e])
            else:
                if s < l:
                    res.append([s, l])
                if e > r:
                    res.append([r, e])
        return res
        