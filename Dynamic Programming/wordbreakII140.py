class Solution:
    def __init__(self):
        self.res = []
        
    def dfs(self, s, path, dp, ind, word_dict):
        if dp[ind + len(s)]: # pruning
            if not s:
                self.res.append(path.strip())
            
            for i in range(1, len(s)+1):
                if s[:i] in word_dict:
                    self.dfs(s[i:], path + " " + s[:i], dp, ind + i, word_dict)
                    
    def word_break1(self, s, word_dict):
        N = len(s)
        dp = [False] * (N + 1)
        dp[0] = True
        for i in range(N):
            for j in range(i, N + 1):
                if dp[i] and s[i:j] in word_dict:
                    dp[j] = True
        # print(dp)
        return dp
        
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        if not s:
            return [""]
        wordDict = set(wordDict)
        dp = self.word_break1(s, wordDict)
        # print(dp)
        self.dfs(s, "", dp, 0, wordDict)
        return self.res