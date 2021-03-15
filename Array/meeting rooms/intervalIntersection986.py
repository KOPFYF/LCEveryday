class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i, j = 0, 0
        m, n = len(firstList), len(secondList)
        res = []
        while i < m and j < n:
            s = max(firstList[i][0], secondList[j][0])
            e = min(firstList[i][1], secondList[j][1])
            if s <= e:
                res.append([s, e])
            if firstList[i][1] < secondList[j][1]:
                i += 1
            else:
                j += 1
        return res