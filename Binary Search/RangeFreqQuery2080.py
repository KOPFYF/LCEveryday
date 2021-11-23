class RangeFreqQuery:

    def __init__(self, arr: List[int]):
        self.dic = defaultdict(list)
        for i, a in enumerate(arr):
            self.dic[a].append(i)
        for a in self.dic.keys():
            self.dic[a].sort()
        

    def query(self, left: int, right: int, value: int) -> int:
        idxs = self.dic[value]
        cnt = 0
        l = bisect_left(idxs, left)
        r = bisect_right(idxs, right)
        return r - l