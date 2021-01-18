class Solution(object):
    def minimumHammingDistance(self, source, target, edges):
        """
        :type source: List[int]
        :type target: List[int]
        :type allowedSwaps: List[List[int]]
        :rtype: int
        """
        res = n = len(source)
        G = [set() for i in xrange(n)]
        for i, j in edges:
            G[i].add(j)
            G[j].add(i)
        seen = [0] * n

        def dfs(i):
            seen[i] = 1
            found.append(i)
            for j in G[i]:
                if not seen[j]:
                    dfs(j)

        for i in xrange(n):
            if seen[i]: continue
            found = []
            dfs(i)
            count1 = collections.Counter(source[j] for j in found)
            count2 = collections.Counter(target[j] for j in found)
            res -= sum((count1 & count2).values())
        return res