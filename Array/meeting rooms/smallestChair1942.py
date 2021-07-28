class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:        
        # heap, sit on the unoccupied chair with the smallest number
        intervals = []
        for fid, (s, e) in enumerate(times):
            intervals.append((s, 1, fid))
            intervals.append((e, -1, fid))
        intervals.sort()
        
        hq = [] # store available chair id
        chair_cnt = 0
        chairs_map = {} # player-to-seat mapping 
        for cut, d, fid in intervals: # go by the chronogical order of time
            if d == 1: # up
                if hq: # have at leat one available seat, use the smallest one
                    chair_id = heapq.heappop(hq)
                else: # no available seat, chair++
                    chair_id = chair_cnt
                    chair_cnt += 1
                if fid == targetFriend:
                    return chair_id
                chairs_map[fid] = chair_id # 
            else: # down, release seat
                heapq.heappush(hq, chairs_map[fid]) # new seat available

class Solution1:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        # sweep
        events = []
        for idx, (start, end) in enumerate(times):
            events.append([end, 0, idx])
            events.append([start, 1, idx])
        events.sort()
        
        free = list(range(len(times)))
        chairs = {}
        for event in events:
            if event[1] == 1:
                chair = min(free)
                free.remove(chair) # O(n)
                chairs[event[2]] = chair
                if event[2] == targetFriend:
                    return chair
            else:
                free.append(chairs[event[2]])
                del chairs[event[2]]
        return -1
    

            

        

        
        
        
            