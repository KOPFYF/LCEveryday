class Solution:
    def numBusesToDestination(self, routes, S, T):
        """
        :type routes: List[List[int]]
        :type S: int
        :type T: int
        :rtype: int
        """
        stopToRoute = collections.defaultdict(set)
        
        for i, stops in enumerate(routes):
            for stop in stops: 
                stopToRoute[stop].add(i)
                
        bfs = [(S,0)]
        seenStops = {S} # seen stop
        seenRoutes = set() # seen bus
        
        for stop, count in bfs:
            if stop == T: 
                return count
            
            for routeIndex in stopToRoute[stop]:
                if routeIndex not in seenRoutes:
                    seenRoutes.add(routeIndex)
                    for next_stop in routes[routeIndex]:
                        if next_stop not in seenStops:
                            seenStops.add(next_stop)
                            bfs.append((next_stop, count+1))
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
                    
        seen = set() # seen record the bus, I like this idea!
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