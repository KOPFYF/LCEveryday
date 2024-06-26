class Solution:
    def canWin(self, s: str) -> bool:
        @lru_cache(None)
        def dfs(s):
            for i in range(len(s) - 1):
                if s[i] == s[i + 1] == '+' and not dfs(s[:i] + '--' + s[i + 2:]):
                    return True
            return False
        
        return dfs(s)
            
        
class Solution2:
	# backtracking
    def canWin(self, s: str) -> bool:        
        for i in range(len(s)-1):
            if s[i] == '+' and s[i+1] == '+' and not self.canWin(s[:i] + '--' + s[i+2:]): 
                return True
        return False