class MyCalendar:

    def __init__(self):
        self.events = []

    def book(self, start: int, end: int) -> bool:
        # Brute force O(n^2) for n check in total
        for s, e in self.events:
            if max(s, start) < min(e, end):
                # overlapped
                return False
        self.events.append((start, end))
        return True


# https://leetcode.com/problems/my-calendar-i/discuss/109476/Binary-Search-Tree-python

# Binary Search
class MyCalendar:

    def __init__(self):
        self.arr = []

    def book(self, start: int, end: int) -> bool:
        index = self.bisect(start)
        # append at the end
        if index == len(self.arr): 
            self.arr.append((start, end))
            return True
        if end > self.arr[index][0]: 
            # overlapped
            return False
        # no overlap, insert
        self.arr = self.arr[:index] + [(start, end)] + self.arr[index:]
        return True
    
    #bisect_right self-implementation search by key= lambda x: x[1]
    def bisect(self, val):
        # bisect start into end 
        if not self.arr: 
            return 0
        if val >= self.arr[-1][1]: 
            return len(self.arr)

        l, r = 0, len(self.arr)-1
        while l < r:
            m = (l + r) // 2
            if self.arr[m][1] <= val: 
                l = m+1
            else: 
                r = m
        return l


class MyCalendar:

    def __init__(self):
        self.ends = []
        self.schedule = []

    def book(self, start: int, end: int) -> bool:
        # bisect new start and insert after end, bisect_right
        index = bisect.bisect(self.ends, start)
        if index == len(self.ends): 
            self.ends.append(end)
            self.schedule.append((start, end))
            return True
        if self.schedule[index][0] < end: 
            # overlapped
            return False
        self.ends = self.ends[:index] + [end] + self.ends[index:]
        self.schedule = self.schedule[:index] + [(start, end)] + self.schedule[index:]
        return True