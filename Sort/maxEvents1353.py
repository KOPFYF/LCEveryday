'''
Sort events increased by start time.
Priority queue pq keeps the current open events.

Iterate from the day 1 to day 100000,
Each day, we add new events starting on day d to the queue pq.
Also we remove the events that are already closed.

Then we greedily attend the event that ends soonest.
If we can attend a meeting, we increment the result res.

'''
class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:

        # greedy, choose the event that ends sooner
        events.sort() # sort by start time
        total_days = max(event[1] for event in events)
        hq = []
        
        day, cnt, eid = 1, 0, 0
        while day <= total_days:
            # no events available today, move to next event
            if eid < len(events) and not hq:
                day = events[eid][0]
            
            # add all possible events <= day to heap
            while eid < len(events) and events[eid][0] <= day:
                heapq.heappush(hq, events[eid][1]) # store end time
                eid += 1
            
            # if event on top of heap expired, remove it
            while hq and hq[0] < day:
                heapq.heappop(hq)
            
            # attend event which will end sooner
            if hq:
                heapq.heappop(hq)
                cnt += 1
            elif eid >= len(events):
                break
            day += 1
        return cnt
    
        # TLE
        seen = [0] * 100001    
        for s, t in sorted(events, key=lambda e:e[1]):
            for i in range(s, t + 1):
                if seen[i]: continue
                seen[i] = 1
                break
        return sum(seen)

        
                