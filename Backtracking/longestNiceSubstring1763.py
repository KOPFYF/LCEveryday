class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        # recursion
        chars = set(s)
        for i in range(len(s)):
            if s[i].swapcase() not in chars:
            # if not (s[i].lower() in chars and s[i].upper() in chars):
                s1 = self.longestNiceSubstring(s[:i])
                s2 = self.longestNiceSubstring(s[i+1:])
                return s2 if len(s2) > len(s1) else s1  
        return s   
        
        # brute force
        res = ""
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                if all(s[k].swapcase() in s[i:j] for k in range(i, j)): 
                    res = max(res, s[i:j], key=len)
        return res
        
        
        # O(n)  divide and conquer
        # ex; "Ya  z  aAayayy  z  aaa  z  ya"
        chars = set(s)
        i = 0
        res = ""
        for j, ch in enumerate(s):
            if ch.swapcase() not in chars:
                res = max(res, self.longestNiceSubstring(s[i:j]), key=len)
                i = j + 1
        return max(res, self.longestNiceSubstring(s[i:]), key=len) if i else s