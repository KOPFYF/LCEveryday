class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        def dfs(i):
            if i <= n:
                result.append(i)
                for d in xrange(10):
                    dfs(10 * i + d)
        result = []
        for i in range(1, 10):
            dfs(i)
        return result
    
        tmp = sorted([str(i) for i in range(1, n + 1)])
        return [int(i) for i in tmp]
        
        return map(int, sorted(map(str, xrange(1, n + 1))))
        
        return sorted(range(1, n + 1), key=str)
    
        return sorted(range(1, n + 1), lambda a, b: cmp(str(a), str(b)))