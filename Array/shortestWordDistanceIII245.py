class Solution:
    def shortestWordDistance(self, words: List[str], word1: str, word2: str) -> int:
        # Only check if word1 and word2 is same once and save it in a boolean and use it wisely. 
        # This way we don't lose the speed and the code remain clean.
        # O(n) / O(1)
        n = len(words)
        res = n
        w1 = -1
        w2 = -1
        for i in range(n):
            if words[i] == word1:
                w1 = i
                if w2 != -1:
                    res = min(w1-w2, res)
            if words[i] == word2:
                w2 = i
                if w1 != -1 and w1 != w2:
                    res = min(w2-w1, res)
        return res
        
        
        
        # TLE
        idxs = defaultdict(list)
        for i, word in enumerate(wordsDict):
            idxs[word].append(i)
        
        res = float('inf')
        if word1 != word2:
            for i in idxs[word1]:
                for j in idxs[word2]:
                    res = min(res, abs(i - j))
            return res
        else:
            for i, j in zip(idxs[word1], idxs[word1][1:]):
                res = min(res, abs(i - j))
            return res