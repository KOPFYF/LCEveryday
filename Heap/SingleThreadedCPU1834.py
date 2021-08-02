class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # task: [start time, process time]
        # shortest processing time, use min heap to store process time
        events = [(start, dur, i) for i, (start, dur) in enumerate(tasks)]
        events.sort()
        hq = []
        res = []
        end = 0
        for start, dur, i in events:
            while hq and end < start: 
                # start > current end time, have pending task to process
                nxt_dur, nxt_idx, nxt_start= heapq.heappop(hq)
                res.append(nxt_idx)
                end = max(end, nxt_start) + nxt_dur
            
            heapq.heappush(hq, (dur, i, start))
        
        # print(hq)
        # print(res)
        while hq:
            # in case hq is not empty
            res.append(heapq.heappop(hq)[1])
        
        return res