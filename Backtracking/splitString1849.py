class Solution:
    def splitString(self, s: str) -> bool:
        @lru_cache(None)
        def dfs(i, prev):
            # try head [1~j] and dfs(j+1)
            if i == len(s):
                return True
            for j in range(i, len(s)):
                val = int(s[i:j+1])
                if prev - val == 1 and dfs(j+1, val):
                    return True
            return False
                            
        for i in range(len(s) - 1):
            val = int(s[:i+1])
            if dfs(i+1, val): 
                return True
        return False
    

class Solution1:
    def splitString(self, s: str) -> bool:    
        self.res = False
        for i in range(1, len(s)):
            self.dfs(int(s[:i]), s, 0)
        return self.res
        
    def dfs(self, num, s, level):
        if num < 0:
            return
        if len(s) == 0 or (num == int(s) and level > 0):
            self.res = True
        
        for j in range(1, len(s)):
            head, nxt_s = int(s[:j]), s[j:]
            if num == head:
                self.dfs(num - 1, nxt_s, level + 1)
        
        