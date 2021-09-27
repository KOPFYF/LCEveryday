"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution1:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        # sweep line, O(nlog(n))/O(n), O(nlog(n)) for sorting, O(n) for scanning
        intervals = [] # flatten
        for ppl in schedule:
            for interval in ppl:
                intervals.append(interval)
        intervals.sort(key=lambda x:x.start) # sort all intervals by start time
        # print(intervals)
        
        res = []
        prev = intervals[0]
        for interval in intervals[1:]:
            if interval.start <= prev.end and interval.end > prev.end:
                # overlapp and merge
                prev.end = interval.end
            elif interval.start > prev.end:
                res.append(Interval(prev.end, interval.start))
                prev = interval
        return res


# T: O(n*log(k)), n is the number of intervals across all employees
#                 k is the number of employees
# S: O(k)
class Solution2:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        # collect first events of all employees
        heap = []
        for i, employee in enumerate(schedule):
            # (event.start, employee index, event index)
            heapq.heappush(heap, (employee[0].start, i, 0))

        res = []
        _, i, j = heap[0]
        prev_end = schedule[i][j].end
        while heap:
            _, i, j = heapq.heappop(heap)
            # check for next employee event and push it
            if j + 1 < len(schedule[i]):
                heapq.heappush(heap, (schedule[i][j + 1].start, i, j + 1))

            event = schedule[i][j]
            if event.start > prev_end:
                res.append(Interval(prev_end, event.start))
            prev_end = max(prev_end, event.end)
        return res



# T: O(n*log(k)), n is the number of intervals across all employees
#                 k is the number of employees
# S: O(k)
class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        iterator = heapq.merge(*schedule, key=operator.attrgetter('start'))
        res, prev_end = [], next(iterator).end
        for event in iterator:
            if event.start > prev_end:
                res.append(Interval(prev_end, event.start))
            prev_end = max(prev_end, event.end)
        return res