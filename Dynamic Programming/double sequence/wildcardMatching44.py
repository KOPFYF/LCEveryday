class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # dp O(mn), dp[n] means substring s[:n] is matched or not
        # '?' Matches any single character.
        # '*' Matches any sequence of characters (including the empty sequence !!).
        m, n = len(s), len(p)
        dp = [[False for _ in range(n+1)] for _ in range(m+1)]
        dp[0][0] = True
        
        for i in range(1, m+1):
            dp[i][0] = False
        for j in range(1, n+1):
            if p[j - 1] == '*': # continuous * could match empty
                dp[0][j] = True
            else:
                break
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                if p[j-1] != '*': # not star, try to match i & j and consider ?(Matches any single character)
                    dp[i][j] = dp[i-1][j-1] and (s[i-1] == p[j-1] or p[j-1] == '?')
                else:
                    # dp[i-1][j] just means * match i, dp[i][j-1] means * match empty
                    dp[i][j] = dp[i-1][j] or dp[i][j-1] # or dp[i-1][j-1], no need actually
        
        return dp[m][n]
    
    
        # recursion
        # if not pattern: return not text
        first = bool(text) and pattern[0] in [text[0], '?', '*']
        if len(pattern) > 1 and pattern[1] == '*':
            return first and self.isMatch(text[1:], pattern) or self.isMatch(text, pattern[2:]) # * matches 0 times
        else:
            return first and self.isMatch(text[1:], pattern[1:])
        
        
        
        