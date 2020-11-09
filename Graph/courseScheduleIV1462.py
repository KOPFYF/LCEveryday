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

#         # Floyd–Warshall Algorithm，Time O(n^3)
#         graph = [[False for i in range(n)] for j in range(n)]
#         for p in prerequisites:
#             graph[p[0]][p[1]] = True
        
#         for k in range(n):
#             for i in range(n):
#                 for j in range(n):
#                     graph[i][j] = graph[i][j] or (graph[i][k] and graph[k][j])
        
#         return [graph[i][j] for i, j in queries]


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