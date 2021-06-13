'''
For each worker, create a sorted list of distances to each bike. The elements of the list are tuples (distance, worker, bike).
For each worker, add the tuple with the shortest distance to the heap.
Until each worker has a bike, pop the smallest distance from the heap.
If this bike is not used, update the result for this worker, else add the next closest tuple for this worker to the heap.

'''

class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:

        distances = []     # distances[worker] is tuple of (distance, worker, bike) for each bike 
        for i, (x, y) in enumerate(workers):
            distances.append([])
            for j, (x_b, y_b) in enumerate(bikes):
                distance = abs(x - x_b) + abs(y - y_b)
                distances[-1].append((distance, i, j))
            distances[-1].sort(reverse = True)  # reverse so we can pop the smallest distance
        
        result = [None] * len(workers)
        used_bikes = set()
        queue = [distances[i].pop() for i in range(len(workers))]   # smallest distance for each worker
        heapq.heapify(queue)
        
        while len(used_bikes) < len(workers):
            _, worker, bike = heapq.heappop(queue)
            if bike not in used_bikes:
                result[worker] = bike
                used_bikes.add(bike)
            else:
                heapq.heappush(queue, distances[worker].pop())  # bike used, add next closest bike
        
        return result
        
        
        
        # assign a bike(M) to each worker(N). N <= M
        # calculates manhattan distance of all possible combinations
        m, n = len(bikes), len(workers)
        dists = []
        for i, worker in enumerate(workers):
            for j, bike in enumerate(bikes):
                dist = abs(worker[0] - bike[0]) + abs(worker[1] - bike[1])
                dists.append((dist, i, j)) # dist, worker_id, bike_id
        
        dists.sort() # O(mnlogmn)
        
        res = [-1] * n
        seen = set()
        for dist, i, j in dists:
            if res[i] == -1 and j not in seen:
                res[i] = j
                seen.add(j)
        return res