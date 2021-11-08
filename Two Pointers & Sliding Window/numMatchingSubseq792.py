class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        
        @cache
        def isSub(s, t):
            # return true if s is subseq of t
            m, n = len(s), len(t)
            if m > n:
                return False
            i, j = 0, 0
            while i < m and j < n:
                if s[i] == t[j]:
                    i += 1
                    j += 1
                else:
                    j += 1
            return i == m
        
        res = 0
        for word in words:
            if isSub(word, s):
                res += 1
        return res