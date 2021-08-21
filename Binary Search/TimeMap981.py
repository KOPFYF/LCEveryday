class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[key].append([timestamp, value])
        

    def get(self, key: str, timestamp: int) -> str:
        arr = self.d[key]
        l, r = 0, len(arr)
        while l < r:
            m = (l + r) // 2
            if arr[m][0] <= timestamp:
                l = m + 1
            else:
                r = m
        # print(l, r, m)
        return arr[l - 1][1] if l != 0 else ""