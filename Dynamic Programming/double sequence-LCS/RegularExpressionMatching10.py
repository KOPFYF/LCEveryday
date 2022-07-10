class Solution:
    def isMatch(self, text: str, pattern: str) -> bool:
        # dp(i, j): does text[i:] and pattern[j:] match?
        m, n = len(text), len(pattern)
        
        @lru_cache(None)
        def dfs(i, j):
            if j == n:
                return i == m
            # cur_match matches i
            cur_match = (i < m) and pattern[j] in (text[i], '.')
            if j + 1 < n and pattern[j+1] == '*':
                # if * in next, skip it(match zero) or match i+1
                return dfs(i, j + 2) or (cur_match and dfs(i+1, j))
            else:
                # no start, cur_match, i++, j++
                return cur_match and dfs(i+1, j+1)
            
        return dfs(0, 0)


class Solution(object):
    def isMatch(self, text, pattern):
        dp = [[False] * (len(pattern) + 1) for _ in range(len(text) + 1)]

        dp[-1][-1] = True
        for i in range(len(text), -1, -1):
            for j in range(len(pattern) - 1, -1, -1):
                first_match = i < len(text) and pattern[j] in {text[i], '.'}
                if j+1 < len(pattern) and pattern[j+1] == '*':
                    dp[i][j] = dp[i][j+2] or first_match and dp[i+1][j]
                else:
                    dp[i][j] = first_match and dp[i+1][j+1]

        return dp[0][0]



class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m = len(s)
        n = len(p)
        #table[(i,j)] = 检查是否s[i:len(s)] 匹配 p[j:len(p)]，匹配返回True
        table = {}
        def dp(i,j):
            #若p到底，检查是否s到底
            if j == n:
                return i == m
            #若s到底，检查剩下的p是否符合 #*#* pattern
            if i == m:
                #剩下的p不是偶数，证明不是以上pattern
                if (n - j) % 2:
                    return False
                #检查是否偶数位为“*”
                for z in range(j,n-1,2):
                    if p[z+1] != "*":
                        return False
                return True
            #检查是否存在dp table里面
            if (i,j) in table:
                return table[(i,j)]
            
            res = False
            #若s[i] == p[j] 或者 p[j] == "."
            if s[i] == p[j] or p[j] == ".":
                #若p[j+1] == "*"
                if j <= n-2 and p[j+1] == "*":
                    #匹配多次 或者 匹配0次
                    res = dp(i+1,j) or dp(i,j+2)
                #无“*”，检查下一个字母
                else:
                    res = dp(i+1,j+1)
            #若s[i] ！= p[j]
            else:
                #若p[j+1] == "*"，则匹配0次
                if j <= n-2 and p[j+1] == "*":
                    res = dp(i,j+2)
                #无“*”，直接不匹配
                else:
                    res = False
            
            table[(i,j)] = res
            
            return res
        return dp(0,0)


class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        LCS
        dp[i][j] means the match status between p[:i] and s[:j]
        """
        m, n = len(p), len(s)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = 1
        
        # s is empty but p is not, only * will match
        for i in range(1, m):
            dp[i + 1][0] = dp[i - 1][0] and p[i] == '*'
        
        for i in range(m):
            for j in range(n):
                if p[i] != '*':
                    dp[i + 1][j + 1] = dp[i][j] and (p[i] == '.' or p[i] == s[j])
                else: # '*' matches recursively
                    dp[i + 1][j + 1] = dp[i - 1][j + 1] or dp[i][j + 1]
                    if p[i - 1] == s[j] or p[i - 1] == '.':
                        dp[i + 1][j + 1] |= dp[i + 1][j] # s[j] could be matched by p[i - 1]
        return dp[-1][-1]


class Solution2(object):
    def isMatch(self, s, p):
        # compress to 1D
        prev = [False, True]
        for j in range(len(p)):
            prev.append(p[j]=='*' and prev[j])

        for i in range(len(s)):
            curr = [False, False]
            for j in range(len(p)):
                if p[j]=='*':
                    curr.append(curr[j] or curr[j+1] or (prev[j+2] and p[j-1] in (s[i], '.')))
                else:
                    curr.append(prev[j+1] and p[j] in (s[i], '.'))
            prev = curr
        return prev[-1]