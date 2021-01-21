class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        # dfs + memo
        memo = {}
        words = set(words)
        def dfs(word):
            if word in memo:
                return memo[word]
            for second_idx in range(1, len(word)):
                prefix, suffix = word[:second_idx], word[second_idx:]
                if (prefix in words and suffix in words) or \
                    (prefix in words and dfs(suffix)): # base case (or) recursion
                    memo[word] = True
                    return True
            memo[word] = False
            return False
        
        return [word for word in words if dfs(word)]
        
        # TLE backtracking
        res = []
        words_dict = set(words)
        
        def dfs(word, d):
            if word in d:
                return True
            for i in range(len(word), 0, -1):
                prefix = word[:i]
                if prefix in d and dfs(word[i:], d):
                    return True
            return False
        
        for word in words:
            words_dict.remove(word) 
            # exclude the word itself, at least two shorter words!
            if dfs(word, words_dict):
                res.append(word)
            words_dict.add(word)
        return res
    


                
            