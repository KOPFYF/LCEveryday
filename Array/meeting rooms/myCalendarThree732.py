class MyCalendarThree:

    def __init__(self):
        self.time = []
        self.k = 0

    def book(self, start: int, end: int) -> int:
        # O(n) insort
        bisect.insort(self.time, (start, 1))
        bisect.insort(self.time, (end, -1))
        
        cnt = 0
        for t, diff in self.time:
            cnt += diff
            self.k = max(self.k, cnt)
        return self.k