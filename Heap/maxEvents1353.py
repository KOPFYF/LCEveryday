class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort()
        pq = []
        res, i, n, d = 0, 0, len(events), 0
        
        while i < n or pq:
            if not pq:
                d = events[i][0]
            while i < n and d >= events[i][0]: # push all events we can possibly attend
                heapq.heappush(pq, events[i][1]) # min heap store end time
                i += 1
            
            heapq.heappop(pq) # greedily attend the earliest ending event
            res += 1
            d += 1 # mark one day of event attended
            while pq and pq[0] < d: # remove all impossible-to-attend events
                heapq.heappop(pq)
        
        return res