class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        '''
        Given:
        1. you can reach any intersection from any other intersection
        2. at most one road between any two intersections
        Q:
        how many ways you can travel from intersection 0 to intersection n - 1 in the shortest amount of time
        Thinking:
        Use Dijkstra algorithm, but also we need to keep not only distances to nodes, but counts as well.

        If we meet candidate == dist[neib], it means we found one more way to reach node with minimal cost.
        If candidate < dist[neib], it means that we found better candidate, so we update distance and put cnt[neib] = cnt[idx].
        Complexity
        It is O((E+V) log V) for time as classical Dijkstra and O(E+V) for space
        '''
        # Dijkstra + DP, cache dist and COUNT
        mod = 10**9 + 7
        graph = collections.defaultdict(dict)
        for u, v, w in roads:
            graph[u][v] = w
            graph[v][u] = w
        
        dist, cnt = [float('inf')] * n, [0] * n
        dist[0], cnt[0] = 0, 1
        hq = [(0, 0)] # (dist, node)
        
        while hq:
            cur_dist, cur_node = heapq.heappop(hq)
            if cur_node == n - 1:
                return cnt[n-1] % mod
            for nxt_node, w in graph[cur_node].items():
                nxt_dist = dist[cur_node] + w
                
                # extra dp to count when tie
                if nxt_dist == dist[nxt_node]:
                    cnt[nxt_node] += cnt[cur_node]
                
                # normal Dijkstra
                if nxt_dist < dist[nxt_node]:
                    dist[nxt_node] = nxt_dist
                    heapq.heappush(hq, (nxt_dist, nxt_node))
                    # update cnt as the same since it's the unique shortest path
                    cnt[nxt_node] = cnt[cur_node] 