class Solution(object):
    def camelMatch(self, queries, pattern):
        """
        :type queries: List[str]
        :type pattern: str
        :rtype: List[bool]
        """
        def helper(query, pattern):
            n, m = len(query), len(pattern)
            if m > n: return False
            i, j = 0, 0
            for i in range(n):
                if j < m and query[i] == pattern[j]:
                    j += 1
                elif 'A' <= query[i] <= 'Z':
                    return False
            return j == m
        
        return [helper(query, pattern) for query in queries]