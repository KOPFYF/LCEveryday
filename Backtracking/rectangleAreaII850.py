class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        # recursion, O(n^2)
        def helper(path, cur, pos):
            if pos >= len(path):
                path.append(cur)
                return
            
            cx1, cy1, cx2, cy2 = cur
            rx1, ry1, rx2, ry2 = path[pos]
            if cx2 <= rx1 or cx1 >= rx2 or cy2 <= ry1 or cy1 >= ry2: 
                # no overlap, directly append
                helper(path, cur, pos + 1)
                return
            
            if cx1 < rx1:
                helper(path, [cx1, cy1, rx1, cy2], pos + 1)
            if cx2 > rx2:
                helper(path, [rx2, cy1, cx2, cy2], pos + 1)
            if cy1 < ry1:
                helper(path, [max(cx1, rx1), cy1, min(cx2, rx2), ry1], pos + 1)
            if cy2 > ry2:
                helper(path, [max(cx1, rx1), ry2, min(cx2, rx2), cy2], pos + 1)
        
        path = []
        for rect in rectangles:
            helper(path, rect, 0)
        cal_area = lambda r : (r[2] - r[0]) * (r[3] - r[1])
        # print(path)
        return sum(cal_area(r) for r in path) % (10**9 + 7)