class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # Soln 1: top down 1 dim dp, j inside, i-j-1 outside
        # "(x) y" where x and y are combinations of brackets of that size and x + y = n-1
        # so (j)k with j + k = i - 1
        dp = [[] for _ in range(n + 1)]
        dp[0].append("") # init case, when n = 0, put empty string
        
        for i in range(n+1):
            for j in range(i):
                dp[i] += ['(' + x + ')' + y for x in dp[j] for y in dp[i - j - 1]]
        return dp[n]
    
        # Soln 2, backtrack
        res = []
        def helper(ls, s, l, r, n):
            print(s)
            if len(s) == n * 2:
                # if we reach 2n, we append and return 
                ls.append(s)
                return
            if l < n:
                # if left parentheses not full
                helper(ls, s + '(', l + 1, r, n)
            if r < l:
                # if right < left, need right bracket to balance
                helper(ls, s + ')', l, r + 1, n)
            
        helper(res, "", 0, 0, n)
        return res