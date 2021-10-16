from collections import defaultdict, deque

class Solution:
    def minJumps(self, arr: List[int]) -> int:
        # O(n) / O(n)
        # underline issue is to have one visited set to record index
        # and implicitly mark visited num
        # same trick as bus route
        d = defaultdict(list)
        for i in range(len(arr)):
            d[arr[i]].append(i)
            
        queue = deque([(0, 0)]) # step, idx
        visit = set([0]) # seen idx

        while queue:
            step, cur_idx = queue.popleft()
            if cur_idx == len(arr)-1:
                return step
            
            for nxt_idx in d[arr[cur_idx]] + [cur_idx - 1, cur_idx + 1]:
                if 0 <= nxt_idx < len(arr) and nxt_idx not in visit:
                    visit.add(nxt_idx)
                    queue.append((step + 1, nxt_idx))
                    
            del d[arr[cur_idx]] # mark number as visited




class BUS_ROUTES_815:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        seen = set([source]) # seen stop
        bfs = deque([(source, 0)])
        while bfs:
            stop, step = bfs.popleft()
            if stop == target:
                return step
            for nxt_bus in stop2bus[stop]:
                for nxt_stop in routes[nxt_bus]:
                    if nxt_stop not in seen:
                        seen.add(nxt_stop) # seen stop
                        bfs.append((nxt_stop, step + 1))
                routes[nxt_bus] = [] # seen this bus
        return -1