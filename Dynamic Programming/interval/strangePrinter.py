class Solution(object):
    def strangePrinter(self, s):
        """
        :type s: str
        :rtype: int
        """
        # top-down dp, time O(n^3) space o(n^2), 752 ms with no dedup, 424 ms with dedup    
        s = ''.join(a for a, b in zip(s, '#' + s) if a != b) # dedup
        memo = {}
        def dfs(i, j):
            if i > j: 
                return 0
            if (i, j) in memo:
                return memo[(i, j)]
            res = dfs(i + 1, j) + 1 # upper bound, assume s[i] != s[k] for any i < k <= j
            for k in range(i + 1, j + 1): 
                # search range [i + 1 ... j]
                # 0 <= i < k <= j < n
                # a b a c c c
                # i   k     j
                if s[k] == s[i]:
                    res = min(res, dfs(i, k - 1) + dfs(k + 1, j))
            memo[(i, j)] = res
            return res
        
        return dfs(0, len(s) - 1)