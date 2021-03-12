class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # greedy, sort by end time
        points.sort(key=lambda x: x[1])
        cnt, end = 0, float('-inf')
        for s, e in points:
            if s > end:
                cnt += 1
                end = e
        return cnt