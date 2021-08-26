'''
Solution 2: Bitmask + BFS every cities

Since n <= 15, there is a maximum 2^15 subset of cities numbered from 1 to n.
For each of subset of cities, we calculate the maximum distance between any two cities in our subset.
For each city in our subset:
Using bfs() or dfs() to calculate distance between city to other cities in subset.
If citiy can't reach to any other cities then subset form an invalid subtree.
Return distance of 2 cities with maxium distance.
Complexity

Time: O(2^n * n^2)
Space: O(n^2)
'''

class Solution:
    def countSubgraphsForEachDiameter(self, n: int, edges: List[List[int]]) -> List[int]:
        # bitmask + BFS
        graph = defaultdict(list)
        for u, v in edges:
            graph[u - 1].append(v - 1)
            graph[v - 1].append(u - 1)
        
        def bfs(cur, subtree):
            # O(n)
            # input, current node, a set of cities in that subtree
            # return (farthest Dist, seen set)
            
            seen, bfs, farthestDist = set([cur]), deque([(cur, 0)]), 0
            while bfs:
                node, dist = bfs.popleft()
                farthestDist = dist
                for nxt_node in graph[node]:
                    if nxt_node not in seen and nxt_node in subtree:
                        seen.add(nxt_node)
                        bfs.append((nxt_node, dist + 1))
            return farthestDist, seen
        
        def maxDist(mask):
            # O(n^2), for loop * BFS
            # given the mask: state of subtree
            # return: maximum distance between any two cities in our subset. 
            subtree = set()
            for i in range(n):
                if mask & (1 << i):
                    subtree.add(i)
            
            res = 0
            for city in subtree:
                farthestDist, seen = bfs(city, subtree)
                if len(seen) < len(subtree):
                    return 0 # if seen set != subtree, not reachable
                res = max(res, farthestDist)
            return res
        
        res = [0] * (n - 1)
        for mask in range(1, 1 << n): # O(2^n)
            d = maxDist(mask)
            if d > 0:
                res[d - 1] += 1
        return res


'''
Solution 1: Bitmask + Floyd Warshall

Using Floyd-Warshall algorithm to calculate minimum distance between any node to any other node.
Since n <= 15, there is a maximum 2^15 subset of cities numbered from 1 to n.
For each of subset of cities:
Our subset forms a subtree if and only if number of edges = number of cities - 1
Iterate all pair of cities to calculate number of edges, number of cities, maximum distance between any 2 cities
Complexity

Time: O(2^n * n^2)
Space: O(n^2)

'''
class Solution1(object):
    def countSubgraphsForEachDiameter(self, n, edges):
        def maxDistance(state):  # return: maximum distance between any two cities in our subset. O(n^2)
            cntEdge, cntCity, maxDist = 0, 0, 0
            for i in range(n):
                if (state >> i) & 1 == 0: continue # Skip if city `i` not in our subset
                cntCity += 1
                for j in range(i + 1, n):
                    if (state >> j) & 1 == 0: continue # Skip if city `j` not in our subset
                    cntEdge += dist[i][j] == 1
                    maxDist = max(maxDist, dist[i][j])
            if cntEdge != cntCity - 1: return 0 # Subset form an invalid subtree!
            return maxDist

        INF = n # Since cities form a tree so maximum distance between 2 cities always < n
        dist = [[INF] * n for _ in range(n)]
        for u, v in edges:
            dist[u-1][v-1] = dist[v-1][u-1] = 1
        
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
        
        ans = [0] * (n - 1)
        for state in range(1, 2**n):
            d = maxDistance(state)
            if d > 0: ans[d - 1] += 1
        return ans