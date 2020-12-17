class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        def dfs(pos, path):
            if len(path) == k:
                res.append(path)
            for i in range(pos, n + 1):
                dfs(i + 1, path + [i])
        dfs(1, [])
        return res