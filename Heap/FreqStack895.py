class FreqStack:
    # Storing (count, index, number) in min-heap and keeping map of counts.

    def __init__(self):
        self.heap = []
        self.freqs = defaultdict(int)
        self.idx = 0

    def push(self, x: int) -> None:
        self.freqs[x] += 1
        heapq.heappush(self.heap, (-self.freqs[x], -self.idx, x))
        self.idx += 1

    def pop(self) -> int:
        freq, pos, x = heapq.heappop(self.heap)
        self.freqs[x] -= 1
        return x