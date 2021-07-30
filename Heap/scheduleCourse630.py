'''
Sort courses by the end date, this way, when we're iterating through the courses, we can switch out any previous course with the current one without worrying about end date.

Next, we iterate through each course, if we have enough days, we'll add it to our priority queue. If we don't have enough days, then we can either
2.1 ignore this course OR
2.2 We can replace this course with the longest course we added earlier.
'''
class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        # sort by last day
        # max heap stores course duration
        # greedily remove the largest-length course until the total duration start is <= end
        courses.sort(key=lambda x:x[1])
        
        pq = []
        start = 0
        for dur, end in courses:
            start += dur
            heapq.heappush(pq, -dur)
            while start > end:
                # each time we only need to remove at most one element from the pq
                start += heapq.heappop(pq) # start--
        return len(pq)
        