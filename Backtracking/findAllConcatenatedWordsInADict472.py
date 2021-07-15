class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        # O(nlogn + n * l * l) / O(n l)
        word_set = set(words)
        
        @lru_cache(None)
        def dfs(word, i):
            if not word:
                return False # corner case [""]
            if i == len(word):
                return True
            for j in range(i, len(word)):
                if word[i:j+1] in word_set and dfs(word, j+1):
                    return True
            return False
        
        res = []
        for word in words:
            word_set.remove(word)
            if dfs(word, 0):
                res.append(word)
            word_set.add(word)
        return res