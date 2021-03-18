class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        # sweep line O(n^2), count row by row
        xs = sorted(set([x for x1, y1, x2, y2 in rectangles for x in (x1, x2)]))
        x2idx = {v:i for i, v in enumerate(xs)} 
        # rectangles = [[0,0,2,2],[1,0,2,3],[1,0,3,1]]
        # print(xs) # [0, 1, 2, 3]
        # print(x2idx) # {0: 0, 1: 1, 2: 2, 3: 3}
        count = [0] * len(x2idx) # sum for each row
        sweep_line = []
        for x1, y1, x2, y2 in rectangles:
            sweep_line.append([y1, x1, x2, 1])
            sweep_line.append([y2, x1, x2, -1])
        sweep_line.sort()
        # print(sweep_line) # [[0, 0, 2, 1], [0, 1, 2, 1], [0, 1, 3, 1], [1, 1, 3, -1], [2, 0, 2, -1], [3, 1, 2, -1]]

        cur_y = cur_x_sum = area = 0
        for y, x1, x2, diff in sweep_line:
            area += (y - cur_y) * cur_x_sum
            cur_y = y
            for i in range(x2idx[x1], x2idx[x2]):
                count[i] += diff
            # print(count)
            cur_x_sum = sum(x2 - x1 if c else 0 for x1, x2, c in zip(xs, xs[1:], count))
        
        return area % (10**9 + 7)