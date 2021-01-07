class Solution_topo:
    def checkIfPrerequisite(self, n: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # O(V + E + Q) / O(V + E + Q)
        def topo_sort(n, pre):
            # O(V + E) / O(V + E)
            graph = defaultdict(list)
            indegrees = {v:0 for v in range(n)}
            preset = defaultdict(set)
            for i, j in pre:
                preset[j].add(i) # set to keep track of prerequisite
                graph[i].append(j)
                indegrees[j] += 1
            
            bfs = deque([k for k, v in indegrees.items() if v == 0])
            while bfs:
                cur = bfs.popleft()
                for nxt in graph[cur]:
                    preset[nxt] = preset[nxt] | preset[cur] # union set
                    indegrees[nxt] -= 1
                    if indegrees[nxt] == 0:
                        bfs.append(nxt)
            return preset
        
        preset = topo_sort(n, prerequisites)
        # print(preset) # {1: {0}, 2: {0, 1}, 3: {0, 1, 2}, 4: {0, 1, 2, 3}, 0: set()}
        
        return [True if u in preset[v] else False for u, v in queries]


class Solution1_py3_cache:
    def checkIfPrerequisite(self, n: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # DFS + memo (aka Top down DP)
        # dp[u, v] = true if u is a pre of v
        # normally we write dfs as a function to detect cycle and run topo-sort
        # but here we dont need the whole chain, but only pairs of courses so memo will do
        G = collections.defaultdict(set)
        result = []
        for u,v in prerequisites:
            G[u].add(v) # build graph

        from functools import lru_cache
        @lru_cache(maxsize=None)
        def dfs(source, target):
            if source == target:
                return True
            
            for t in G[source]:
                if dfs(t, target):
                    return True
            return False
            
        for query in queries:
            result.append(dfs(query[0], query[1]))
        return result



class Solution2(object):
    def checkIfPrerequisite(self, n, pre, queries):
        """
        :type n: int
        :type prerequisites: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        # DFS + memo (aka Top down DP)
        # dp[u, v] = true if u is a pre of v
        # normally we write dfs as a function to detect cycle and run topo-sort
        # but here we dont need the whole chain, but only pairs of courses so memo will do
        G = collections.defaultdict(set)
        result = []
        memo = {}
        for u,v in pre:
            memo[(u, v)] = True # base cases
            G[u].add(v) # build graph

        def dfs(source, target):
            if (source, target) in memo:
                return memo[(source, target)]
            
            for t in G[source]:
                if dfs(t, target):
                    memo[(source, target)] = True
                    return True
                
            memo[(source, target)] = False
            return False
            
        for query in queries:
            result.append(dfs(query[0], query[1]))
        return result


class Solution3(object):
    def checkIfPrerequisite(self, n, pre, queries):
        # Floyd–Warshall Algorithm，Time O(n^3)
        graph = [[False for i in range(n)] for j in range(n)]
        for p in prerequisites:
            graph[p[0]][p[1]] = True
        
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    graph[i][j] = graph[i][j] or (graph[i][k] and graph[k][j])
        
        return [graph[i][j] for i, j in queries]