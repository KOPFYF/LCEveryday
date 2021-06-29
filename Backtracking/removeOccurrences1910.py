class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        while part in s:
            s = s.replace(part, '')
        return s


        r = ''
        for ch in s:
            r = (r + ch).removesuffix(part)
        return r

        # backtracking
        self.res = ""
        
        def dfs(s, p):
            if len(s) < len(p) or p not in s:
                self.res = s
                return
            
            if p in s:
                m, n = len(p), len(s)
                for i in range(n):
                    if i + m <= n:
                        if s[i:i+m] == p:
                            dfs(s[:i] + s[i+m:], p)
                            break # leftmost occurrence
        
        dfs(s, part)
        return self.res