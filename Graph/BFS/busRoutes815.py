class Solution(object):
    def numBusesToDestination(self, routes, S, T):
        """
        :type routes: List[List[int]]
        :type S: int
        :type T: int
        :rtype: int
        """       
        if S == T: return 0
        stopBoard = defaultdict(list)
        for bus, stops in enumerate(routes):
            for stop in stops:
                stopBoard[stop].append(bus)
                    
        seen = set([S]) # seen record the stop
        bfs = deque([(S, 0)])
        while bfs:
            stop, step = bfs.popleft()
            if stop == T:
                return step
            for i in stopBoard[stop]: # current bus we can pick
                for new_stop in routes[i]: # all stops for current bus
                    if new_stop not in seen: # seen this stop before
                        seen.add(new_stop) 
                        bfs.append((new_stop, step + 1))
                routes[i] = [] # seen this bus before, clear it
        return -1


class Solution(object):
    def numBusesToDestination(self, routes, S, T):
        """
        :type routes: List[List[int]]
        :type S: int
        :type T: int
        :rtype: int
        """ 
        if S == T: return 0
        stopBoard = defaultdict(list)
        for bus, stops in enumerate(routes):
            for stop in stops:
                stopBoard[stop].append(bus)
                    
        seen = set() # seen record the bus
        bfs = deque([(S, 0)])
        while bfs:
            stop, step = bfs.popleft()
            if stop == T:
                return step
            for i in stopBoard[stop]: # current bus we can pick
                if i not in seen:
                    seen.add(i)
                    for new_stop in routes[i]: # all stops for current bus
                        bfs.append((new_stop, step + 1))
        return -1