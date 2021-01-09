class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # count airplane in the sky
        ls = []
        for i, j in intervals:
            ls.append((i, 1))
            ls.append((j, -1))
            
        # ls.sort(key = lambda x:(x[0], x[1]))
        ls.sort()
        res, cnt = 0, 0
        for k, v in ls:
            cnt += v
            res = max(res, cnt)
        return res
    
        # shorter version
        res = cur = 0
        for i, v in sorted(x for i, j in intervals for x in [[i, 1], [j, -1]]):
            cur += v
            res = max(res, cur)
        return res
            
        
        
        intervals.sort(key = lambda x:x[0]) # sort by start time
        hq = [] # store the end time
        for sch in intervals:
            if hq and sch[0] >= hq[0]:
                heapq.heappushpop(hq, sch[1])
            else:
                heapq.heappush(hq, sch[1])
        return len(hq)