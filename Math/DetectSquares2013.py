class DetectSquares:
    '''
    Fix 2 diagnal points
    To compute count(p1):
    We try all points p3 which together with p1 form the diagonal of non-empty square, it means abs(p1.x-p3.x) == abs(p1.y-p3.y) && abs(p1.x-p3.x) > 0
    Since we have 2 points p1 and p3, we can form a square by computing the positions of 2 remain points p2, p4.
    p2 = (p1.x, p3.y)
    p4 = (p3.x, p1.y)
    '''
    def __init__(self):
        self.cnt = collections.Counter() 

    def add(self, point: List[int]) -> None:
        self.cnt[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        res = 0
        x1, y1 = point
        for (x3, y3), c in self.cnt.items():
            if abs(x3 - x1) == abs(y3 - y1) and abs(x3 - x1) > 0:
                res += c * self.cnt[(x1, y3)] * self.cnt[(x3, y1)]
        return res
        


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)