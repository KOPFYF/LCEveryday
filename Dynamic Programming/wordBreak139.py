class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [True] + [False] * n
        
        for i in range(1, n + 1):
            for word in wordDict:
                if dp[i - len(word)] and s[i - len(word):i] == word:
                    dp[i] = True
                    break
        return dp[-1]