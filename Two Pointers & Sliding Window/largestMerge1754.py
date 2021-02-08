class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        m, n = len(word1), len(word2)
        i, j = 0, 0
        res = ""
        while i < m and j < n:
            if word1[i] > word2[j]:
                res += word1[i]
                i += 1
            elif word1[i] < word2[j]:
                res += word2[j]
                j += 1
            else:
                if word1[i+1:] > word2[j+1:]:
                    res += word1[i]
                    i += 1
                else:
                    res += word2[j]
                    j += 1  
            # print(res, i, j)
        while i < m:
            res += word1[i]
            i += 1
        while j < n:
            res += word2[j]
            j += 1
        return res