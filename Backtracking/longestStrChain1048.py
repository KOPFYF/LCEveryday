class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        # O(l^2 n)
        wordSet = set(words)
        
        @cache
        def dfs(word):
            res = 1
            for i in range(len(word)): #O(n)
                nxt_word = word[:i] + word[i+1:]
                if nxt_word in wordSet: # O(l)
                    res = max(res, dfs(nxt_word) + 1)
            return res
        
        return max(dfs(word) for word in words)