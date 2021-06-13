class Solution1:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        # O(nlogk)
        available = list(range(k)) # heap 1, record available server
        busy = [] # heap 2, (end time, server id)
        res = [0] * k
        
        for i, (a, l) in enumerate(zip(arrival, load)): # simulation
            # print(available, busy)
            while busy and busy[0][0] <= a: 
                # current start time >= busy server end time, pop out and push into available 
                _, end_server_id = heapq.heappop(busy)
                # print('while:', i, end_server_id, i + (end_server_id - i) % k)
                heapq.heappush(available, i + (end_server_id - i) % k) # circular
            
            if available: 
                j = heapq.heappop(available) % k # next available server id in the circle
                heapq.heappush(busy, (a + l, j))
                res[j] += 1
        
        maxm = max(res)
        return [i for i in range(k) if res[i] == maxm]


# SortedList is an interesting data structure of sortedcontainers which is an external library 
# and doesn't come with Python by default. 
from sortedcontainers import SortedList

class Solution2:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        freq = [0]*k
        busy = [] # min-heap 
        free = SortedList(range(k)) # balanced bst
        
        for i, (ta, tl) in enumerate(zip(arrival, load)): 
            while busy and busy[0][0] <= ta: 
                _, ii = heappop(busy)
                free.add(ii)
            
            if free: 
                ii = free.bisect_left(i%k) % len(free) # this line is different from soln 1
                server = free.pop(ii)
                freq[server] += 1
                heappush(busy, (ta+tl, server))
        
        mx = max(freq)
        return [i for i, x in enumerate(freq) if x == mx]