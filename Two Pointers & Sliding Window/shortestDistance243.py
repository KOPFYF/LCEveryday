class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        # O(n) / O(1)
        min_dist = float("inf")
        i, j = -1, -1
        for idx, word in enumerate(wordsDict):
            if word in (word1, word2):
                if word == word1:
                    i = idx
                else:
                    j = idx
                # print(i, j, word)
                if i >= 0 and j >= 0:
                    min_dist = min(min_dist, abs(i - j))

        return min_dist
        
        
        idxs = defaultdict(list)
        for i, word in enumerate(wordsDict):
            if word in (word1, word2):
                idxs[word].append(i)
        res = float('inf')
        for i in idxs[word1]:
            for j in idxs[word2]:
                res = min(res, abs(i-j))
        return res