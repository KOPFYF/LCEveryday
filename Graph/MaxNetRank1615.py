class Solution(object):
    def maximalNetworkRank(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        # time O(n^2), space O(n^2)
        G = defaultdict(set) 
        citys = [0] * n # degree of connection
        for u, v in roads:
            G[u].add(v)
            G[v].add(u)
            citys[u] += 1
            citys[v] += 1

        res = 0
        for i in range(n):
            for j in range(i + 1, n):
                # Try every pair of different cities and calculate its network rank.
                # The network rank of two vertices is the sum of their degrees minus inbetween.
                res = max(res, citys[i] + citys[j] - int(i in G[j]))
        return res