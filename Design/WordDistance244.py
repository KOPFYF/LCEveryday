class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.idxs = defaultdict(list)
        for i, word in enumerate(wordsDict):
            self.idxs[word].append(i)
    
    @lru_cache(None)
    def shortest(self, word1: str, word2: str) -> int:
        # O(n^2) / O(n)
        res = float('inf')
        for i in self.idxs[word1]:
            for j in self.idxs[word2]:
                res = min(res, abs(i - j))
        return res