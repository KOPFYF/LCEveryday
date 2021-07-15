'''
for a given node - it is possible that we encounter - a route which takes less time later on in our search.
'''
class Solution:
    def minCost(self, maxTime: int, edges: List[List[int]], passingFees: List[int]) -> int:
        # djistra, (cost, time, vertex)
        n = len(passingFees)
        graph = defaultdict(list)
        for u, v, t in edges:
            graph[u].append((v, t))
            graph[v].append((u, t)) # graph record time&node
        
        pq = [(passingFees[0], 0, 0)]
        times = {}
        
        while pq:
            cost, node, time = heapq.heappop(pq)
            if time > maxTime:
                continue
            if node == n - 1:
                return cost
            
            if node not in times or times[node] > time:
                times[node] = time
                for nxt_node, nxt_time in graph[node]:
                    heapq.heappush(pq, (cost + passingFees[nxt_node], nxt_node, time + nxt_time))
        return -1
        