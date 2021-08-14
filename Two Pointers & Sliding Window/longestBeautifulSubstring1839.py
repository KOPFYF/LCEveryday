class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        i, res = 0, 0
        seen = set()
        for j in range(len(word)):
            if not j or word[j] >= word[j - 1]:
                # grow right pointer j
                seen.add(word[j])
                # if len(set(word[i:j+1])) == 5: # TLE
                if len(seen) == 5:
                    res = max(res, j - i + 1)
            else:
                # grow left pointer i
                i = j 
                seen = set([word[j]])
        return res