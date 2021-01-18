class Solution_bu:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [True] + [False] * n
        
        for i in range(1, n + 1):
            for word in wordDict:
                if dp[i - len(word)] and s[i - len(word):i] == word:
                    dp[i] = True
                    break
        return dp[-1]


class Solution_td:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # top down
        wordSet = set(wordDict)
        n = len(s)
   
        @lru_cache(None)
        def dfs(k):
            if k == n: return True
            for i in range(k + 1, n + 1):
                if s[k:i] in wordSet and dfs(i):
                    return True        
            return False
        
        return dfs(0)
    
        # top down, tle
        wordDict = set(wordDict)
        memo = {}
        def dfs(pos):
            if pos == len(s): return True
            if pos in memo: return memo[pos]
            for i in range(pos + 1, len(s) + 1):
                if s[pos:i] in wordDict and dfs(i):
                    memo[i] = True
                    return True
            memo[i] = False
            return False
            
        return dfs(0)       