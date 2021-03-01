class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.v1 = v1
        self.v2 = v2
        self.n1 = len(v1)
        self.n2 = len(v2)
        self.p1 = 0
        self.p2 = 0
        self.prev = 2

    def next(self) -> int:
        if self.hasNext():
            if self.prev == 2:
                if self.p1 < self.n1:
                    res = self.v1[self.p1]
                    self.p1 += 1
                    self.prev = 1
                else:
                    res = self.v2[self.p2]
                    self.p2 += 1
            else:
                if self.p2 < self.n2:
                    res = self.v2[self.p2]
                    self.p2 += 1
                    self.prev = 2
                else:
                    res = self.v1[self.p1]
                    self.p1 += 1
            return res

                
    def hasNext(self) -> bool:
        return self.p1 < self.n1 or self.p2 < self.n2