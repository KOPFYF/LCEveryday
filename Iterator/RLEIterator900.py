class RLEIterator:

    def __init__(self, encoding: List[int]):
        self.encoding = encoding
        self.idx = 0 # idx of cnt, followed by a num
        self.dq = deque()

    def next(self, n: int) -> int:
        while self.idx + 1 < len(self.encoding):
            if n <= self.encoding[self.idx]:
                self.encoding[self.idx] -= n
                return self.encoding[self.idx + 1]
            # not find the value, for example, 0,9
            n -= self.encoding[self.idx]
            self.idx += 2
        return -1