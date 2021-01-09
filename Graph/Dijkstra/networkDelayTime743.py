class Solution(object):
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        # bellman-ford (relax edge) Time: average O(E), worst O(VE) Space: O(V+E)
        dist = [float('inf') for _ in range(N)]
        dist[K - 1] = 0
        for _ in range(N - 1): # for each vertex
            for u, v, w in times: # for each edge
                if dist[u - 1] + w < dist[v - 1]:
                    dist[v - 1] = dist[u - 1] + w
        return max(dist) if max(dist) < float('inf') else -1
    
        # Dijkstra， time O(E+VlogV), space O(V+E)
        weight = collections.defaultdict(dict)
        for u, v, w in times:
            weight[u][v] = w
        heap = [(0, K)]
        dist = {}
        while heap:
            time, u = heapq.heappop(heap)
            if u not in dist:
                dist[u] = time
                for v in weight[u]:
                    heapq.heappush(heap, (dist[u] + weight[u][v], v))
        return max(dist.values()) if len(dist) == N else -1
    
    
        # Floyd-Warshall, Time: O(V^3), Space: O(V^2)
        dist = [[float("inf") for _ in range(N)] for _ in range(N)]
        for u, v, w in times:
            dist[u-1][v-1] = w
        for i in range(N):
            dist[i][i] = 0
        for k in range(N):
            for i in range(N):
                for j in range(N):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
        return max(dist[K-1]) if max(dist[K-1]) < float("inf") else -1
        
        # SPFA, Time: average O(E), worst O(VE) Space: O(V+E)
        dist = [float("inf") for _ in range(N)]
        K -= 1
        dist[K] = 0
        weight = collections.defaultdict(dict)
        for u, v, w in times:
            weight[u-1][v-1] = w
        queue = collections.deque([K])
        while queue:
            u = queue.popleft()
            for v in weight[u]:
                if dist[u] + weight[u][v] < dist[v]:
                    dist[v] = dist[u] + weight[u][v]
                    queue.append(v)
        return max(dist) if max(dist) < float("inf") else -1
        
        
        
        # heap
        hq = [(0, K)] # heap (cost, node)
        d = {} # hashmap storing cost (node: cost)
        adj = collections.defaultdict(list) # adjacent graph
        for u, v, w in times:
            adj[u].append((v, w))
        
        while hq:
            curCost, curNode = heapq.heappop(hq)
            if curNode not in d:
                d[curNode] = curCost
                for nxtNode, weight in adj[curNode]:
                    heapq.heappush(hq, (curCost + weight, nxtNode))
        return max(d.values()) if len(d) == N else -1
            