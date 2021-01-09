class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key=lambda x: x[0]) # sort by start time
        for int1, int2 in zip(intervals[:-1], intervals[1:]):
            if int2[0] < int1[1]:
                return False
        return True